#!/usr/bin/env python3
"""
Journal Quality Analyzer
A comprehensive tool for analyzing academic journal quality using multiple data sources and AI.

Copyright © 2025 Ihababdelbasset ANNAKI
Open Source - Available for collaboration and contributions
License: MIT
"""

import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import os
import re
from datetime import datetime
import google.generativeai as genai

# Configuration constants
SCIMAGO_PATH = "data/scimago_journals.csv"  # SCImago Journal Rank dataset
PREDATORY_J_PATH = "data/predatory_journals.txt"  # Beall's list of predatory journals
PREDATORY_P_PATH = "data/predatory_publishers.txt"  # Predatory publishers list
SCOPUS_API = "https://api.elsevier.com/content/serial/title"  # Elsevier Scopus API endpoint
CACHE_EXPIRY = 86400  # 24-hour cache duration for dataset loading

@st.cache_data(ttl=CACHE_EXPIRY)
def load_data():
    # Load datasets with error handling
    try:
        scimago = pd.read_csv(SCIMAGO_PATH, sep=';')
        with open(PREDATORY_J_PATH) as f:
            predatory_journals = {line.strip().lower() for line in f if line.strip() and not line.strip().startswith('#')}
        with open(PREDATORY_P_PATH) as f:
            predatory_publishers = {line.strip().lower() for line in f if line.strip() and not line.strip().startswith('#')}
        return scimago, predatory_journals, predatory_publishers
    except Exception as e:
        st.error(f"Data loading error: {str(e)}")
        st.stop()

def filter_journals(df: pd.DataFrame, category: str) -> pd.DataFrame:
    # Use regex=False to avoid regex group warnings and match category as a substring
    filtered = df[
        df['Categories'].str.contains(category, na=False, regex=False)
    ]
    return filtered.drop_duplicates('Title')

def check_scopus_indexing(title: str, api_key: str) -> bool:
    """
    Verifies journal indexing in Scopus database

    Args:
        title: Journal title to verify
        api_key: Elsevier API key for Scopus access

    Returns:
        True if indexed in Scopus, False otherwise

    Implements rate limiting (0.5s delay) to avoid API throttling
    """
    time.sleep(0.5)  # Rate limiting
    headers = {"X-ELS-APIKey": api_key}
    params = {"title": title, "view": "STANDARD"}
    
    try:
        response = requests.get(SCOPUS_API, headers=headers, params=params)
        response.raise_for_status()
        return bool(response.json().get('serial-metadata-response', {}).get('entry'))
    except requests.HTTPError as e:
        st.error(f"Scopus API error: {str(e)}")
        return False
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return False

def is_predatory(journal: str, publisher: str, pred_j: set, pred_p: set) -> tuple:
    j_lower = journal.strip().lower()
    p_lower = publisher.strip().lower() if isinstance(publisher, str) else ""
    pred_j_matches = [pred for pred in pred_j if pred and pred == j_lower]
    pred_p_matches = [pred for pred in pred_p if pred and pred == p_lower]
    if pred_j_matches or pred_p_matches:
        st.write(f"DEBUG: Journal '{journal}' matched predatory journals: {pred_j_matches}, publisher '{publisher}' matched predatory publishers: {pred_p_matches}")
    return bool(pred_j_matches), bool(pred_p_matches)

def search_gemini_info(journal_name: str, gemini_api_key: str) -> tuple:
    """
    Uses Gemini API to extract APC, frequency, open access, and hybrid status for a journal by name.
    Returns (APC, Frequency, is_open_access, is_hybrid) as (str, str, bool or None, bool or None).
    """
    if not genai:
        return None, None, None, None
    genai.configure(api_key=gemini_api_key)
    prompt = f"""
    For the academic journal '{journal_name}', provide:
    1. The article processing charge (APC) in USD, EUR, or GBP if available, or 'None' if not found.
    2. The publication frequency (e.g., monthly, quarterly, annual, or number of issues per year), or 'None' if not found.
    3. Whether the journal is open access (answer 'Yes', 'No', or 'Unknown').
    4. Whether the journal is hybrid (answer 'Yes', 'No', or 'Unknown').
    Respond in the format:
    APC: <value>\nFrequency: <value>\nOpen Access: <Yes/No/Unknown>\nHybrid: <Yes/No/Unknown>
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        text = response.text if hasattr(response, 'text') else str(response)
        apc, freq, open_access, hybrid = None, None, None, None
        for line in text.splitlines():
            if line.lower().startswith('apc:'):
                apc = line.split(':',1)[1].strip()
            if line.lower().startswith('frequency:'):
                freq = line.split(':',1)[1].strip()
            if line.lower().startswith('open access:'):
                val = line.split(':',1)[1].strip().lower()
                if val.startswith('y'):
                    open_access = True
                elif val.startswith('n'):
                    open_access = False
                else:
                    open_access = None
            if line.lower().startswith('hybrid:'):
                val = line.split(':',1)[1].strip().lower()
                if val.startswith('y'):
                    hybrid = True
                elif val.startswith('n'):
                    hybrid = False
                else:
                    hybrid = None
        st.write(f"DEBUG: Gemini API for '{journal_name}' returned: apc={apc}, freq={freq}, open_access={open_access}, hybrid={hybrid}, raw='{text}'")
        return apc, freq, open_access, hybrid
    except Exception as e:
        st.write(f"DEBUG: Gemini API error for '{journal_name}': {str(e)}")
        return None, None, None, None

def search_specific_journal(df: pd.DataFrame, journal_name: str) -> pd.DataFrame:
    """
    Search for a specific journal by name (case-insensitive partial match)
    
    Args:
        df: SCImago dataframe
        journal_name: Journal name to search for
    
    Returns:
        Filtered dataframe containing matching journals
    """
    if not journal_name.strip():
        return pd.DataFrame()
    
    # Case-insensitive partial match on journal title
    filtered = df[
        df['Title'].str.contains(journal_name.strip(), na=False, case=False, regex=False)
    ]
    return filtered.drop_duplicates('Title')

def main():
    st.title("🔬 Journal Quality Analyzer")
    st.markdown("*Comprehensive analysis of academic journals for quality assessment*")
    
    # Sidebar with instructions and deployment info
    with st.sidebar:
        st.header("📋 Instructions")
        
        st.subheader("🔑 API Keys Required")
        st.markdown("""
        **Elsevier/Scopus API Key:**
        - Visit: [Elsevier Developer Portal](https://dev.elsevier.com/)
        - Create account → Apply for API key
        - Free tier: 5,000 requests/week
        
        **Google Gemini API Key:**
        - Visit: [Google AI Studio](https://aistudio.google.com/)
        - Create project → Generate API key
        - Free tier: 60 requests/minute
        """)        
        
        st.subheader("🔒 Privacy & Security")
        st.markdown("""
        **🛡️ Your API Keys are Safe:**
        - ✅ **Never stored** on our servers
        - ✅ **Never logged** or cached
        - ✅ **Session-only** usage (cleared when you close browser)
        - ✅ **Direct API calls** - no intermediary storage
        - ✅ **Open source** - you can verify the code
        
        **🔐 How it works:**
        - Keys are used only for real-time API requests
        - No database or file storage of credentials
        - Each session is independent and temporary
        """)
        

        
        st.subheader("ℹ️ About")
        st.markdown("""
        This tool analyzes academic journals using:
        - **[SCImago](https://www.scimagojr.com/)**: Journal rankings & categories
        - **[Scopus API](https://dev.elsevier.com/)**: Real-time indexing verification
        - **[Predatory DB](http://predatoryjournals.org/)**: Predatory journal detection
        - **[Google Gemini](https://ai.google.dev/)**: AI-powered APC analysis
        
        📋 **Non-commercial academic research use only**
        """)
        
        st.markdown("---")
        st.markdown("""
        **© 2025 Ihababdelbasset ANNAKI**  
        📧 Contact: [i.annaki@ump.ac.ma](mailto:i.annaki@ump.ac.ma) | [iannaki.developer@gmail.com](mailto:iannaki.developer@gmail.com)  
        🤝 Open Source - Available for collaboration  
        💡 Contributions welcome on [GitHub](https://github.com/thefledgedhurricane/journal-quality-analyzer)
        """)
    
    # Load data
    scimago, pred_j, pred_p = load_data()
    
    # Search mode selection
    search_mode = st.radio(
        "Choose search method:",
        ["Browse by Category", "Search Specific Journal"],
        horizontal=True
    )
    
    # Common API inputs
    scopus_key = st.text_input("Elsevier API Key (Scopus check):", type="password")
    gemini_key = st.text_input("Gemini API Key (for APC/Frequency):", type="password")
    
    filtered = pd.DataFrame()
    
    if search_mode == "Browse by Category":
        # Get unique categories
        unique_categories = sorted({
            category.strip() 
            for categories in scimago['Categories'].dropna().str.split(';') 
            for category in categories
        })
        
        category = st.selectbox("Select Category:", options=unique_categories)
        
        if st.button("Analyze Journals by Category"):
            filtered = filter_journals(scimago, category)
            
    else:  # Search Specific Journal
        journal_name = st.text_input(
            "Enter Journal Name:", 
            placeholder="e.g. Nature, Science, IEEE Transactions...",
            help="Enter full or partial journal name. Search is case-insensitive."
        )
        
        if st.button("Analyze Specific Journal"):
            filtered = search_specific_journal(scimago, journal_name)
            
            if filtered.empty and journal_name.strip():
                st.warning(f"No journals found matching '{journal_name}'. Try a different search term or check spelling.")
                return
    
    # Process results if we have filtered data
    if not filtered.empty:
        st.info(f"Found {len(filtered)} journal(s) to analyze")
        
        # Show preview of journals to be analyzed
        with st.expander("Preview journals to be analyzed"):
            st.dataframe(filtered[['Title', 'Publisher', 'Categories']].head(10))
            
        # Enrich data
        results = []
        progress_bar = st.progress(0)
        
        for i, row in enumerate(filtered.itertuples()):
            # Scopus check
            indexed = check_scopus_indexing(row.Title, scopus_key) if scopus_key else None
            st.write(f"DEBUG: Scopus check for '{row.Title}' returned: {indexed}")
            # Predatory risk (True/False)
            is_pred_journal, is_pred_publisher = is_predatory(row.Title, row.Publisher, pred_j, pred_p)
            # Gemini API for APC, Frequency, Open Access, Hybrid
            apc, freq, is_open_access, is_hybrid = search_gemini_info(row.Title, gemini_key) if gemini_key else (None, None, None, None)
            results.append({
                "Title": row.Title,
                "ISSN": row.Issn,
                "Publisher": row.Publisher,
                "Categories": row.Categories,
                "Scopus_Indexed": indexed,
                "is_predatory_journal": is_pred_journal,
                "is_predatory_publisher": is_pred_publisher,
                "APC": apc,
                "Frequency": freq,
                "is_open_access": is_open_access,
                "is_hybrid": is_hybrid
            })
            progress_bar.progress((i+1)/len(filtered))
        
        # Export results
        result_df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        search_type = "category" if search_mode == "Browse by Category" else "specific"
        csv_filename = f"exports/journal_analysis_{search_type}_{timestamp}.csv"
        xlsx_filename = f"exports/journal_analysis_{search_type}_{timestamp}.xlsx"
        os.makedirs("exports", exist_ok=True)
        result_df.to_csv(csv_filename, index=False)
        result_df.to_excel(xlsx_filename, index=False, engine="openpyxl")
        
        st.success(f"Analysis complete! {len(result_df)} journal(s) processed")
        st.dataframe(result_df)
        
        # Download buttons
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📄 Download CSV", 
                data=result_df.to_csv(index=False), 
                file_name=csv_filename,
                mime="text/csv"
            )
        with col2:
            st.download_button(
                "📊 Download XLSX", 
                data=open(xlsx_filename, "rb").read(), 
                file_name=xlsx_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    # Page configuration - must be first Streamlit command
    st.set_page_config(
        page_title="Journal Quality Analyzer",
        page_icon="favicon.svg",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    main()
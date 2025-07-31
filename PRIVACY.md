# 🔒 Privacy Policy - Journal Quality Analyzer

**Last Updated:** January 2025  
**Effective Date:** January 2025

## Overview

The Journal Quality Analyzer is committed to protecting your privacy and ensuring the security of your API credentials. This privacy policy explains how we handle your data and API keys.

## 🛡️ API Key Security Guarantee

### What We DON'T Do
- ❌ **Never store** your API keys in any database, file, or persistent storage
- ❌ **Never log** API keys in application logs, error reports, or debug outputs
- ❌ **Never cache** or persist API keys between sessions
- ❌ **Never transmit** keys to any third-party services (except direct API calls)
- ❌ **Never use** keys for any purpose other than your requested analysis

### What We DO
- ✅ **Session-only usage**: Keys exist only in browser memory during active use
- ✅ **Direct API calls**: Keys go directly to Elsevier/Google APIs as intended
- ✅ **Immediate disposal**: Keys are cleared when you close the browser/tab
- ✅ **Open source transparency**: All code is publicly auditable
- ✅ **HTTPS encryption**: All data transmission is encrypted

## 🔍 Technical Implementation Details

### Input Handling
```python
# API keys are handled using Streamlit's secure input
scopus_key = st.text_input("Elsevier API Key:", type="password")
gemini_key = st.text_input("Gemini API Key:", type="password")
```

### Function Parameters (Not Global Storage)
```python
# Keys are passed as parameters, never stored globally
def check_scopus_indexing(title: str, api_key: str) -> bool:
    # Key used only for this specific API call
    headers = {"X-ELS-APIKey": api_key}
    # No storage or logging of api_key
```

### No Caching of Sensitive Data
- Data loading functions use `@st.cache_data` only for public datasets
- API functions with keys are **never cached**
- Each API call is independent and fresh

## 📊 Data We Process

### Public Data (Cached)
- SCImago journal rankings (public dataset)
- Predatory journal lists (public dataset)
- Journal analysis results (your generated reports)

### Private Data (Never Stored)
- Your Elsevier/Scopus API keys
- Your Google Gemini API keys
- API request/response logs containing keys

## 🌐 Deployment Security

### Local Installation
- Runs entirely on your machine
- No external data transmission except API calls
- You have full control over the environment

### Hosted Deployment (Streamlit Cloud, etc.)
- Same codebase with identical privacy protections
- HTTPS encryption for all communications
- No server-side logging of sensitive inputs
- Streamlit's built-in security measures apply

## 🔐 Your Rights & Control

### You Control Your Keys
- Enter keys only when needed for analysis
- Keys are never required to browse public data
- Close browser/tab to immediately clear all session data

### Verification
- **Open Source**: Inspect our code at any time
- **No Hidden Processes**: All functionality is transparent
- **Community Audited**: Public repository allows security review

## 📞 Contact & Questions

If you have privacy concerns or questions:

- **Email**: i.annaki@ump.ac.ma | iannaki.developer@gmail.com
- **GitHub Issues**: Report security concerns via repository issues
- **Code Review**: Examine the source code directly

## 🔄 Policy Updates

This privacy policy may be updated to reflect:
- Changes in data handling practices
- New security enhancements
- Regulatory compliance requirements

Users will be notified of significant changes through:
- Repository README updates
- GitHub release notes
- Application interface notices

## ⚖️ Legal Compliance

This tool complies with:
- **GDPR**: No personal data collection or processing
- **Academic Research Ethics**: Transparent, non-commercial use
- **API Terms of Service**: Respectful use of third-party APIs
- **Open Source Licensing**: MIT License transparency

---

**🛡️ Security Promise**: Your API keys are treated with the highest level of security. We understand these credentials are valuable and sensitive, and we've designed our system to never compromise their confidentiality.

**🔍 Transparency**: This is an open-source project. Every line of code that handles your data is publicly visible and auditable.
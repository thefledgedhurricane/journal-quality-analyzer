# 🔬 Journal Quality Analyzer

[![Privacy First](https://img.shields.io/badge/Privacy-API%20Keys%20Never%20Stored-green?style=flat-square&logo=shield)](PRIVACY.md)
[![Open Source](https://img.shields.io/badge/License-MIT-blue?style=flat-square&logo=github)](LICENSE)
[![Academic Research](https://img.shields.io/badge/Purpose-Academic%20Research-orange?style=flat-square&logo=graduation-cap)](README.md)

A comprehensive Streamlit application for analyzing academic journal quality using multiple data sources and AI-powered insights.

**🔒 Privacy Guarantee**: Your API keys are never stored, logged, or cached. [Read our Privacy Policy](PRIVACY.md)

## ✨ Features

- **📊 SCImago Journal Rankings**: Browse journals by academic categories
- **🔍 Smart Search**: Find specific journals by name with fuzzy matching
- **✅ Scopus Verification**: Check journal indexing status via Elsevier API
- **⚠️ Predatory Detection**: Identify potentially predatory journals and publishers
- **🤖 AI-Powered Analysis**: Get APC, frequency, and open access info via Google Gemini
- **📁 Export Results**: Download analysis as CSV or XLSX files

## 🚀 Quick Start

### Local Development

1. **Clone and Setup**
   ```bash
   git clone https://github.com/iannaki/journal-quality-analyzer.git
   cd journal-quality-analyzer
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   # Using the startup script (recommended)
   ./start_app.sh
   
   # Or manually
   streamlit run app.py
   ```

3. **Access the App**
   - Open your browser to `http://localhost:8501`

## 🔑 API Keys Setup

### Elsevier/Scopus API Key
1. Visit [Elsevier Developer Portal](https://dev.elsevier.com/)
2. Create an account and apply for API access
3. **Free tier**: 5,000 requests/week
4. Use the key in the app's "Elsevier API Key" field

### Google Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new project
3. Generate an API key
4. **Free tier**: 60 requests/minute
5. Use the key in the app's "Gemini API Key" field

## 🌐 Deployment Options

### 🌟 Streamlit Community Cloud (Recommended - Free)

1. **Prepare Repository**
   - Push your code to GitHub
   - Ensure `requirements.txt` is in the root
   - Add your data files to the `data/` folder

2. **Deploy**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `app.py`
   - Deploy!

3. **Environment Variables** (Optional)
   - Add API keys as secrets in Streamlit Cloud
   - Access via `st.secrets["api_key"]`

### ☁️ Heroku

1. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

2. **Add Buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Set Config Vars**
   ```bash
   heroku config:set SCOPUS_API_KEY=your_key
   heroku config:set GEMINI_API_KEY=your_key
   ```

### 🔧 Railway/Render

1. **Connect Repository**
   - Link your GitHub repo
   - Auto-detects Python app

2. **Environment Variables**
   - Add API keys in dashboard
   - Set `PORT` if required

3. **Deploy**
   - Automatic deployment on git push

### 🏢 Self-Hosted (VPS/Cloud)

1. **Server Setup**
   ```bash
   # Install Python 3.8+
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Clone repository
   git clone <your-repo>
   cd "Journal Finder"
   
   # Install dependencies
   pip3 install -r requirements.txt
   ```

2. **Run with Process Manager**
   ```bash
   # Using PM2
   npm install -g pm2
   pm2 start "streamlit run app.py --server.port 8501" --name journal-analyzer
   
   # Using systemd (create service file)
   sudo systemctl enable journal-analyzer
   sudo systemctl start journal-analyzer
   ```

3. **Reverse Proxy (Nginx)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 📁 Project Structure

```
journal-quality-analyzer/
├── app.py                    # Main Streamlit application
├── start_app.sh             # Startup script with environment activation
├── requirements.txt         # Python dependencies
├── favicon.svg             # Custom favicon
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
├── .gitignore             # Git ignore rules
├── data/                  # Data files
│   ├── scimago_journals.csv
│   ├── predatory_journals.txt
│   └── predatory_publishers.txt
└── exports/               # Generated analysis files
    └── journal_analysis_*.csv/xlsx
```

## 🛠️ Configuration

### Environment Variables
- `SCOPUS_API_KEY`: Your Elsevier API key
- `GEMINI_API_KEY`: Your Google Gemini API key
- `PORT`: Server port (default: 8501)

### Data Sources

**Primary Databases:**
- **[SCImago Journal & Country Rank](https://www.scimagojr.com/)**: Journal rankings, categories, and bibliometric indicators
  - *License*: Freely available for academic and research purposes
  - *Usage*: Non-commercial research and educational use
- **[Predatory Journals Database](http://predatoryjournals.org/)**: Comprehensive list of predatory journals and publishers
  - *Source*: Community-maintained database based on Beall's criteria
  - *Usage*: Public resource for academic integrity

**APIs & Services:**
- **[Elsevier Scopus API](https://dev.elsevier.com/)**: Real-time journal indexing verification
  - *License*: Free tier available for academic research
  - *Rate Limits*: 5,000 requests/week (free tier)
- **[Google Gemini API](https://ai.google.dev/)**: AI-powered journal information extraction
  - *License*: Free tier available
  - *Rate Limits*: 60 requests/minute (free tier)

**Data Usage Disclaimer:**
This tool is developed for **non-commercial academic research purposes only**. All data sources are used in compliance with their respective terms of service and licensing agreements. No revenue is generated from this tool.

## 🤝 Contributing & Collaboration

**We welcome contributions from researchers, developers, and data scientists!** This project thrives on community collaboration.

### 🚀 How to Contribute

#### **Quick Contributions:**
- 🐛 **Report Issues**: Found a bug? [Open an issue](../../issues/new)
- 💡 **Suggest Features**: Have an idea? [Start a discussion](../../discussions)
- 📚 **Improve Documentation**: Fix typos, add examples, or clarify instructions
- 🌍 **Add Data Sources**: Know of additional journal databases or APIs?

#### **Code Contributions:**
1. **Fork the Repository**
   ```bash
   git clone https://github.com/[username]/journal-quality-analyzer.git
   cd journal-quality-analyzer
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Follow existing code style and patterns
   - Add comments for complex logic
   - Update documentation if needed

5. **Test Thoroughly**
   ```bash
   streamlit run app.py  # Test the application
   ```

6. **Submit Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Include screenshots for UI changes

### 🎯 Priority Areas for Contribution

- **🔍 Enhanced Search**: Fuzzy matching, advanced filters
- **📊 Data Visualization**: Charts, graphs, analytics dashboard
- **🌐 API Integration**: Additional journal databases (CrossRef, DOAJ, etc.)
- **🤖 AI Improvements**: Better prompt engineering, additional AI models
- **🔒 Security**: Input validation, API key management
- **⚡ Performance**: Caching, async processing, optimization
- **🌍 Internationalization**: Multi-language support
- **📱 Mobile Responsiveness**: Better mobile UI/UX

### 📧 Contact & Support

**Project Maintainer**: Ihababdelbasset ANNAKI  
**Email**: [i.annaki@ump.ac.ma](mailto:i.annaki@ump.ac.ma) | [iannaki.developer@gmail.com](mailto:iannaki.developer@gmail.com)

**For Collaboration:**
- 💬 **General Questions**: Email or [GitHub Discussions](../../discussions)
- 🐛 **Bug Reports**: [GitHub Issues](../../issues)
- 🚀 **Feature Requests**: [GitHub Issues](../../issues) with "enhancement" label
- 🤝 **Research Partnerships**: Direct email contact

### 🏆 Contributors

We appreciate all contributors! Your name will be added here once you make your first contribution.

<!-- Contributors will be listed here -->

## 📄 License & Copyright

© 2025 Ihababdelbasset ANNAKI. This project is open source and available under the [MIT License](LICENSE).

## 📚 Citation

If you use this tool in your research or academic work, please consider citing it:

### **APA Style:**
```
Annaki, I. (2025). Journal Quality Analyzer: A comprehensive tool for analyzing academic journal quality using multiple data sources and AI-powered insights. GitHub. https://github.com/thefledgedhurricane/journal-quality-analyzer
```

### **BibTeX:**
```bibtex
@software{annaki2025journalanalyzer,
  author = {Annaki, Ihababdelbasset},
  title = {Journal Quality Analyzer: A comprehensive tool for analyzing academic journal quality using multiple data sources and AI-powered insights},
  year = {2025},
  url = {https://github.com/thefledgedhurricane/journal-quality-analyzer},
  note = {GitHub repository}
}
```

### **IEEE Style:**
```
I. Annaki, "Journal Quality Analyzer: A comprehensive tool for analyzing academic journal quality using multiple data sources and AI-powered insights," GitHub, 2025. [Online]. Available: https://github.com/thefledgedhurricane/journal-quality-analyzer
```

**Attribution Note:** While this tool is freely available under the MIT License, we kindly request that users acknowledge its use in their research publications, presentations, or academic work. Your citation helps support continued development and maintenance of this open-source project.

### Legal Disclaimer

This software is provided for **educational and research purposes only**. The tool:
- Uses publicly available data sources in compliance with their terms of service
- Generates no revenue or commercial benefit
- Respects rate limits and usage policies of all APIs
- Is intended to support academic research and journal selection

Users are responsible for ensuring their use complies with applicable terms of service and local regulations.

### 🔒 Privacy Policy & API Key Security

**Your API Keys Are Never Stored or Logged:**

- ✅ **Zero Storage**: API keys are never saved to files, databases, or any persistent storage
- ✅ **No Logging**: Keys are not logged in application logs or error reports
- ✅ **Session-Only**: Keys exist only in browser memory during your active session
- ✅ **Direct API Calls**: Keys are used exclusively for real-time API requests to Elsevier/Google
- ✅ **Open Source Verification**: All code is publicly available for security audit
- ✅ **No Analytics**: No tracking or analytics services that could capture sensitive data

**Technical Implementation:**
- Streamlit's `st.text_input(type="password")` ensures keys are masked in UI
- No caching decorators applied to functions handling API keys
- Keys are passed as function parameters, not stored as global variables
- Application restarts clear all memory, including any temporary key storage

**For Deployment Security:**
- Hosted versions use the same codebase with identical privacy protections
- No server-side logging of user inputs or API responses containing sensitive data
- HTTPS encryption protects data in transit

**🤝 Open for Collaboration**: This tool is actively maintained and welcomes contributions from the research and developer community. Whether you're interested in adding new features, improving existing functionality, or enhancing the user experience, your contributions are highly valued!

### Ways to Contribute:
- 🐛 Report bugs and suggest improvements
- 💡 Propose new features or data sources
- 🔧 Submit code improvements and optimizations
- 📚 Enhance documentation and user guides
- 🌍 Add support for additional languages or regions

## 🆘 Support

If you encounter issues:
1. Check the [Issues](../../issues) page
2. Verify your API keys are valid
3. Ensure all dependencies are installed
4. Check the console for error messages

---

**Made with ❤️ using Streamlit**
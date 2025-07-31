# Contributing to Journal Quality Analyzer

🎉 **Thank you for your interest in contributing!** We welcome contributions from researchers, developers, and data scientists worldwide.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of Streamlit (helpful but not required)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/[your-username]/journal-quality-analyzer.git
   cd journal-quality-analyzer
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test the Application**
   ```bash
   streamlit run app.py
   ```

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use the [issue template](../../issues/new)
- Include steps to reproduce
- Provide error messages and screenshots
- Mention your OS and Python version

### 💡 Feature Requests
- Check [existing issues](../../issues) first
- Describe the problem you're solving
- Provide use cases and examples
- Consider implementation complexity

### 📚 Documentation
- Fix typos and grammar
- Add code examples
- Improve API documentation
- Create tutorials or guides

### 🔧 Code Contributions

#### Priority Areas:
- **Enhanced Search**: Fuzzy matching, advanced filters
- **Data Visualization**: Charts, graphs, analytics
- **API Integration**: CrossRef, DOAJ, additional databases
- **AI Improvements**: Better prompts, additional models
- **Performance**: Caching, async processing
- **Security**: Input validation, API key management
- **Mobile**: Responsive design improvements

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small

### Commit Messages
```
type(scope): brief description

- Use present tense ("Add feature" not "Added feature")
- Types: feat, fix, docs, style, refactor, test, chore
- Keep first line under 50 characters
- Reference issues: "Fixes #123"
```

Examples:
```
feat(search): add fuzzy matching for journal names
fix(api): handle rate limiting for Scopus API
docs(readme): update installation instructions
```

### Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write clean, documented code
   - Follow existing patterns
   - Test your changes thoroughly

3. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   ```

4. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   - Use the PR template
   - Link related issues
   - Add screenshots for UI changes
   - Request review from maintainers

## 🧪 Testing

### Manual Testing
- Test with different journal names
- Verify API integrations work
- Check export functionality
- Test edge cases and error handling

### Before Submitting
- [ ] Code runs without errors
- [ ] New features are documented
- [ ] No sensitive data in commits
- [ ] PR description is clear

## 📧 Getting Help

**Project Maintainer**: Ihababdelbasset ANNAKI  
**Email**: [i.annaki@ump.ac.ma](mailto:i.annaki@ump.ac.ma) | [iannaki.developer@gmail.com](mailto:iannaki.developer@gmail.com)

**Communication Channels**:
- 💬 [GitHub Discussions](../../discussions) - General questions
- 🐛 [GitHub Issues](../../issues) - Bug reports and features
- 📧 Email - Research partnerships and complex questions

## 🏆 Recognition

All contributors will be:
- Added to the Contributors section in README
- Mentioned in release notes for significant contributions
- Credited in academic publications if applicable

## 📜 Code of Conduct

### Our Pledge
We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Expected Behavior
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project maintainer at [i.annaki@ump.ac.ma](mailto:i.annaki@ump.ac.ma) or [iannaki.developer@gmail.com](mailto:iannaki.developer@gmail.com).

---

**Thank you for contributing to Journal Quality Analyzer!** 🚀
#!/bin/bash

# Journal Quality Analyzer Startup Script
# This script activates the research-env environment and launches the Streamlit app

echo "🔬 Activating research-env environment..."

# Check if pyenv is available
if command -v pyenv &> /dev/null; then
    # Activate the research-env environment
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    
    # Switch to research-env
    pyenv activate research-env
    
    echo "✅ Environment activated: $(pyenv version)"
else
    echo "⚠️  pyenv not found, using system Python"
fi

echo "🚀 Starting Journal Quality Analyzer..."
echo "📊 App will be available at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

# Launch the Streamlit app
streamlit run app.py --server.port 8501
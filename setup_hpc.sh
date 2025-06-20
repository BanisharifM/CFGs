#!/bin/bash
echo "🚀 Setting up LLM-based CFG Generation Pipeline for HPC Environment..."

# Check if we're in a conda environment
if [[ -z "${CONDA_DEFAULT_ENV}" ]]; then
    echo "⚠️  Warning: No conda environment detected"
    echo "   Please activate your environment first: conda activate cfg_env"
    echo "   Then run this script again"
    exit 1
else
    echo "✅ Conda environment detected: $CONDA_DEFAULT_ENV"
fi

# Create directories
echo "📁 Creating output directory..."
mkdir -p output

# Install Python dependencies using pip (no sudo needed)
echo "🐍 Installing Python dependencies with pip..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Python dependencies"
    echo "   Try: pip install --user -r requirements.txt"
    exit 1
fi

# Clone BOTS repository
echo "📥 Cloning BOTS repository..."
if [ ! -d "bots" ]; then
    git clone https://github.com/bsc-pm/bots.git
    if [ $? -eq 0 ]; then
        echo "✅ BOTS repository cloned successfully"
    else
        echo "❌ Failed to clone BOTS repository"
        echo "   Check your internet connection and git access"
        exit 1
    fi
else
    echo "ℹ️  BOTS repository already exists"
fi

# Check installation
echo "🔍 Verifying installation..."
python --version
git --version

# Check if required Python packages are available
echo "🔍 Checking Python packages..."
python -c "import matplotlib, networkx, numpy; print('✅ Core packages available')" 2>/dev/null || echo "⚠️  Some packages may not be installed correctly"

# Check for graphviz (optional)
if command -v dot &> /dev/null; then
    echo "✅ Graphviz found: $(dot -V 2>&1 | head -1)"
elif python -c "import graphviz; print('✅ Python graphviz package available')" 2>/dev/null; then
    echo "✅ Python graphviz package available (system graphviz not needed)"
else
    echo "⚠️  Graphviz not found - PNG generation may not work"
    echo "   You can still generate DOT files and convert them later"
    echo "   Or install with: pip install graphviz"
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. cd scripts"
echo "2. python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_for/sparselu.c"
echo "3. Check results in ../output/"
echo ""
echo "💡 Your conda environment: $CONDA_DEFAULT_ENV"
echo "💡 Optional: Set OpenAI API key for better results:"
echo "   export OPENAI_API_KEY=your_api_key_here"


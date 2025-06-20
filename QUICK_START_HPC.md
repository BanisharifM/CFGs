# Quick Start Guide for HPC Environment

## 🚀 Setup Instructions

### 1. Activate Your Conda Environment
```bash
conda activate cfg_env
```

### 2. Extract and Setup
```bash
tar -xzf openmp-cfg-project-hpc.tar.gz
cd openmp-cfg-project-hpc
chmod +x setup_hpc.sh
./setup_hpc.sh
```

### 3. Test the Pipeline
```bash
cd scripts
python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_for/sparselu.c
```

### 4. Check Results
```bash
ls ../output/
```

## 🔧 Key Differences from Standard Version

- ✅ **No sudo required** - Uses pip install only
- ✅ **Conda environment detection** - Validates environment
- ✅ **HPC-friendly graphics** - Python graphviz package
- ✅ **Graceful fallbacks** - Works without system graphviz

## 📊 What You'll Get

```
output/
├── sparselu_cfg.dot     # Machine-readable CFG
├── sparselu_cfg.png     # Visual diagram (if possible)
└── ...
```

## 🛠️ Troubleshooting

**"No conda environment detected"**
```bash
conda activate cfg_env
```

**"Permission denied"**
```bash
chmod +x setup_hpc.sh scripts/*.py
```

**"Package installation failed"**
```bash
pip install --user -r requirements.txt
```

Ready for HPC! 🚀


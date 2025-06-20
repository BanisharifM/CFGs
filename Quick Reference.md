# Quick Reference: Running Different Benchmarks

## 🎯 All Available BOTS Benchmarks

### 1. **SparseLU** (Sparse Matrix LU Factorization)
```bash
# For-based version
python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_for/sparselu.c

# Single-task version  
python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_single/sparselu.c
```
**OpenMP Features**: Nested loops, untied tasks, single regions, implicit barriers

### 2. **FFT** (Fast Fourier Transform)
```bash
python cfg_generator.py --input ../bots/omp-tasks/fft/fft.c
```
**OpenMP Features**: Complex task dependencies, recursive parallelism, taskwait

### 3. **Strassen** (Matrix Multiplication)
```bash
python cfg_generator.py --input ../bots/omp-tasks/strassen/strassen.c
```
**OpenMP Features**: Divide-and-conquer tasks, recursive structure

### 4. **N-Queens** (Backtracking Algorithm)
```bash
python cfg_generator.py --input ../bots/omp-tasks/nqueens/nqueens.c
```
**OpenMP Features**: Dynamic task creation, load balancing

### 5. **Health** (Discrete Event Simulation)
```bash
python cfg_generator.py --input ../bots/omp-tasks/health/health.c
```
**OpenMP Features**: Irregular parallelism, dynamic scheduling

### 6. **Alignment** (Protein Sequence Alignment)
```bash
# For-based version
python cfg_generator.py --input ../bots/omp-tasks/alignment/alignment_for/alignment.c

# Single-task version
python cfg_generator.py --input ../bots/omp-tasks/alignment/alignment_single/alignment.c
```
**OpenMP Features**: Nested parallel loops, data dependencies

### 7. **Floorplan** (VLSI Floorplanning)
```bash
python cfg_generator.py --input ../bots/omp-tasks/floorplan/floorplan.c
```
**OpenMP Features**: Branch-and-bound parallelism, pruning

### 8. **Sort** (Merge Sort)
```bash
python cfg_generator.py --input ../bots/omp-tasks/sort/sort.c
```
**OpenMP Features**: Recursive divide-and-conquer, task synchronization

### 9. **Fibonacci** (Recursive Fibonacci)
```bash
python cfg_generator.py --input ../bots/omp-tasks/fib/fib.c
```
**OpenMP Features**: Simple recursive tasks, basic parallelism

### 10. **UTS** (Unbalanced Tree Search)
```bash
python cfg_generator.py --input ../bots/omp-tasks/uts/uts.c
```
**OpenMP Features**: Irregular tree traversal, dynamic load balancing

### 11. **Knapsack** (0/1 Knapsack Problem)
```bash
python cfg_generator.py --input ../bots/omp-tasks/knapsack/knapsack.c
```
**OpenMP Features**: Branch-and-bound, dynamic programming

### 12. **ConCom** (Connected Components)
```bash
python cfg_generator.py --input ../bots/omp-tasks/concom/concom.c
```
**OpenMP Features**: Graph algorithms, irregular data access

## 🔧 Command Line Options

### Basic Usage
```bash
python cfg_generator.py --input <file.c>
```

### With Custom Hardware
```bash
python cfg_generator.py --input <file.c> --cores 32 --arch x86_64
```

### Custom Output Directory
```bash
python cfg_generator.py --input <file.c> --output /path/to/results/
```

### All Options
```bash
python cfg_generator.py \
    --input ../bots/omp-tasks/sparselu/sparselu_for/sparselu.c \
    --output ../results/ \
    --cores 16 \
    --arch x86_64 \
    --api-key YOUR_OPENAI_KEY
```

## 📊 Expected Output for Each Benchmark

### SparseLU Output
```
sparselu_cfg.dot    # 13 basic blocks, 3 task types, nested loops
sparselu_cfg.png    # Visual with parallel regions and task flows
```

### FFT Output  
```
fft_cfg.dot         # Complex task dependencies, recursive structure
fft_cfg.png         # Shows divide-and-conquer pattern
```

### N-Queens Output
```
nqueens_cfg.dot     # Dynamic task creation, backtracking
nqueens_cfg.png     # Branch-and-bound visualization
```

## 🚀 Batch Processing

### Process All Benchmarks
```bash
python batch_process.py
```

### Process Specific Subset
Edit `batch_process.py` to filter benchmarks:
```python
# Only process specific benchmarks
target_benchmarks = ['sparselu', 'fft', 'nqueens', 'strassen']
if any(target in file_path for target in target_benchmarks):
    # Process this file
```

## 🎯 Research-Specific Usage

### Compare OpenMP Variants
```bash
# Compare different implementations of same algorithm
python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_for/sparselu.c --output results/sparselu_for/
python cfg_generator.py --input ../bots/omp-tasks/sparselu/sparselu_single/sparselu.c --output results/sparselu_single/

# Compare alignment variants
python cfg_generator.py --input ../bots/omp-tasks/alignment/alignment_for/alignment.c --output results/alignment_for/
python cfg_generator.py --input ../bots/omp-tasks/alignment/alignment_single/alignment.c --output results/alignment_single/
```

### Hardware-Specific Analysis
```bash
# Generate CFGs for different target architectures
python cfg_generator.py --input benchmark.c --cores 4 --arch arm64 --output results/embedded/
python cfg_generator.py --input benchmark.c --cores 16 --arch x86_64 --output results/workstation/
python cfg_generator.py --input benchmark.c --cores 32 --arch x86_64 --output results/server/
```

### Performance Study
```bash
# Generate CFGs for performance comparison
for benchmark in sparselu fft nqueens strassen health; do
    python cfg_generator.py --input ../bots/omp-tasks/$benchmark/$benchmark.c --output results/$benchmark/
done
```

## 📈 Understanding Benchmark Characteristics

### **Compute-Intensive**
- SparseLU, Strassen, FFT
- Dense mathematical operations
- Regular parallelism patterns

### **Search-Based**
- N-Queens, UTS, Knapsack
- Irregular parallelism
- Dynamic load balancing needed

### **Graph/Tree Algorithms**
- ConCom, UTS, Floorplan
- Pointer-chasing patterns
- Memory-bound operations

### **Simulation**
- Health, Alignment
- Event-driven parallelism
- Complex dependencies

This gives you complete control over which benchmarks to analyze and how to customize the analysis for your research needs!


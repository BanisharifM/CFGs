#!/usr/bin/env python3
"""
Batch process all BOTS benchmarks
"""

import os
import subprocess
from pathlib import Path

def find_openmp_files(bots_path):
    """Find all OpenMP C files in BOTS repository"""
    openmp_files = []
    
    if not os.path.exists(bots_path):
        print(f"❌ BOTS repository not found at: {bots_path}")
        print("   Run setup.sh first to clone the repository")
        return []
    
    # Search in omp-tasks directory
    omp_tasks_path = os.path.join(bots_path, "omp-tasks")
    
    if not os.path.exists(omp_tasks_path):
        print(f"❌ omp-tasks directory not found in: {bots_path}")
        return []
    
    for root, dirs, files in os.walk(omp_tasks_path):
        for file in files:
            if file.endswith('.c'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if '#pragma omp' in content:
                            openmp_files.append(file_path)
                except Exception as e:
                    print(f"⚠️  Could not read {file_path}: {e}")
                    continue
    
    return openmp_files

def main():
    bots_path = "../bots"
    output_path = "../output"
    
    print("🔍 Searching for OpenMP files in BOTS repository...")
    openmp_files = find_openmp_files(bots_path)
    
    if not openmp_files:
        print("❌ No OpenMP files found!")
        print("   Make sure the BOTS repository is cloned correctly")
        return 1
    
    print(f"✅ Found {len(openmp_files)} OpenMP files:")
    for i, file in enumerate(openmp_files, 1):
        rel_path = os.path.relpath(file, bots_path)
        print(f"   {i:2d}. {rel_path}")
    
    print(f"\n🚀 Processing all files...")
    
    success_count = 0
    fail_count = 0
    
    # Process each file
    for i, file_path in enumerate(openmp_files, 1):
        rel_path = os.path.relpath(file_path, bots_path)
        print(f"\n[{i}/{len(openmp_files)}] Processing: {rel_path}")
        
        try:
            cmd = [
                'python3', 'cfg_generator.py',
                '--input', file_path,
                '--output', output_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Success: {rel_path}")
            success_count += 1
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed: {rel_path}")
            print(f"   Error: {e}")
            if e.stderr:
                print(f"   Details: {e.stderr.strip()}")
            fail_count += 1
        except Exception as e:
            print(f"❌ Unexpected error for {rel_path}: {e}")
            fail_count += 1
    
    print(f"\n📊 Batch processing completed!")
    print(f"   ✅ Successful: {success_count}")
    print(f"   ❌ Failed: {fail_count}")
    print(f"   📁 Results in: {output_path}")
    
    if success_count > 0:
        print(f"\n🎉 Generated CFGs for {success_count} benchmarks!")
        return 0
    else:
        print(f"\n😞 No CFGs were generated successfully")
        return 1

if __name__ == "__main__":
    exit(main())


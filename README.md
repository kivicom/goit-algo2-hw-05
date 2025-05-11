# Big Data Algorithms Homework

This repository contains solutions for two tasks related to big data algorithms.

## Task 1: Bloom Filter for Password Uniqueness
- Implements `BloomFilter` class and `check_password_uniqueness` function to check password uniqueness efficiently.
- Includes example usage with test cases.

## Task 2: HyperLogLog vs Exact Counting
- Compares exact counting of unique IP addresses (using `set`) with HyperLogLog approximation.
- Processes log file data and displays performance results in a table.

## Files
- `bloom_filter_passwords.py`: Solution for Task 1.
- `compare_unique_ips.py`: Solution for Task 2.
- `requirements.txt`: Dependency list for the project.

## Requirements
- Python 3.x
- Libraries:
  - `hashlib` (built-in)
  - `hyperloglog` (>= 0.1.0)
  - `tabulate` (>= 0.9.0)
- Install dependencies using the provided `requirements.txt`:
  ```bash
  pip3 install -r requirements.txt
  ```

## Usage
Run each script to test:
```bash
python3 bloom_filter_passwords.py
python3 compare_unique_ips.py
```

## Notes
- For Task 2, ensure `lms-stage-access.log` exists or use the built-in test dataset.
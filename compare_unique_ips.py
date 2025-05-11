"""
Module for comparing exact and approximate counting of unique IP addresses using set and HyperLogLog.
"""

import time
import re
from hyperloglog import HyperLogLog
from tabulate import tabulate

def load_ip_addresses(filename):
    """
    Load IP addresses from a log file, ignoring invalid lines.
    If file is not found, use a small test dataset.

    Args:
        filename (str): Path to the log file.

    Returns:
        list: List of extracted IP addresses.
    """
    ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    ip_addresses = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                match = ip_pattern.search(line)
                if match:
                    ip_addresses.append(match.group())
    except FileNotFoundError:
        print(f"Warning: File {filename} not found. Using test dataset.")
        test_data = [
            "192.168.1.1 - - [11/May/2025:12:00:00] GET /index.html",
            "192.168.1.2 - - [11/May/2025:12:00:01] GET /page1.html",
            "192.168.1.1 - - [11/May/2025:12:00:02] POST /submit.html",
            "192.168.1.3 - - [11/May/2025:12:00:03] GET /page2.html"
        ]
        for line in test_data:
            match = ip_pattern.search(line)
            if match:
                ip_addresses.append(match.group())
    except IOError as e:
        print(f"Error reading file: {e}")
        return []

    return ip_addresses

def exact_count_unique(ips):
    """
    Perform exact counting of unique IP addresses using a set.

    Args:
        ips (list): List of IP addresses.

    Returns:
        int: Number of unique IP addresses.
    """
    return len(set(ips))

def hyperloglog_count_unique(ips, error_rate=0.01):
    """
    Perform approximate counting of unique IP addresses using HyperLogLog.

    Args:
        ips (list): List of IP addresses.
        error_rate (float): Acceptable error rate for HyperLogLog (default: 0.01).

    Returns:
        float: Approximate number of unique IP addresses.
    """
    hll = HyperLogLog(error_rate)
    for ip in ips:
        hll.add(ip)
    return hll.card()

def compare_methods(filename):
    """
    Compare exact and HyperLogLog methods for counting unique IP addresses.

    Args:
        filename (str): Path to the log file.

    Prints a table comparing the results and execution times of both methods.
    """
    ip_addresses = load_ip_addresses(filename)
    if not ip_addresses:
        return

    # Exact counting
    start_time = time.time()
    exact_count = exact_count_unique(ip_addresses)
    exact_time = time.time() - start_time

    # HyperLogLog counting
    start_time = time.time()
    hll_count = hyperloglog_count_unique(ip_addresses)
    hll_time = time.time() - start_time

    # Display results in a table
    table = [
        ["Унікальні елементи", exact_count, hll_count],
        ["Час виконання (сек.)", f"{exact_time:.2f}", f"{hll_time:.2f}"]
    ]
    print("Результати порівняння:")
    print(tabulate(table, headers=["", "Точний підрахунок", "HyperLogLog"], tablefmt="pretty"))

if __name__ == "__main__":
    # Run comparison on the log file
    compare_methods("lms-stage-access.log")
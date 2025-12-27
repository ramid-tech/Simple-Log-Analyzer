# Simple Log Analyzer

Simple Log Analyzer is a small Python project created to practice core programming concepts by working with log-style data. The script goes through a list of log entries, prints each entry with its position in the list, and keeps track of specific conditions such as errors.

This project is intentionally simple and focuses on building a solid foundation in Python while working with examples that reflect real-world IT, networking, and cybersecurity tasks.

---

## Objective

The objective of this project is to strengthen Python fundamentals by applying them to a practical scenario. Instead of working with abstract examples, this project uses log-style data to practice iteration, indexing, and basic analysis techniques that are commonly used when reviewing system or application logs.

---

## How It Works

The program processes a list of log entries and performs the following actions:
- Iterates through each log entry
- Prints the log entry along with its index number
- Tracks and counts error-related entries using a counter
- Displays structured output that is easy to read and understand

All processing is done locally in memory to focus on logic rather than external dependencies.

---

## Steps

1. A list of log entries is defined in the script  
2. A counter variable is initialized to track errors  
3. A loop iterates through the list using `enumerate()`  
4. Each log entry is printed along with its position in the list  
5. Conditional logic checks for error-related keywords  
6. The error counter is incremented when a match is found  
7. The final output reflects both the logs and tracked results  

---

## Skills Learned

- Python list handling and indexing  
- Looping through data using `for` loops  
- Using `enumerate()` to access index positions  
- Implementing counters and conditional logic  
- Writing readable and organized Python code  
- Thinking through basic log-analysis workflows  

---

## Tools Used

- **Python 3**
- Code editor (VS Code)
- Command line / terminal

---

## Why This Project Matters

Log analysis is a common task in IT operations, networking, and cybersecurity. While this project is simple, the concepts demonstrated here scale directly into more advanced tools that work with real log files, monitoring systems, and security alerts.

This project serves as a foundation that can be expanded into file-based log parsing, filtering by severity, or basic automation scripts.

---

## Future Improvements

Possible next steps for this project include:
- Reading logs from external files
- Supporting different log formats
- Filtering logs by severity level
- Generating summary reports
- Expanding error detection logic

---

## Author

Created as part of ongoing learning in Python, networking, and cybersecurity fundamentals, with a focus on building practical, real-world skills.

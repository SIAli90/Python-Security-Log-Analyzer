# Python Security Log Analyzer

A simple Python project that analyses authentication logs to detect suspicious activity such as brute-force login attempts and successful logins after repeated failures.

## Features
- Parses authentication log data
- Counts failed login attempts per IP
- Detects IPs that exceed a brute-force threshold
- Flags successful logins that occurred after previous failures

## Files
- `log_analyzer.py` - main Python script
- `auth.log` - sample authentication log data

## How to Run
```bash
python log_analyzer.py

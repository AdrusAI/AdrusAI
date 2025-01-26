ADRUS Troubleshooting Guide
If you encounter any issues while using ADRUS, this guide will help you troubleshoot common problems and their solutions.

General Checklist
Before diving into specific issues, ensure the following:

You are using Python 3.8 or later.
You have activated your virtual environment (if applicable).
All dependencies are installed via pip install -r requirements.txt.
Your firewall or antivirus isn't blocking the application.
Common Issues and Solutions
Issue 1: ModuleNotFoundError
Error Message:
ModuleNotFoundError: No module named 'flask'

Solution:

Ensure dependencies are installed by running:
pip install -r requirements.txt
Activate your virtual environment before running the code:
source venv/bin/activate (On macOS/Linux)
venv\Scripts\activate (On Windows)
Issue 2: OSError: [Errno 98] Address already in use
Cause:
The dashboard service is already running on port 5000.

Solution:

Identify and kill the process using port 5000:
lsof -ti:5000 | xargs kill -9 (macOS/Linux)
netstat -ano | findstr :5000 (Windows - find the PID and use taskkill /PID <pid> /F)

Restart the dashboard:
python src/dashboard/dashboard_ui.py

Issue 3: PermissionError: [Errno 13] Permission denied
Cause:
Insufficient privileges to access or modify files.

Solution:

Try running the command with administrator privileges:
sudo python src/dashboard/dashboard_ui.py (Linux/macOS)
Ensure that the project directory has the right permissions:
chmod -R 755 adrus/
﻿
Issue 4: ImportError: Cannot Import Module
Error Message:
ImportError: cannot import name 'AgentMonitor' from 'src.monitoring'

Solution:

Ensure you are running the script from the project root directory:
cd /path/to/adrus
python examples/tracking_demo.py
Check that the Python path includes the project directory:
export PYTHONPATH=$PYTHONPATH:/path/to/adrus/src
Issue 5: Virtual Environment Not Found
Error Message:
command not found: venv

Solution:

Ensure virtualenv is installed:
pip install virtualenv
Create and activate the virtual environment again:
python -m venv venv
source venv/bin/activate (On macOS/Linux)
venv\Scripts\activate (On Windows)
Issue 6: Dashboard Not Loading in Browser
Cause:
The dashboard may not have started correctly.

Solution:

Check if the Flask server is running:
ps aux | grep flask (macOS/Linux)
tasklist | findstr "python" (Windows)
If it's not running, restart with:
python src/dashboard/dashboard_ui.py
Try clearing your browser cache or using an incognito window.
Issue 7: High Memory Usage
Cause:
Large data processing can consume excessive memory.

Solution:

Optimize monitoring intervals in config.json:
json
Copy
Edit
{
    "monitoring_interval": 10, 
    "alert_threshold": 0.9
}
Run ADRUS with resource limits:
ulimit -m 500000 (Limit memory usage on Linux/macOS)
Issue 8: Tests Failing
Error Message:
AssertionError: Expected output does not match actual

Solution:

Run the test suite and capture detailed logs:
pytest -v --capture=tee-sys tests/
Ensure all dependencies are installed correctly.
Issue 9: API Not Responding
Cause:
The API service may not be running properly.

Solution:

Verify Flask is running by checking:
curl http://127.0.0.1:5000/dashboard
Restart the API server and check logs for errors:
python src/dashboard/dashboard_ui.py

Issue 10: Git Issues When Cloning
Error Message:
fatal: repository not found

Solution:

Make sure the repository URL is correct:
git clone https://github.com/yourusername/adrus.git
Check your internet connection and GitHub access rights.
Debugging Tips
If none of the above solutions work, follow these debugging tips:

Check for syntax errors in your Python code:
python -m py_compile src/*/.py

View the last log entries:
tail -n 50 logs/adrus.log

Restart your system and try running ADRUS again.

Contact Support
If you're still facing issues, open a GitHub issue with the following details:

Operating System (Windows/macOS/Linux)
Python version (python --version)
Steps to reproduce the issue
Relevant error messages

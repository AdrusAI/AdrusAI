ADRUS Installation Guide
Welcome to ADRUS – an AI-driven agent tracking and management platform. Follow this guide to install and set up ADRUS on your local environment.

Prerequisites
Before installing ADRUS, ensure you have the following requirements installed:

Python (>= 3.8) – https://www.python.org/downloads/
Git – https://git-scm.com/downloads
Virtual Environment (Recommended)

Step 1: Clone the Repository
Start by cloning the ADRUS repository from GitHub:
Python.org
Download Python
The official home of the Python Programming Language
Image
Step 2: Set Up a Virtual Environment (Recommended)
It is highly recommended to create a virtual environment to manage dependencies effectively.

On macOS/Linux:
Once activated, your terminal should show the virtual environment name, indicating that it's active.

Step 3: Install Dependencies
After activating your virtual environment, install all required dependencies using:
Step 4: Verify Installation
To verify if the installation was successful, run the following command:
If no errors are shown, ADRUS is successfully installed.

Step 5: Running ADRUS Locally
To start the ADRUS dashboard and monitor AI agents in real-time, run:
Step 6: Testing the Setup
Run the test suite to confirm everything is working correctly:
Expected output should indicate that all tests have passed.

Step 7: Configuration
ADRUS uses a configuration file to customize tracking settings. Modify the config.json file to update parameters such as:
Common Installation Issues
| Error                      | Solution                                             |
|----------------------------|-----------------------------------------------------|
| ModuleNotFoundError       | Ensure you've activated the virtual environment.    |
| Permission Denied         | Run with sudo on Linux/macOS.                      |
| Port 5000 already in use   | Kill the running process using lsof -ti:5000       |

For more troubleshooting tips, check the [Troubleshooting Guide](troubleshooting.md).

Next Steps
Once installed, check out the [Usage Guide](usage_guide.md) to start using ADRUS for AI agent tracking and behavior analysis.

Uninstallation
If you need to uninstall ADRUS, simply remove the directory and the virtual environment:
﻿
eosphoreus
eosphoreus

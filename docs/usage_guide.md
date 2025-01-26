ADRUS Usage Guide
This guide will help you get started with ADRUS and utilize its features effectively.

Initializing ADRUS
To start monitoring an AI agent, import the necessary module and create an instance of the AgentMonitor class.

Example:
from src.monitoring.agent_monitor import AgentMonitor

monitor = AgentMonitor(agent_id="123") monitor.track_activity("Training Model", status="In Progress") monitor.log_metric("CPU Usage", 70)

Running the Dashboard
ADRUS provides a web-based dashboard to visualize real-time data from your AI agents.

To start the dashboard, run the following command:

python src/dashboard/dashboard_ui.py

Once started, open your web browser and navigate to:

http://127.0.0.1:5000/dashboard

You should see a visual representation of your AI agent's performance, including logs and anomaly alerts.

Detecting Anomalies
ADRUS can automatically detect anomalies in your AI agent's performance. Use the AnomalyDetector class to analyze data.

Example:

from src.anomaly_detection.anomaly_detector import AnomalyDetector

detector = AnomalyDetector(threshold=0.85) data_points = [0.5, 0.7, 1.1, 0.9] anomalies = detector.detect(data_points)

if anomalies: print("Potential anomalies detected:", anomalies)

Explanation:

threshold: A value above which data points are considered anomalies.
detect: Identifies data points exceeding the threshold.
Generating Reports
To analyze agent behavior, use the BehaviorAnalyzer class to generate insights and detect inefficiencies.

Example:

from src.behavior_analysis.behavior_analyzer import BehaviorAnalyzer

analyzer = BehaviorAnalyzer(agent_id="123") report = analyzer.generate_report() print("Behavior Report:", report)

Explanation:

generate_report: Provides a summary of agent performance and identifies potential optimization areas.
Custom Configuration
ADRUS allows customization of tracking parameters via a config.json file located in the root directory.

Example content of config.json:

{ "monitoring_interval": 5, "alert_threshold": 0.85, "log_level": "INFO" }

Explanation:

monitoring_interval: Defines the frequency of monitoring checks (in seconds).
alert_threshold: Adjusts the threshold for anomaly detection.
log_level: Controls the verbosity of logs.
Testing ADRUS
Before deploying ADRUS, it's recommended to run the test suite to ensure all components are functioning correctly.

Run tests using:

pytest tests/

Expected output should indicate that all tests have passed successfully.

Logging and Monitoring
ADRUS logs agent activity, system metrics, and anomalies. Logs can be accessed in the logs/ directory.

To view recent logs:

tail -n 50 logs/adrus.log

You can adjust logging verbosity by modifying the config.json file.

Deployment Considerations
For deploying ADRUS in a production environment, consider the following:

Use a process manager like gunicorn to run the dashboard:
gunicorn -w 4 -b 0.0.0.0:5000 src.dashboard.dashboard_ui:app

Enable logging and monitoring to an external service for better tracking.
Set up periodic backups for logged data.
Error Handling
To handle errors gracefully, wrap your ADRUS calls in try-except blocks:

try: monitor.track_activity("Invalid Task", status="Unknown") except ValueError as e: print(f"Error: {e}")

This will prevent unexpected crashes and provide meaningful error messages.

Advanced Usage
For users looking to integrate ADRUS with other applications, the API can be accessed via RESTful endpoints.

Example API request using requests library:

import requests

response = requests.get("http://127.0.0.1:5000/dashboard") print(response.json())
Next Steps
Now that you have a basic understanding of ADRUS, you can:

Explore the API Reference for detailed function documentation.
Read the Troubleshooting Guide for common issues.
Contribute to ADRUS by following our Contribution Guidelines.
If you have any questions, visit our GitHub page or open an issue.

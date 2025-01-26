ADRUS API Reference
Welcome to the ADRUS API documentation. This guide provides details about the available modules, their usage, and how you can integrate ADRUS into your workflow.

Modules Overview
ADRUS consists of the following core modules:

[Monitoring Module](#monitoring-module)
[Behavior Analysis Module](#behavior-analysis-module)
[Anomaly Detection Module](#anomaly-detection-module)
[Dashboard API](#dashboard-api)

---

Monitoring Module
Import
Class: AgentMonitor
The AgentMonitor class provides functionality to track and monitor AI agent activities in real time.

#### Initialization
Parameters:
agent_id (str): Unique identifier for the AI agent.

---

Methods
#### track_activity(description: str, status: str = "Pending")
Logs an activity for the agent.

Usage:
Parameters:
description (str): Description of the activity.
status (str): Status of the task (default: "Pending").

---

#### log_metric(metric_name: str, value: float)
Logs a performance metric for the agent.

Usage:
Parameters:
metric_name (str): Name of the metric.
value (float): Value of the metric.

---

#### detect_anomaly() -> bool
Checks for anomalies in the agent’s activities.

Usage:
Returns:
bool: Returns True if an anomaly is detected, otherwise False.

---

Behavior Analysis Module
Import
Class: BehaviorAnalyzer
The BehaviorAnalyzer class provides methods to analyze AI agent behavior patterns and detect inefficiencies.

#### Initialization
Parameters:
agent_id (str): Unique identifier for the AI agent.

---

Methods
#### analyze_behavior(logs: list) -> dict
Analyzes agent behavior logs to detect inefficiencies.

Usage:

# agent_monitor.py
 
import time
 
class AgentMonitor:
    """
    A class to monitor AI agent activities and performance metrics.
    """
 
    def __init__(self, agent_id):
        """
        Initializes the monitoring system for a specific AI agent.
 
        :param agent_id: str, unique identifier for the AI agent.
        """
        self.agent_id = agent_id
        self.activities = []
        self.metrics = {}
 
    def track_activity(self, description, status="Pending"):
        """
        Tracks an activity performed by the AI agent.
 
        :param description: str, description of the activity.
        :param status: str, status of the activity (default is 'Pending').
        """
        activity = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "status": status
        }
        self.activities.append(activity)
        print(f"Activity Logged: {activity}")
 
    def log_metric(self, metric_name, value):
        """
        Logs performance metrics such as CPU and memory usage.
 
        :param metric_name: str, name of the metric (e.g., 'CPU Usage').
        :param value: float, value of the metric.
        """
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
 
        self.metrics[metric_name].append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "value": value
        })
        print(f"Metric Recorded: {metric_name} - {value}")
 
    def detect_anomaly(self, threshold=80):
        """
        Detects anomalies based on the threshold for recorded metrics.
 
        :param threshold: float, threshold value to detect anomalies (default is 80).
        :return: bool, True if anomalies detected, False otherwise.
        """
        for metric, values in self.metrics.items():
            for entry in values:
                if entry["value"] > threshold:
                    print(f"Anomaly detected in {metric}: {entry['value']} at {entry['timestamp']}")
                    return True
        return False
 
    def generate_report(self):
        """
        Generates a report of the agent's activities and performance metrics.
 
        :return: dict, summarized report.
        """
        report = {
            "agent_id": self.agent_id,
            "total_activities": len(self.activities),
            "metrics_logged": {metric: len(values) for metric, values in self.metrics.items()}
        }
        return report

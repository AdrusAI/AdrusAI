from src.monitoring.agent_monitor import AgentMonitor

Initialize the agent monitor with a unique agent ID
monitor = AgentMonitor(agent_id="AI-Agent-001")

Track various activities of the AI agent
monitor.track_activity("Data preprocessing started", status="In Progress") monitor.track_activity("Model training initiated", status="Pending") monitor.track_activity("Evaluation phase", status="Completed")

Log system performance metrics
monitor.log_metric("CPU Usage", 65.4) monitor.log_metric("Memory Usage", 2048) monitor.log_metric("Disk I/O", 120)

Check for anomalies in the agent's performance
if monitor.detect_anomaly(): print("Warning: Anomalous behavior detected in the AI agent.") else: print("All activities and metrics are within normal parameters.")

Display the tracked activities and metrics
print("Tracked Activities:", monitor.activities)

# test_monitoring.py
 
import unittest
from src.monitoring.agent_monitor import AgentMonitor
 
class TestAgentMonitor(unittest.TestCase):
    """
    Unit tests for the AgentMonitor class.
    """
 
    def setUp(self):
        """
        Setup function to initialize the AgentMonitor instance.
        """
        self.monitor = AgentMonitor(agent_id="TestAgent001")
 
    def test_track_activity_valid(self):
        """
        Test tracking a valid activity.
        """
        self.monitor.track_activity("Model training", status="In Progress")
        self.assertEqual(len(self.monitor.activities), 1)
        self.assertEqual(self.monitor.activities[0]["description"], "Model training")
        self.assertEqual(self.monitor.activities[0]["status"], "In Progress")
 
    def test_track_multiple_activities(self):
        """
        Test tracking multiple activities.
        """
        self.monitor.track_activity("Data preprocessing", status="Completed")
        self.monitor.track_activity("Model evaluation", status="Pending")
 
        self.assertEqual(len(self.monitor.activities), 2)
        self.assertEqual(self.monitor.activities[1]["description"], "Model evaluation")
        self.assertEqual(self.monitor.activities[1]["status"], "Pending")
 
    def test_log_metric_valid(self):
        """
        Test logging valid performance metrics.
        """
        self.monitor.log_metric("CPU Usage", 75.5)
        self.monitor.log_metric("Memory Usage", 2048)
 
        self.assertIn("CPU Usage", self.monitor.metrics)
        self.assertEqual(self.monitor.metrics["CPU Usage"][0]["value"], 75.5)
        self.assertIn("Memory Usage", self.monitor.metrics)
        self.assertEqual(self.monitor.metrics["Memory Usage"][0]["value"], 2048)
 
    def test_detect_anomaly_no_anomaly(self):
        """
        Test anomaly detection with normal metric values.
        """
        self.monitor.log_metric("CPU Usage", 65)
        self.monitor.log_metric("Memory Usage", 1024)
 
        self.assertFalse(self.monitor.detect_anomaly(threshold=80))
 
    def test_detect_anomaly_with_high_values(self):
        """
        Test anomaly detection with values exceeding threshold.
        """
        self.monitor.log_metric("CPU Usage", 90)
        self.monitor.log_metric("Memory Usage", 3000)
 
        self.assertTrue(self.monitor.detect_anomaly(threshold=80))
 
    def test_generate_report(self):
        """
        Test generating a report of monitored data.
        """
        self.monitor.track_activity("Data analysis", status="Completed")
        self.monitor.log_metric("Disk I/O", 50)
 
        report = self.monitor.generate_report()
 
        self.assertEqual(report["agent_id"], "TestAgent001")
        self.assertEqual(report["total_activities"], 1)
        self.assertIn("Disk I/O", report["metrics_logged"])
        self.assertEqual(report["metrics_logged"]["Disk I/O"], 1)
 
    def tearDown(self):
        """
        Cleanup function after each test.
        """
        del self.monitor
 
if __name__ == "__main__":
    unittest.main()

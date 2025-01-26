# test_full_system.py
 
import unittest
from src.monitoring.agent_monitor import AgentMonitor
from src.behavior_analysis.behavior_analyzer import BehaviorAnalyzer
from src.anomaly_detection.anomaly_detector import AnomalyDetector
 
class TestFullSystem(unittest.TestCase):
    """
    Integration tests to validate the full functionality of the ADRUS system.
    """
 
    def setUp(self):
        """
        Setup before each test case.
        Initializes required components for testing.
        """
        self.agent_id = "TestAgent123"
        self.monitor = AgentMonitor(self.agent_id)
        self.analyzer = BehaviorAnalyzer(self.agent_id)
        self.detector = AnomalyDetector(threshold=0.8)
 
    def test_tracking_and_metrics_logging(self):
        """
        Test whether agent activities and metrics are logged correctly.
        """
        self.monitor.track_activity("Data processing started", status="In Progress")
        self.monitor.track_activity("Training model", status="Completed")
        self.monitor.log_metric("CPU Usage", 75.5)
        self.monitor.log_metric("Memory Usage", 2048)
 
        self.assertEqual(len(self.monitor.activities), 2)
        self.assertEqual(len(self.monitor.metrics["CPU Usage"]), 1)
        self.assertEqual(self.monitor.metrics["Memory Usage"][0]["value"], 2048)
 
    def test_behavior_analysis(self):
        """
        Test whether behavior analysis provides correct reports.
        """
        self.analyzer.log_activity({"status": "Completed", "description": "Task 1"})
        self.analyzer.log_activity({"status": "Error", "description": "Task 2"})
        self.analyzer.log_activity({"status": "Completed", "description": "Task 3"})
 
        report = self.analyzer.analyze_behavior()
 
        self.assertEqual(report["total_tasks"], 3)
        self.assertEqual(report["completed_tasks"], 2)
        self.assertEqual(report["error_tasks"], 1)
        self.assertAlmostEqual(report["efficiency"], 66.67, delta=0.01)
 
    def test_anomaly_detection(self):
        """
        Test whether anomaly detection works correctly.
        """
        data_points = [0.5, 0.6, 0.9, 1.2, 0.3, 0.95]
        anomalies = self.detector.detect(data_points)
 
        self.assertEqual(len(anomalies), 2)
        self.assertIn(1.2, anomalies)
        self.assertIn(0.95, anomalies)
 
    def test_full_system_integration(self):
        """
        Test the integration of all system components.
        """
        self.monitor.track_activity("Task Execution", status="Completed")
        self.monitor.log_metric("CPU Usage", 90.0)
 
        report = self.monitor.generate_report()
        anomalies_detected = self.detector.detect([50, 75, 90, 100])
 
        self.assertEqual(report["total_activities"], 1)
        self.assertEqual(report["metrics_logged"]["CPU Usage"], 1)
        self.assertTrue(len(anomalies_detected) > 0)
 
    def tearDown(self):
        """
        Cleanup after each test case.
        """
        del self.monitor
        del self.analyzer
        del self.detector
 
if __name__ == "__main__":
    unittest.main()

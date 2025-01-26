# test_behavior.py
 
import unittest
from src.behavior_analysis.behavior_analyzer import BehaviorAnalyzer
 
class TestBehaviorAnalyzer(unittest.TestCase):
    """
    Unit tests for the BehaviorAnalyzer class.
    """
 
    def setUp(self):
        """
        Setup function to initialize the BehaviorAnalyzer instance.
        """
        self.analyzer = BehaviorAnalyzer(agent_id="TestAgent001")
 
    def test_log_activity_valid(self):
        """
        Test logging a valid activity.
        """
        activity = {"status": "Completed", "description": "Task execution"}
        self.analyzer.log_activity(activity)
        self.assertEqual(len(self.analyzer.logs), 1)
        self.assertEqual(self.analyzer.logs[0]["status"], "Completed")
 
    def test_log_activity_invalid(self):
        """
        Test logging an invalid activity (missing status key).
        """
        activity = {"description": "Invalid Task"}
        with self.assertRaises(ValueError):
            self.analyzer.log_activity(activity)
 
    def test_analyze_behavior(self):
        """
        Test behavior analysis to ensure correct calculation of efficiency.
        """
        self.analyzer.log_activity({"status": "Completed", "description": "Task 1"})
        self.analyzer.log_activity({"status": "Error", "description": "Task 2"})
        self.analyzer.log_activity({"status": "Completed", "description": "Task 3"})
 
        report = self.analyzer.analyze_behavior()
 
        self.assertEqual(report["total_tasks"], 3)
        self.assertEqual(report["completed_tasks"], 2)
        self.assertEqual(report["error_tasks"], 1)
        self.assertAlmostEqual(report["efficiency"], 66.67, delta=0.01)
 
    def test_generate_report(self):
        """
        Test generating a human-readable report.
        """
        self.analyzer.log_activity({"status": "Completed", "description": "Task A"})
        report = self.analyzer.generate_report()
 
        self.assertIn("Behavior Analysis Report for Agent", report)
        self.assertIn("Total Tasks:", report)
        self.assertIn("Completed Tasks:", report)
        self.assertIn("Efficiency:", report)
 
    def test_empty_logs(self):
        """
        Test behavior analysis with no logged activities.
        """
        report = self.analyzer.analyze_behavior()
        self.assertEqual(report["total_tasks"], 0)
        self.assertEqual(report["efficiency"], 0)
 
    def tearDown(self):
        """
        Cleanup function after each test.
        """
        del self.analyzer
 
if __name__ == "__main__":
    unittest.main()

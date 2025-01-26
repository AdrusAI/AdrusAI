# test_anomalies.py
 
import unittest
from src.anomaly_detection.anomaly_detector import AnomalyDetector
 
class TestAnomalyDetector(unittest.TestCase):
    """
    Unit tests for the AnomalyDetector class.
    """
 
    def setUp(self):
        """
        Setup function to initialize the AnomalyDetector instance.
        """
        self.detector = AnomalyDetector(threshold=0.8)
 
    def test_anomaly_detection_with_valid_data(self):
        """
        Test anomaly detection with a valid dataset.
        """
        data = [0.5, 0.7, 0.9, 1.2, 0.3, 0.95]
        anomalies = self.detector.detect(data)
 
        self.assertEqual(len(anomalies), 2)
        self.assertIn(0.9, anomalies)
        self.assertIn(1.2, anomalies)
 
    def test_anomaly_detection_with_no_anomalies(self):
        """
        Test when no anomalies are present in the dataset.
        """
        data = [0.1, 0.2, 0.5, 0.6, 0.75]
        anomalies = self.detector.detect(data)
 
        self.assertEqual(len(anomalies), 0)
 
    def test_anomaly_detection_with_empty_data(self):
        """
        Test anomaly detection with an empty dataset.
        """
        data = []
        anomalies = self.detector.detect(data)
 
        self.assertEqual(len(anomalies), 0)
 
    def test_anomaly_detection_with_non_numeric_data(self):
        """
        Test anomaly detection with invalid non-numeric data.
        """
        data = ["a", "b", "c"]
        with self.assertRaises(ValueError):
            self.detector.detect(data)
 
    def test_summary_of_anomalies(self):
        """
        Test the summary method for correct calculation of anomaly statistics.
        """
        data = [0.1, 0.4, 0.9, 1.5, 0.3, 0.85]
        summary = self.detector.summary(data)
 
        self.assertEqual(summary["total_values"], 6)
        self.assertEqual(summary["anomalies_detected"], 2)
        self.assertAlmostEqual(summary["anomaly_percentage"], 33.33, delta=0.01)
 
    def tearDown(self):
        """
        Cleanup function after each test.
        """
        del self.detector
 
if __name__ == "__main__":
    unittest.main()
 

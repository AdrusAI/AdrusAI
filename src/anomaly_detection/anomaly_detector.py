anomaly_detector.py
class AnomalyDetector:
    """
    A class for detecting anomalies in AI agent performance data.
    """

    def init(self, threshold=0.85):
        """
        Initializes the anomaly detector with a specified threshold.

        :param threshold: float, value above which a data point is considered an anomaly.
        """
        self.threshold = threshold

    def detect(self, data):
        """
        Detects anomalies in the provided dataset based on the threshold.

        :param data: list of float, the dataset to analyze for anomalies.
        :return: list of float, values that exceed the threshold.
        """
        if not isinstance(data, list):
            raise ValueError("Input data must be a list of numerical values.")

        anomalies = [value for value in data if value > self.threshold]
        return anomalies

    def summary(self, data):
        """
        Provides a summary of the dataset including number of anomalies detected.

        :param data: list of float, the dataset to analyze.
        :return: dict, summary containing total values, anomalies detected, and percentage of anomalies.
        """
        total_values = len(data)
        anomalies = self.detect(data)
        anomaly_count = len(anomalies)
        anomaly_percentage = (anomaly_count / total_values) * 100 if total_values > 0 else 0

        return {
            "total_values": total_values,
            "anomalies_detected": anomaly_count,
            "anomaly_percentage": anomaly_percentage
        }

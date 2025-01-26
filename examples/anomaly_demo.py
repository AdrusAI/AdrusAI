anomaly_demo.py
from src.anomaly_detection.anomaly_detector import AnomalyDetector

Sample data representing AI agent performance metrics
data_points = [0.2, 0.4, 0.6, 1.1, 0.8, 0.3, 0.9, 1.5]

Initialize the anomaly detector with a threshold value
detector = AnomalyDetector(threshold=0.85)

Detect anomalies in the data
anomalies = detector.detect(data_points)

Display results
if anomalies: print("Anomalies detected in the dataset:", anomalies) else: print("No anomalies detected. System operating normally.")

Example of logging potential anomalies
for value in anomalies: print(f"Alert: Anomaly detected with value {value}, exceeding threshold.")

End of anomaly_demo.py

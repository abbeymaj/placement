# Importing packages
from src.monitoring.detect_drift import DetectDataDrift

# Running the drift detection pipeline
if __name__ == "__main__":
    drift_detector = DetectDataDrift()
    drift_detector.run_data_drift_detection()
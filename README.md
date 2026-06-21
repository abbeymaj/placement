# 🎓 Predicting Student Placements
*A Machine Learning project to predict whether a student will get placed in a firm.*

---

## 📌 Overview  
This project predicts whether a student will find a job (get placed) based on several features. The features are as follows:

- Intellectual Quotient (IQ) 
- CGPA
- Communication Skills
- Projects Completed 

The task is framed as a **classification problem**, and the project includes a full end‑to‑end workflow: data ingestion, model training, model registry, monitoring, and a Flask-based web interface for real-time predictions.

---

## 🚀 Installation  

It is recommended to install dependencies inside a **virtual environment** (e.g., `venv` or Anaconda).

This project was built using **Python 3.9**.

```bash
pip install -r requirements.txt

```
## 🧰 Tech Stack  

| Category | Tools |
|---------|-------|
| **Frontend** | Flask, HTML, CSS |
| **Backend** | Flask |
| **Language** | Python |
| **Model Registry** | MLflow (via Dagshub) |
| **Monitoring** | Evidently |
| **Feature Store** | GitHub |
| **CI/CD** | GitHub Actions |
| **Database** | SQLite |

---

## 🏗️ High‑Level Design Document  

You can view the full High‑Level Design Document here:

[📄 ****]()

---

## 🌐 Web Application Screenshots  

The project includes a simple two‑page Flask web app for user interaction.

---

### 🏠 Landing Page  
Provides an overview of the project and navigation to the prediction interface.

![Landing Page Screenshot](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/placement_landing_page.jpg)

---

### 🎯 Prediction Page  
Allows users to input student details (IQ, CGPA, Communication Skills, Projects Completed) and generate a prediction whether the student will get placed or not (that is, "Yes" or "No").

![Prediction Page Screenshot](https://github.com/abbeymaj80/my-ml-datasets/blob/master/screenshots/placement_prediction.jpg)
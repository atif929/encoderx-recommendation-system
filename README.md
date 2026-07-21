# Movie Recommendation System

## Overview

This project was developed as part of the **EncoderX AI/ML Internship – Week 03**.

The objective of this project is to build a movie recommendation system using **Collaborative Filtering**. The system predicts user preferences and recommends movies based on historical user ratings.

---

## Dataset

MovieLens 100K Dataset

- 100,000 Ratings
- 943 Users
- 1,682 Movies

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Scikit-Surprise
- Matplotlib
- Jupyter Notebook

---

## Data Preparation

The dataset was cleaned and prepared by:

- Removing duplicate records
- Checking missing values
- Creating a user-item interaction matrix

---

## Recommendation Algorithm

**Collaborative Filtering**

Model Used:

- Singular Value Decomposition (SVD)

---

## Evaluation

The recommendation system was evaluated using:

- RMSE
- Precision@10
- Recall@10

---

## Demonstration Interface

A simple console-based interface allows users to enter a User ID and receive the top movie recommendations.

---

## Project Structure

```text
encoderx-recommendation-system/
│
├── app/
├── dataset/
├── images/
├── models/
├── notebook/
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the Notebook

```bash
jupyter notebook
```

Open:

```
recommendation_system.ipynb
```

---

## Run the Interface

```bash
cd app
python interface.py
```

---

## Author

**Atif Rameez**

EncoderX AI/ML Internship
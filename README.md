# 🏏 IPL Win Probability Predictor

This is a simple Streamlit web application that predicts the winning probability of an IPL team during a live match, based on current match conditions.

## 🔮 Features

- Select **Batting** and **Bowling** teams
- Enter **match conditions**: runs, wickets, overs, target score, etc.
- Displays the **real-time win probability** for each team using a trained machine learning model
- Gives visual feedback using progress bars and probability percentages

## 🚀 Live Demo

[Add your deployed Streamlit link here, e.g. via Streamlit Community Cloud or another hosting service]

## 🖥️ Screenshots

![UI Preview](uidemo.png)

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend / Model**: Scikit-learn
- **Language**: Python
- **Model Type**: Trained on past IPL match data using classification algorithms (e.g. Logistic Regression, Random Forest)

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/bharthdev-05/ipl-win-predictor.git
cd ipl-win-predictor

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activat

3. **Install dependencies**

```bash
pip install -r requirements.txt

4. **Run the app**

```bash
streamlit run app.py

🧠 Future Improvements
Add match visualization charts (run rate comparison, momentum graph)
Deploy using Streamlit Cloud / AWS / Heroku
Live data integration via API
Add T20 leagues from other countries

🙌 Acknowledgements
Kaggle IPL datasets
Streamlit Docs
Scikit-learn & Pandas

📬 Contact
For questions, suggestions, or feedback, feel free to reach out at [bharathsde05@gmail.com] or raise an issue.

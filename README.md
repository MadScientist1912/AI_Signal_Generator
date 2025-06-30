# 🧠 AI Signal Generator

An AI-powered multi-asset signal prediction system that uses technical indicators and machine learning to generate Buy / Hold / Sell signals for stocks, cryptocurrencies, and commodities.

---

## 🚀 Features

* 📈 Trains models for multiple financial assets (AAPL, BTC-USD, ETH-USD, NVDA, GLD, USO)
* 🤖 Uses XGBoost for classification
* 🧮 Generates technical indicators using `ta`
* ⚖️ Automatically balances classes (Buy/Hold/Sell)
* 🔮 Predicts trading signals + backtests strategy
* 📊 Streamlit dashboard to visualize and interact with live predictions

---

## 🗂️ Project Structure

```
├── app.py                         # Streamlit dashboard
├── models/                        # Trained XGBoost models
├── data/
│   ├── predictions/              # Predictions for each asset
│   ├── processed/                # Processed CSVs with indicators (optional)
│   └── raw/                      # Raw market data (optional)
```

---

## ⚙️ Setup Instructions

### ✅ Local Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/MadScientist1912/AI_Signal_Generator.git
   cd AI_Signal_Generator
   ```

2. Create a virtual environment (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Live Dashboard (via Streamlit Cloud)

[Deploy this app on Streamlit Cloud](https://streamlit.io/cloud)

Just connect this GitHub repo → click **"Deploy"** → enjoy your hosted dashboard in under 2 minutes.

---

## 📸 Screenshot

![Dashboard Screenshot](https://github.com/MadScientist1912/AI_Signal_Generator/raw/main/demo_screenshot.png)

---

## 🧩 Future Improvements

* Add SHAP for model explainability
* Include equity curve & backtest analytics
* Improve prediction accuracy via ensemble models
* Build an alert system for real-time triggers

---

## 👤 Author

**MadScientist1912**
[GitHub Profile](https://github.com/MadScientist1912)

---

## 📄 License

MIT License – use freely, credit appreciated.

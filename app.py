import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Signal Generator", layout="wide")
st.title("📈 AI-Powered Multi-Asset Signal Dashboard")

# --- Asset Selector ---
assets = [f.split('_')[-1].replace('.pkl', '') for f in os.listdir("models") if f.endswith(".pkl")]
selected_asset = st.selectbox("Select an Asset", sorted(assets))

# --- Load Model & Predictions ---
model_path = f"models/xgb_model_{selected_asset}.pkl"
pred_path = f"data/predictions/predictions_{selected_asset}.csv"

if os.path.exists(model_path) and os.path.exists(pred_path):
    model = joblib.load(model_path)
    df = pd.read_csv(pred_path, index_col=0, parse_dates=True)

    st.subheader("🔮 Latest Prediction")
    signal_map = {0: "Buy", 1: "Hold", 2: "Sell"}
    latest_signal = signal_map[df["Prediction"].iloc[-1]]
    st.metric(label=f"Latest Signal for {selected_asset}", value=latest_signal)

    st.subheader("📊 Historical Predictions")
    df_tail = df.tail(100)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_tail.index, df_tail["Prediction"], marker='o', linestyle='-')
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["Buy", "Hold", "Sell"])
    ax.set_title("Prediction History")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.error("Model or predictions not found for selected asset.")

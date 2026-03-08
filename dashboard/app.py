import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

st.set_page_config(page_title="AI Realtime IDS", layout="wide")

st.title("🔐 AI Powered Realtime Intrusion Detection System")

FILE = "realtime_predictions.json"


def load_data():

    if not os.path.exists(FILE):
        return pd.DataFrame()

    try:
        with open(FILE) as f:
            data = json.load(f)
        return pd.DataFrame(data)

    except:
        return pd.DataFrame()


df = load_data()

if df.empty:
    st.warning("Waiting for realtime predictions...")
    st.stop()


# -------------------
# Metrics
# -------------------

total_flows = len(df)
attacks = len(df[df["prediction"] == "ATTACK"])
benign = len(df[df["prediction"] == "BENIGN"])
avg_prob = df["probability"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Flows", total_flows)
c2.metric("Attack Alerts", attacks)
c3.metric("Benign Flows", benign)
c4.metric("Avg Attack Probability", round(avg_prob, 5))

st.divider()

# -------------------
# Threat Level
# -------------------

if attacks == 0:
    threat = "LOW"
elif attacks < 10:
    threat = "MEDIUM"
else:
    threat = "HIGH"

st.subheader(f"🚨 Threat Level: {threat}")

st.divider()

# -------------------
# Charts
# -------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Attack Probability Timeline")

    df["index"] = range(len(df))

    fig = px.line(
        df,
        x="index",
        y="probability",
        title="Attack Probability Over Time"
    )

    st.plotly_chart(fig, width="stretch")

with col2:

    st.subheader("Prediction Distribution")

    counts = df["prediction"].value_counts()

    fig2 = px.pie(
        values=counts.values,
        names=counts.index,
        title="Traffic Classification"
    )

    st.plotly_chart(fig2, width="stretch")

st.divider()

# -------------------
# Protocol Distribution
# -------------------

st.subheader("Network Protocol Distribution")

if "protocol" in df.columns:

    proto_counts = df["protocol"].value_counts()

    fig_proto = px.pie(
        values=proto_counts.values,
        names=proto_counts.index,
        title="Traffic by Protocol"
    )

    st.plotly_chart(fig_proto, width="stretch")

else:
    st.info("Protocol information not available yet.")

st.divider()

# -------------------
# Top Attackers
# -------------------

st.subheader("Top Suspicious IPs")

attack_df = df[df["prediction"] == "ATTACK"]

if not attack_df.empty and "src_ip" in attack_df.columns:

    top_ips = attack_df["src_ip"].value_counts().head(5)

    fig3 = px.bar(
        x=top_ips.values,
        y=top_ips.index,
        orientation="h",
        labels={"x": "Alerts", "y": "IP Address"},
        title="Top Attack Sources"
    )

    st.plotly_chart(fig3, width="stretch")

else:
    st.info("No attack sources detected.")

st.divider()

# -------------------
# Latest Predictions
# -------------------

st.subheader("Latest Predictions")

columns_to_show = ["timestamp", "src_ip", "flow_packets", "prediction", "probability"]

available_cols = [c for c in columns_to_show if c in df.columns]

st.dataframe(
    df[available_cols].tail(10),
    width="stretch"
)

st.divider()

# -------------------
# 🚨 Live Alerts
# -------------------

st.subheader("🚨 Live Alerts")

if os.path.exists("alerts.json"):

    try:
        with open("alerts.json", "r") as f:
            alerts = json.load(f)

        alert_df = pd.DataFrame(alerts)

        if not alert_df.empty:
            st.dataframe(alert_df.tail(10), width="stretch")
        else:
            st.info("No alerts triggered.")

    except:
        st.info("Alert log exists but could not be read.")

else:
    st.info("No alerts triggered yet.")

st.divider()

# -------------------
# SHAP Explainability
# -------------------

st.subheader("Explainable AI (SHAP)")

latest = df.iloc[-1]

shap_data = latest.get("explanation")

if isinstance(shap_data, dict):

    shap_df = pd.DataFrame(
        list(shap_data.items()),
        columns=["Feature", "Importance"]
    )

    shap_df = shap_df.sort_values("Importance")

    fig4 = px.bar(
        shap_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Contribution to Prediction"
    )

    st.plotly_chart(fig4, width="stretch")

else:

    st.info("SHAP explanation not available yet.")
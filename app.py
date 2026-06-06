import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Banking Fraud Detection System",
    layout="wide"
)

# ---------------- LOGIN ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🏦 Bank Employee Login")

    username = st.text_input("Employee ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "bank123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid Credentials")

# ---------------- DASHBOARD ----------------

else:

    st.title("🏦 Banking Fraud Detection System")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # Load Dataset
    data = pd.read_csv("creditcard.csv")

    # Load Model
    model = joblib.load("fraud_model.pkl")

    # Overview
    st.header("📊 Dataset Overview")
    st.write(data.head())

    # Statistics
    st.header("📈 Dataset Statistics")
    st.write(data.describe())

    # Fraud Distribution
    st.header("Fraud vs Genuine Transactions")

    fraud_count = data["Class"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(
        ["Genuine", "Fraud"],
        [fraud_count[0], fraud_count[1]]
    )

    ax.set_title("Transaction Distribution")
    st.pyplot(fig)

    # Pie Chart
    st.header("Fraud Percentage")

    fig2, ax2 = plt.subplots()

    ax2.pie(
        [fraud_count[0], fraud_count[1]],
        labels=["Genuine", "Fraud"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig2)

    # Fraud Transaction List
    st.header("Known Fraud Transactions")

    fraud_rows = data[data["Class"] == 1]

    st.write(
        "Sample Fraud Indexes:",
        fraud_rows.index.tolist()[:20]
    )

    # Prediction Section
    st.header("Transaction Verification")

    index = st.number_input(
        "Enter Transaction Index",
        min_value=0,
        max_value=len(data)-1,
        value=int(fraud_rows.index[0])
    )

    sample = data.drop("Class", axis=1).iloc[[index]]

    prediction = model.predict(sample)

    actual = data["Class"].iloc[index]

    st.write("Actual Class:", actual)

    if prediction[0] == 1:
        st.error("🚨 FRAUD TRANSACTION DETECTED")
    else:
        st.success("✅ Genuine Transaction")

    # ALERT SIMULATION
    st.header("Alert System")

    if st.button("🚨 Simulate Fraud Alert"):

        st.error("Fraudulent Transaction Detected")

        st.subheader("📧 Email Alert")

        st.code("""
To: fraud@bank.com

Subject: Fraud Transaction Alert

Dear Security Team,

A suspicious transaction has been detected.

Please verify immediately.

Regards,
Fraud Detection System
        """)

        st.subheader("📱 SMS Alert")

        st.code("""
SMS ALERT

Warning!

Fraudulent transaction detected.

Account temporarily flagged.

Please contact the bank immediately.
        """)

        st.success("Alerts Generated Successfully")

    # Project Details
    st.header("Project Information")

    st.info("""
Project Name:
Banking Fraud Detection System

Algorithm:
Random Forest Classifier

Accuracy:
99.95%

Modules:
✔ Employee Login
✔ Fraud Detection
✔ Data Visualization
✔ Email Alert Simulation
✔ SMS Alert Simulation
✔ Machine Learning Prediction

Technology:
Python, Streamlit, Pandas,
Scikit-Learn, Matplotlib
    """)

import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title = "Credit Risk Prediction System",
    page_icon = "💳",
    layout = "wide",
    initial_sidebar_state = "expanded"
)
# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
            
/* Main background */
.stApp{
    background-color:#ffffff;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:#F8FAFC;
    border-radius:15px;
    padding:20px;
    border:1px solid #D6E4F0;
    box-shadow:0px 5px 12px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton>button{
    background:#2E86DE;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    padding:12px;
}

.stButton>button:hover{
    background:#1B4F72;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#1F2937;
}

section[data-testid="stSidebar"] *{
    color:white;
}
            
</style>
""", unsafe_allow_html=True)
st.write("")
# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("credit_risk_model.pkl")
st.write("")
#----------------------------
# Sidebar
# ----------------------------
st.sidebar.image(
    "https://img.icons8.com/color/96/bank-building.png",
    width=80
)

st.sidebar.title("Credit Risk Dashboard")

st.sidebar.markdown("---")

st.sidebar.metric("Model", "ElasticNet")

st.sidebar.metric("ROC-AUC", "0.74")

st.sidebar.metric("SMOTE", "Enabled")

st.sidebar.markdown("---")

st.sidebar.success("FutureAI Internship Project")

st.sidebar.caption("Developed by Shreya Magadum")
st.write("")
# ----------------------------
# Main Title
# ----------------------------
st.markdown("""
<div style="text-align:center; padding-top:5px; padding-bottom:15px;">

<h1 style="
font-size:48px;
font-weight:700;
color:#2563EB;
margin-bottom:0;">
💳 Credit Risk Prediction
</h1>

<p style="
font-size:20px;
color:#555;
margin-top:5px;">
AI-Powered Loan Default Prediction System
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#1E3A8A;
padding:15px;
border-radius:12px;
text-align:center;
color:white;
font-size:18px;
font-weight:500;
margin-bottom:20px;">

🏦 Banking Analytics Dashboard | ElasticNet Model

</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "ElasticNet")

with col2:
    st.metric("ROC-AUC", "0.74")

with col3:
    st.metric("Algorithm", "SMOTE + ElasticNet")

st.write(
    "Predict the probability that a loan applicant will default using an ElasticNet machine learning model."
)

st.markdown("---")
st.write("")
# ----------------------------
# Input Fields
# ----------------------------

st.subheader("📝 Applicant Information")
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    person_age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    person_income = st.number_input(
        "Annual Income ($)",
        min_value=0,
        value=50000
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    person_emp_length = st.number_input(
        "Employment Length (Years)",
        min_value=0.0,
        value=5.0
    )

    loan_intent = st.selectbox(
        "Loan Purpose",
        [
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "PERSONAL",
            "HOMEIMPROVEMENT",
            "DEBTCONSOLIDATION"
        ]
    )

with col2:

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A","B","C","D","E","F","G"]
    )

    loan_amnt = st.number_input(
        "Loan Amount ($)",
        min_value=500,
        value=10000
    )

    loan_int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        value=10.5
    )

    loan_percent_income = st.slider(
        "Loan / Income Ratio",
        0.0,
        1.0,
        0.20,
        step=0.01
    )

    cb_person_default_on_file = st.selectbox(
        "Previous Default",
        ["N","Y"]
    )

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length",
        min_value=1,
        value=5
    )

# ----------------------------
# Prediction
# ----------------------------

predict = st.button(
    "🔍 Predict Credit Risk",
    use_container_width=True
)

if predict:

    # Create dataframe
    data = pd.DataFrame({
        "person_age":[person_age],
        "person_income":[person_income],
        "person_home_ownership":[person_home_ownership],
        "person_emp_length":[person_emp_length],
        "loan_intent":[loan_intent],
        "loan_grade":[loan_grade],
        "loan_amnt":[loan_amnt],
        "loan_int_rate":[loan_int_rate],
        "loan_percent_income":[loan_percent_income],
        "cb_person_default_on_file":[cb_person_default_on_file],
        "cb_person_cred_hist_length":[cb_person_cred_hist_length]
    })

    # Prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if prediction == 0:
         st.markdown("""
            <div style='background:#D5F5E3;
                padding:15px;
                border-radius:10px;
                text-align:center;
                color:#145A32;
                font-size:24px;
                font-weight:bold;'>

                ✅ LOW CREDIT RISK

            </div>
                """, unsafe_allow_html=True)

    else:
        st.markdown("""
            <div style='background:#FADBD8;
                padding:15px;
                border-radius:10px;
                text-align:center;
                color:#922B21;
                font-size:24px;
                font-weight:bold;'>

                🔴 HIGH CREDIT RISK

            </div>
            """, unsafe_allow_html=True)


    # Three dashboard cards
    c1, c2, c3 = st.columns(3)

    with c1:
        if prediction == 1:
            st.error("🔴 HIGH RISK")
        else:
            st.success("🟢 LOW RISK")

    with c2:
        st.metric(
            "Default Probability",
            f"{probability*100:.2f}%"
        )

    with c3:
        st.metric(
            "ROC-AUC",
            "0.74"
        )

    st.markdown("### Risk Score")

    st.progress(probability)

    st.caption(f"Risk Score: {probability*100:.2f}%")

    if probability < 0.30:
        st.success("Excellent Credit Profile")
    elif probability < 0.60:
        st.warning("Moderate Credit Risk")
    else:
        st.error("High Credit Risk")
###########
    


    # ----------------------------
# Applicant Summary
# ----------------------------
    
    st.markdown("---")
    st.subheader("📝 Applicant Summary")

    st.write(f"**Age:** {person_age} years")
    st.write(f"**Annual Income:** ${person_income}")
    st.write(f"**Home Ownership:** {person_home_ownership}")
    st.write(f"**Employment Length:** {person_emp_length} years")
    st.write(f"**Loan Purpose:** {loan_intent}")
    st.write(f"**Loan Grade:** {loan_grade}")
    st.write(f"**Loan Amount:** ${loan_amnt}")
    st.write(f"**Interest Rate:** {loan_int_rate}%")
    st.write(f"**Loan / Income Ratio:** {loan_percent_income*100:.2f}%")
    st.write(f"**Previous Default:** {cb_person_default_on_file}")
    st.write(f"**Credit History Length:** {cb_person_cred_hist_length} years")
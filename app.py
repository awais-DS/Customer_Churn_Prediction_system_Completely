import streamlit as st
from predict import predict

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"], index=None, placeholder="Select...")
dependents = st.selectbox("Dependents", ["Yes", "No"], index=None, placeholder="Select...")
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"],
                        index=None, placeholder="Select...")
tenure = st.number_input("Tenure (months)", min_value=0, value=0, step=1)
monthly = st.number_input("Monthly charges", min_value=0.0, value=0.0, step=1.0)

if st.button("Predict"):
    if gender is None or dependents is None or contract is None:
        st.warning("Please fill in all the fields.")
    else:
        label, score = predict({
            "gender": gender,
            "Dependents": dependents,
            "Contract": contract,
            "tenure": tenure,
            "MonthlyCharges": monthly,
        })
        if label == 1:
            st.error(f"This customer is likely to churn (risk score {score:.0%}).")
        else:
            st.success(f"This customer is likely to stay (risk score {score:.0%}).")

import streamlit as st
import requests
from datetime import datetime

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="EDM Lead Network Ping", page_icon="📞", layout="centered")
st.title("📞 EDM Lead Network Ping API Tester")

# ---------------------------
# Fixed Credentials
# ---------------------------
LP_CAMPAIGN_ID = "689fc15a83cdd"
LP_CAMPAIGN_KEY = "WmDKJVdyvNzHrZjwpkFx"
CALLER_ID = "+18545672120"

# ---------------------------
# Input Fields
# ---------------------------
st.header("🧍 Lead Information (Required)")

# Use columns for side-by-side inputs
col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First Name", "")
    phone_number = st.text_input("Phone Number", "")
    address = st.text_input("Address", "")
    state = st.text_input("State", "")
with col2:
    last_name = st.text_input("Last Name", "")
    email_address = st.text_input("Email Address", "")
    city = st.text_input("City", "")
    zip_code = st.text_input("Zip Code", "")

st.header("🧾 Optional Details")

col3, col4 = st.columns(2)
with col3:
    dob = st.date_input("Date of Birth", value=None)
with col4:
    gender = st.selectbox("Gender", ["", "Male", "Female"])

# ---------------------------
# Submit Button
# ---------------------------
if st.button("🚀 Send Ping"):
    if not all([first_name, last_name, phone_number, email_address,
                address, city, state, zip_code]):
        st.error("⚠️ Please fill in all required fields.")
    else:
        payload = {
            "lp_campaign_id": LP_CAMPAIGN_ID,
            "lp_campaign_key": LP_CAMPAIGN_KEY,
            "caller_id": CALLER_ID,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "email_address": email_address,
            "address": address,
            "city": city,
            "state": state,
            "zip_code": zip_code
        }

        # ---------------------------
        # Make API Request
        # ---------------------------
        try:
            response = requests.post(
                "https://track.edmleadnetwork.com/call-preping.do",
                data=payload,
                timeout=10
            )
            result = response.json()

            st.json(result)

            if result.get("success"):
                st.markdown(f"**💰 Payout:** ${result.get('payout', 'N/A')}")
                st.markdown(f"**⏱️ Duration:** {result.get('duration', 'N/A')} seconds")
                st.markdown(f"**📞 Transfer Number:** {result.get('number', 'N/A')}")
            else:
                st.error(f"❌ {result.get('message', 'Ping Rejected')}")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

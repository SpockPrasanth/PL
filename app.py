import streamlit as st
import pandas as pd

# Set page config and title
st.set_page_config(page_title="Canada Enplanement Data Entry", layout="wide")

# Display your logo (assumes logo is in assets folder)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/paradies_logo.png", use_container_width=True)

st.title("Canada Enplanement Data Entry")

# Dropdown options
countries = ["Canada"]
months = list(range(1, 13))
years = list(range(2000, 3001))

# Initialize session state for data storage
if "enplanement_data" not in st.session_state:
    st.session_state.enplanement_data = pd.DataFrame(
        columns=["COUNTRY", "MONTH", "YEAR", "PASSENGERS"]
    )

# Data entry form
with st.form("entry_form"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        country = st.selectbox("Country", countries)
    with col2:
        month = st.selectbox("Month", months)
    with col3:
        year = st.selectbox("Year", years)
    with col4:
        passengers = st.number_input("Passengers", min_value=0, step=1)

    submitted = st.form_submit_button("Add Data")

if submitted:
    new_entry = pd.DataFrame([{
        "COUNTRY": country,
        "MONTH": month,
        "YEAR": year,
        "PASSENGERS": passengers
    }])
    # Append new data
    st.session_state.enplanement_data = pd.concat(
        [st.session_state.enplanement_data, new_entry],
        ignore_index=True
    )
    st.success("Data added successfully!")

# Show entered data table
st.subheader("Entered Data")
if not st.session_state.enplanement_data.empty:
    st.dataframe(st.session_state.enplanement_data, use_container_width=True)
else:
    st.info("No data entered yet.")

# Buttons for clearing data and placeholder for Snowflake submission
col1, col2 = st.columns(2)

with col1:
    if st.button("Clear Data"):
        st.session_state.enplanement_data = pd.DataFrame(
            columns=["COUNTRY", "MONTH", "YEAR", "PASSENGERS"]
        )
        st.experimental_rerun()

with col2:
    if st.button("Submit to Snowflake (Future)"):
        st.write("Snowflake submission logic to be added here.")
        st.write(st.session_state.enplanement_data)

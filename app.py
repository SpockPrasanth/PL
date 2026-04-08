import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canada Enplanement Entry", layout="wide")

st.title("Canada Enplanement Data Entry")

# -------------------------------
# Dropdown values
# -------------------------------
countries = ["Canada"]  # can expand later
months = list(range(1, 13))
years = list(range(2000, 3001))

# -------------------------------
# Session State (store data)
# -------------------------------
if "enplanement_data" not in st.session_state:
    st.session_state.enplanement_data = pd.DataFrame(
        columns=["COUNTRY", "MONTH", "YEAR", "PASSENGERS"]
    )

# -------------------------------
# Input Form
# -------------------------------
with st.form("data_entry_form"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        country = st.selectbox("Country", countries)

    with col2:
        month = st.selectbox("Month", months)

    with col3:
        year = st.selectbox("Year", years)

    with col4:
        passengers = st.number_input("Passengers", min_value=0, step=1)

    submit = st.form_submit_button("Add Data")

# -------------------------------
# Add Data Logic
# -------------------------------
if submit:
    new_row = pd.DataFrame([{
        "COUNTRY": country,
        "MONTH": month,
        "YEAR": year,
        "PASSENGERS": passengers
    }])

    st.session_state.enplanement_data = pd.concat(
        [st.session_state.enplanement_data, new_row],
        ignore_index=True
    )

    st.success("Data added successfully!")

# -------------------------------
# Show Data Table
# -------------------------------
st.subheader("Entered Data")

if not st.session_state.enplanement_data.empty:
    st.dataframe(
        st.session_state.enplanement_data,
        use_container_width=True
    )
else:
    st.info("No data entered yet.")

# -------------------------------
# Optional Actions
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Clear Data"):
        st.session_state.enplanement_data = pd.DataFrame(
            columns=["COUNTRY", "MONTH", "YEAR", "PASSENGERS"]
        )
        st.experimental_rerun()

with col2:
    if st.button("Submit to Snowflake (Future)"):
        st.write("Integrate Snowflake write here")
        st.write(st.session_state.enplanement_data)

import streamlit as st
import pandas as pd
import os

# File to store units
DATA_FILE = "units_data.csv"

# Load data from CSV
def load_units():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE, index_col=0).to_dict()['count']
    else:
        return {}

# Save data to CSV
def save_units():
    df = pd.DataFrame(list(st.session_state.units.items()), columns=['unit', 'count'])
    df.to_csv(DATA_FILE, index=False)

# Initialize units from file if not already in session_state
if 'units' not in st.session_state:
    st.session_state.units = load_units()

# Function to add units
def add_unit():
    unit_name = st.session_state.unit_name.strip()
    count = st.session_state.unit_count
    if unit_name:
        st.session_state.units[unit_name] = st.session_state.units.get(unit_name, 0) + count
        save_units()
        st.success(f"Added {count} {unit_name}(s). Total: {st.session_state.units[unit_name]}")

# Function to remove units
def remove_unit():
    unit_name = st.session_state.unit_name.strip()
    count = st.session_state.unit_count
    if unit_name in st.session_state.units and st.session_state.units[unit_name] >= count:
        st.session_state.units[unit_name] -= count
        if st.session_state.units[unit_name] == 0:
            del st.session_state.units[unit_name]
        save_units()
        st.success(f"Removed {count} {unit_name}(s). Remaining: {st.session_state.units.get(unit_name, 0)}")
    else:
        st.error(f"Cannot remove {count} {unit_name}(s). Not enough stock or unit does not exist.")

# Streamlit UI with pastel colors
st.markdown(
    """
    <style>
        body {
            background-color: #f9f7f7;
        }
        .stApp {
            background-color: #fefefe;
            border: 2px solid #dbe2ef;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1 {
            color: #3f72af;
            text-align: center;
        }
        .stButton button {
            background-color: #f7d6e0;
            color: black;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #ffdde1;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and input fields
st.title("Unit Counter By Aleena Amir")

with st.container():
    st.subheader("Add or Remove Units")
    st.text_input("Unit Name", key="unit_name")
    st.number_input("Count", min_value=1, step=1, key="unit_count")

    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Add Unit", on_click=add_unit)
    with col2:
        st.button("➖ Remove Unit", on_click=remove_unit)

# Display all units
st.subheader("📊 Current Units")
if st.session_state.units:
    st.table(pd.DataFrame(st.session_state.units.items(), columns=["Unit", "Count"]))
else:
    st.info("No units available yet. Add some units to get started!")



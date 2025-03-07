import streamlit as st

# Initialize or get the session state for the unit counter
if 'units' not in st.session_state:
    st.session_state.units = {}

# Function to add units
def add_unit():
    unit_name = st.session_state.unit_name
    count = st.session_state.unit_count
    if unit_name:
        st.session_state.units[unit_name] = st.session_state.units.get(unit_name, 0) + count
        st.success(f"Added {count} {unit_name}(s). Total: {st.session_state.units[unit_name]}")

# Function to remove units
def remove_unit():
    unit_name = st.session_state.unit_name
    count = st.session_state.unit_count
    if unit_name in st.session_state.units and st.session_state.units[unit_name] >= count:
        st.session_state.units[unit_name] -= count
        st.success(f"Removed {count} {unit_name}(s). Remaining: {st.session_state.units[unit_name]}")
        if st.session_state.units[unit_name] == 0:
            del st.session_state.units[unit_name]
    else:
        st.error(f"Cannot remove {count} {unit_name}(s). Not enough stock or unit does not exist.")

# Title and inputs
st.title("Unit Counter App")

st.text_input("Unit Name", key="unit_name")
st.number_input("Count", min_value=1, step=1, key="unit_count")

col1, col2 = st.columns(2)
with col1:
    st.button("Add Unit", on_click=add_unit)

with col2:
    st.button("Remove Unit", on_click=remove_unit)

# Display all units and counts
st.subheader("Current Units")
if st.session_state.units:
    for unit, count in st.session_state.units.items():
        st.write(f"{unit}: {count}")
else:
    st.write("No units available.")


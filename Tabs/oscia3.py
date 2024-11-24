import streamlit as st
import pandas as pd
import random

# Title
st.title("Smart Traffic Management System by 2341566 and 2341512")

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.traffic_count = {
        'North': random.randint(1, 10),
        'South': random.randint(1, 10),
        'East': random.randint(1, 10),
        'West': random.randint(1, 10)
    }
    st.session_state.signal_state = 'None'
    st.session_state.rounds_waited = {'North': 0, 'South': 0, 'East': 0, 'West': 0}
    st.session_state.process_log = pd.DataFrame(columns=["Step", "Signal State", "Direction Allowed", "Vehicles Moved", "North Traffic", "South Traffic", "East Traffic", "West Traffic"])
    st.session_state.step = 0

# Display current traffic count
st.subheader("Current Vehicle Counts")
for direction, count in st.session_state.traffic_count.items():
    st.write(f"{direction}: {count} vehicles")

# Simulate traffic management logic
if st.button("Simulate Step"):
    # Example simulation logic (replace with actual traffic signal logic)
    current_signal = random.choice(['North', 'South', 'East', 'West'])
    vehicles_moved = min(st.session_state.traffic_count[current_signal], 3)  # Allow up to 3 vehicles to move
    st.session_state.traffic_count[current_signal] -= vehicles_moved
    st.session_state.rounds_waited = {key: val + 1 for key, val in st.session_state.rounds_waited.items()}
    st.session_state.rounds_waited[current_signal] = 0
    st.session_state.signal_state = current_signal
    st.session_state.step += 1

    # Log the step
    st.session_state.process_log = pd.concat([
        st.session_state.process_log,
        pd.DataFrame([{
            "Step": st.session_state.step,
            "Signal State": current_signal,
            "Direction Allowed": current_signal,
            "Vehicles Moved": vehicles_moved,
            "North Traffic": st.session_state.traffic_count['North'],
            "South Traffic": st.session_state.traffic_count['South'],
            "East Traffic": st.session_state.traffic_count['East'],
            "West Traffic": st.session_state.traffic_count['West']
        }])
    ], ignore_index=True)

    st.success(f"Step {st.session_state.step} simulated. {vehicles_moved} vehicles moved from {current_signal}.")

# Reset simulation
if st.button("Reset Simulation"):
    st.session_state.traffic_count = {
        'North': random.randint(1, 10),
        'South': random.randint(1, 10),
        'East': random.randint(1, 10),
        'West': random.randint(1, 10)
    }
    st.session_state.signal_state = 'None'
    st.session_state.rounds_waited = {'North': 0, 'South': 0, 'East': 0, 'West': 0}
    st.session_state.process_log = pd.DataFrame(columns=["Step", "Signal State", "Direction Allowed", "Vehicles Moved", "North Traffic", "South Traffic", "East Traffic", "West Traffic"])
    st.session_state.step = 0
    st.success("Simulation has been reset.")

# Reset vehicle counts manually
if st.button("Reset Vehicle Counts"):
    st.session_state.traffic_count = {
        'North': st.number_input('Enter new number of vehicles on North side:', min_value=0, value=0, step=1),
        'South': st.number_input('Enter new number of vehicles on South side:', min_value=0, value=0, step=1),
        'East': st.number_input('Enter new number of vehicles on East side:', min_value=0, value=0, step=1),
        'West': st.number_input('Enter new number of vehicles on West side:', min_value=0, value=0, step=1)
    }
    st.success("Vehicle counts have been reset manually.")

# Display process log
st.subheader("Process Log")
st.write(st.session_state.process_log)

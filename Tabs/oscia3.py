import streamlit as st
import pandas as pd
import random

def app():
    """Smart Traffic Management System Simulation"""

    # Add a title to the page
    st.title("Smart Traffic Management System")

    # Initialize session state for traffic counts, signal states, and logs
    if 'traffic_count' not in st.session_state:
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

    # Display traffic counts for each direction
    st.subheader("Traffic Counts")
    for direction, count in st.session_state.traffic_count.items():
        st.write(f"{direction}: {count} vehicles")

    # Determine which direction gets the green light
    def determine_signal():
        max_traffic = max(st.session_state.traffic_count.values())
        for direction, count in st.session_state.traffic_count.items():
            if count == max_traffic:
                return direction
        return 'None'

    # Simulate one step of traffic light management
    def simulate_step():
        st.session_state.step += 1
        signal = determine_signal()
        if signal != 'None':
            vehicles_moved = min(st.session_state.traffic_count[signal], 5)  # Simulate moving up to 5 vehicles
            st.session_state.traffic_count[signal] -= vehicles_moved
            st.session_state.rounds_waited = {k: v + 1 for k, v in st.session_state.rounds_waited.items()}
            st.session_state.rounds_waited[signal] = 0
            st.session_state.signal_state = signal
        else:
            vehicles_moved = 0

        # Log the process
        st.session_state.process_log = pd.concat([
            st.session_state.process_log,
            pd.DataFrame([{
                "Step": st.session_state.step,
                "Signal State": signal,
                "Direction Allowed": signal,
                "Vehicles Moved": vehicles_moved,
                "North Traffic": st.session_state.traffic_count['North'],
                "South Traffic": st.session_state.traffic_count['South'],
                "East Traffic": st.session_state.traffic_count['East'],
                "West Traffic": st.session_state.traffic_count['West']
            }])
        ], ignore_index=True)

    # Button to simulate the next step
    if st.button("Simulate Step"):
        simulate_step()

    # Display the current signal state
    st.subheader("Current Signal State")
    st.write(f"Signal is green for: **{st.session_state.signal_state}**")

    # Display the log of the process
    st.subheader("Process Log")
    st.dataframe(st.session_state.process_log)

    # Reset the simulation
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
        st.success("Simulation reset!")

    # Reset vehicle counts manually
    st.subheader("Manually Reset Vehicle Counts")
    north = st.number_input("Enter new number of vehicles for North:", min_value=0, value=st.session_state.traffic_count['North'], step=1)
    south = st.number_input("Enter new number of vehicles for South:", min_value=0, value=st.session_state.traffic_count['South'], step=1)
    east = st.number_input("Enter new number of vehicles for East:", min_value=0, value=st.session_state.traffic_count['East'], step=1)
    west = st.number_input("Enter new number of vehicles for West:", min_value=0, value=st.session_state.traffic_count['West'], step=1)
    
    if st.button("Apply New Vehicle Counts"):
        st.session_state.traffic_count = {'North': north, 'South': south, 'East': east, 'West': west}
        st.success("Vehicle counts updated!")


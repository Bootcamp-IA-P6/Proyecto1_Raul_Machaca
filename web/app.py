import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from taximeter import Trip
from src.auth import authenticate
from src.db import get_all_trips

st.title("F5 Taximeter Web")

# --- Autenticación ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.success("Logged in!")
        else:
            st.error("Invalid credentials")
else:
    st.success("Welcome!")

    if "trip" not in st.session_state:
        st.session_state.trip = Trip()

    trip = st.session_state.trip

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start Trip"):
            trip.start()
            st.success("Trip started")
    with col2:
        if st.button("Stop"):
            trip.change_state("stopped")
            st.info("State: stopped")
    with col3:
        if st.button("Move"):
            trip.change_state("moving")
            st.info("State: moving")

    if st.button("Finish Trip"):
        fare = trip.finish()
        st.metric("Fare (€)", f"{fare:.2f}")

    st.subheader("Trip History")
    trips = get_all_trips()
    if trips:
        for t in trips:
            st.write(f"Stopped: {t['stopped_time']:.1f}s | Moving: {t['moving_time']:.1f}s | Fare: €{t['total_fare']:.2f}")

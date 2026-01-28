import streamlit as st
import requests

st.title("🏭 Worker Productivity Dashboard")

backend_url = "http://127.0.0.1:8000"

metrics = requests.get(f"{backend_url}/metrics").json()

st.metric("Total Workers", metrics["total_workers"])
st.metric("Total Workstations", metrics["total_stations"])
st.metric("Total Events", metrics["total_events"])

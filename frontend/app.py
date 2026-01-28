import streamlit as st
import requests
import os

st.title("🏭 Worker Productivity Dashboard")

backend_url = os.getenv("BACKEND_URL")

if not backend_url:
    st.error("Backend URL not configured")
else:
    try:
        metrics = requests.get(f"{backend_url}/metrics", timeout=5).json()
        st.metric("Total Workers", metrics["total_workers"])
        st.metric("Total Workstations", metrics["total_stations"])
        st.metric("Total Events", metrics["total_events"])
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")

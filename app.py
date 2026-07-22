import streamlit as st
import subprocess
import sys

st.title("Debug")

st.write("Python:", sys.version)

result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True,
    text=True
)

st.text(result.stdout)

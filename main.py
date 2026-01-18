import streamlit as st
import pandas as pd
import numpy as np

st.title('F-lite')

col1, col2, col3, col4 = st.columns(4)
col1.title("a")
col2.title("a")
col3.title("a")
col4.title("a")

np.random.seed(42)
data = pd.DataFrame({
    'X': np.random.randn(50),  # random numbers for X-axis
    'Y': np.random.randn(50),  # random numbers for Y-axis
    'Size': np.random.randint(10, 100, size=50),  # optional: size of points
    'Color': np.random.randint(0, 100, size=50)   # optional: color intensity
})

# Basic scatter chart
st.write("SCATTER, SCRAM, SIX SEVEN:")
st.scatter_chart(data[['X', 'Y']])
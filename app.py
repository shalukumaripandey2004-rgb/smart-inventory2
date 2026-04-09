
import pyodbc
import pandas as pd

# --- Connect to SQL Server ---
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'          
    'DATABASE=SmartInventory;'   
    'Trusted_Connection=yes;' 
)

# --- Load data from SQL Server ---
df = pd.read_sql("SELECT * FROM Machines;", conn)

# --- Print data to confirm ---
print(df)
import streamlit as st

# --- Dashboard Title ---
st.title("Smart Equipment Dashboard")


# --- KPIs ---
st.metric("Total Machines", len(df))
st.metric("Active", len(df[df['Status'] == "Working"]))
st.metric("Faulty", len(df[df['Status'] == "Faulty"]))

# --- Charts ---
st.subheader("Machine Status Distribution")
st.bar_chart(df['Status'].value_counts())

st.subheader("Machines by Location")
st.bar_chart(df['Location'].value_counts())

# --- Machine Table ---
st.subheader("Machine List")
st.dataframe(df)
# --- Update Machine Status ---
st.subheader("Update Machine Status")

# Select machine by name
machine_name = st.selectbox("Select Machine", df['Name'])

# Choose new status
new_status = st.selectbox("New Status", ["Working", "Faulty", "In", "Out"])

# Update button
if st.button("Update Status"):
    cursor = conn.cursor()
    cursor.execute("UPDATE Machines SET Status=? WHERE Name=?", (new_status, machine_name))
    conn.commit()
    st.success(f"Status for {machine_name} updated to {new_status}!")
    import streamlit as st
import pandas as pd
import plotly.express as px

# Example dataframe (replace with your SQL query result)
# df = pd.read_sql("SELECT * FROM Machines", conn)

import datetime

st.subheader("Update Machine Location")

# Select the machine you want to move
machine_name = st.selectbox("Select Machine", df['Name'], key="update_machine_location")

# Get current location
current_row = df[df['Name'] == machine_name].iloc[0]
st.write(f"Current Location: {current_row['Location']}")

# Enter new location
new_location = st.text_input("New Location", current_row['Location'], key="new_location_input")

# Update button
if st.button("Change Location", key="change_location_button"):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Machines SET Location=?, LastUpdated=? WHERE Name=?",
        (new_location, datetime.datetime.now(), machine_name)
    )
    conn.commit()
    st.success(f"{machine_name} moved → New Location: {new_location}")

    import pandas as pd
import streamlit as st

# machine image adding



import pandas as pd
import streamlit as st

df = pd.read_csv("machines.csv")

st.write("### Machine List with Images")

for _, row in df.iterrows():
    st.write(f"**{row['Name']}** — {row['Status']} ({row['Location']})")
    st.image(row['ImageUrl'], width=150)   # <-- use correct version here

# again

import pandas as pd
import streamlit as st
import os

df = pd.read_csv("machines.csv")

st.write("### Machine List with Images")

for _, row in df.iterrows():
    img_path = os.path.join("images", row['ImageUrl'])
    
    if os.path.exists(img_path):
        st.image(img_path, width=150)
    else:
        st.warning(f"Image not found: {img_path}")





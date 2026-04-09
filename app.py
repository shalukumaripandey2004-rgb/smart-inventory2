import pandas as pd
import streamlit as st

# --- Load data from CSV ---
df = pd.read_csv("machines.csv")

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

# --- Machine Details with Color-Coded Alerts ---
st.subheader("Machine Details")
for i, row in df.iterrows():
    st.markdown(f"### {row['Name']}")
    st.image(row["ImageUrl"])
    if row["Status"].lower() == "working":
        st.success(f"Status: {row['Status']}")
    elif row["Status"].lower() in ["idle", "out"]:
        st.warning(f"Status: {row['Status']}")
    else:
        st.error(f"Status: {row['Status']}")

# --- Update Machine Status ---
st.subheader("Update Machine Status")

# Select machine by name
machine_name = st.selectbox("Select Machine", df['Name'])

# Choose new status
new_status = st.selectbox("New Status", ["Working", "Faulty", "Idle", "Out"])

# Apply update
if st.button("Update Status"):
    df.loc[df['Name'] == machine_name, 'Status'] = new_status
    st.success(f"Updated {machine_name} to {new_status}")
    st.dataframe(df)

    # Optional: save back to CSV so changes persist
    df.to_csv("machines.csv", index=False)

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





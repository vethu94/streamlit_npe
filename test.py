import pandas as pd
import pymongo
import streamlit as st
import matplotlib.pyplot as plt

# Setup MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["firmware"]
collection = db["firmware_data"]

# Read CSV and Create Dropdown List
df = pd.read_csv("data.csv")
options = list(df['Options'])

# First Tab
def tab1():
    st.write("## Tab 1")
    selected_option = st.selectbox("Select an option:", options)
    input_value = st.text_input("Enter a value:")
    if st.button("Confirm"):
        st.write("Selected option:", selected_option)
        st.write("Input value:", input_value)

# Second Tab
def tab2():
    st.write("## Tab 2")
    version_filter = st.text_input("Enter firmware version:")
    data = collection.find({"firmware_version": version_filter})
    df = pd.DataFrame(list(data))
    if not df.empty:
        st.write(df)
        plt.plot(df['x'], df['y'])
        st.pyplot()
def main():
    # Create Tabs
    tabs = ["Tab 1", "Tab 2"]
    page = st.sidebar.radio("Select a page:", tabs)

    if page == "Tab 1":
        tab1()
    else:
        tab2()
if __name__ == '__main__':
    main()
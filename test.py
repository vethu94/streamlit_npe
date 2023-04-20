import pandas as pd
import pymongo
import streamlit as st
import matplotlib.pyplot as plt
import csv

# Setup MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
id_collection = db["id_counter"]
collection = db["mycollection"]

# CSV-Datei im Lese-Modus öffnen
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    data = [row for row in reader]
    # Read CSV and Create Dropdown List

    options = []
    for row in data:
        options.append(row[0])


# First Tab
def tab1():

    st.write("## Testcase")

    selected_option = st.selectbox("Select an option:", options)
    for item in data:
        if selected_option in item[0]:  # output (String vergleichen mit array)
            unit_name = (item[1])
            serialNr = (item[2])
            serialNrAntenna = (item[3])
    st.write("Unit name: " + unit_name)
    st.write("SerialNr:" + serialNr)
    st.write("SNAntenna:" + serialNrAntenna)
    input_value = st.text_input("Enter a value:")

    if st.button("Confirm"):
        st.write("Selected option:", selected_option)
        st.write("Input value:", input_value)

    # Define the data as a list of lists
    data3 = [
        ["Author Name", "Testunit Name", "Test Command"],
        ["Patrick Mueller", "1.2", "Testcase 2,3"],
        ["Nattan Meier", "1.3", "Testcase 3,5 "],
        ["Philip Schaerer", "2.4", "Testcase 4,2"],
    ]

    # Create a pandas DataFrame with the data
    df = pd.DataFrame(data3[1:], columns=data3[0])

    # Display the DataFrame in a table in Streamlit
    st.table(df)

# Second Tab
def tab2():
    st.write("## Analyze")
    count = db.collection.count_documents({})
    st.write("Number of documents in collection:", count)
    # Get all documents in the collection
    documents = db.collection.find()

    # Print out the documents in Streamlit
    st.write("Documents in collection:")
    for document in documents:
        st.write(document)
    # Get all distinct firmware versions
    versions = db.collection.distinct("firmware")

    # Print the list of firmware versions
    st.write("Firmware versions found:")
    st.write(versions)
    version_filter = st.text_input("Enter firmware version:")
    result_list = list(db.collection.find({"firmware": version_filter}, {"bootuptime": 1}))
    st.write(result_list)




    #df = pd.DataFrame(list(data2))
    #if not df.empty:
    #    st.write(df)
    #    plt.plot(df['x'], df['y'])
    #    st.pyplot()


def main():
    # Create Tabs
    tabs = ["Testcase", "Analyze"]
    page = st.sidebar.radio("Select a page:", tabs)

    if page == "Testcase":
        tab1()
    else:
        tab2()


if __name__ == '__main__':
    main()

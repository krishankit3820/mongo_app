import streamlit as st
from pymongo import MongoClient
import pandas as pd

# MongoDB connection parameters
CONNECTION_STRING = "your_connection_string"  # Replace with your MongoDB Atlas connection string

# Function to get MongoDB client
def get_client():
    return MongoClient(CONNECTION_STRING)

# Function to fetch data from MongoDB
def fetch_data(database, collection, query={}):
    client = get_client()
    db = client[database]
    collection = db[collection]
    data = list(collection.find(query))
    client.close()
    return data

# Streamlit app
st.title("MongoDB Atlas Data Viewer")

database = st.text_input("Enter Database Name")
collection = st.text_input("Enter Collection Name")
query = st.text_area("Enter Query as JSON")

if st.button("Fetch Data"):
    if database and collection:
        try:
            query_dict = eval(query) if query else {}
            data = fetch_data(database, collection, query_dict)
            df = pd.DataFrame(data)
            st.write(df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter both database and collection names.")

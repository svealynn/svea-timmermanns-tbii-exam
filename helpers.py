import streamlit as st
from hugchat.login import Login
from hugchat import hugchat
import requests
from pymongo.mongo_client import MongoClient

@st.cache_resource
def connect_to_hugging_face():
    hf_email = st.secrets['email']
    hf_pass = st.secrets['password']

    # connect to hugging face
    sign = Login(hf_email, hf_pass)
    cookies = sign.login()

    return cookies


def generate_response(prompt):
    cookies = connect_to_hugging_face()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt)


def get_images(query, api_key, results=10):
    """Code from chatgpt to fetch image URLs based on a query."""
    search_url = "https://api.unsplash.com/search/photos"
    response = requests.get(search_url,
                            params={"query": query.lower(), "client_id": api_key, "per_page": results})
    return [img["urls"]["regular"] for img in response.json().get("results", [])]



@st.cache_resource

def connect_to_mongo():
    #load from secrets.toml file
    db_username = st.secrets["db_username"]
    db_password = st.secrets["db_password"]

    uri = f"mongodb+srv://{db_username}:{db_password}@tb-ii.t0miq.mongodb.net/?retryWrites=true&w=majority&appName=tb-ii"

    # connect to mongodb
    client = MongoClient(uri)

    return client

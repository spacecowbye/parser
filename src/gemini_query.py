import google.generativeai as genai
import streamlit as st


API_KEY1 = st.secrets["google"]["a1"]
API_KEY2 = st.secrets["google"]["a2"]
API_KEY3 = st.secrets["google"]["a3"]
# Define the API keys
API_KEYS = [API_KEY1, API_KEY2, API_KEY3]
api_key_index = 0  # Index to track which API key to use

def get_answer_gemini(prompt):
    ''' Method to get the answer from the Gemini '''
    global api_key_index

    # Configure with the current API key
    genai.configure(api_key=API_KEYS[api_key_index])
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    # Update the index to use the next API key for the next call
    api_key_index = (api_key_index + 1) % len(API_KEYS)

    return response.text

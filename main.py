import os
import streamlit as st
import zipfile
import tempfile
from pyairtable import Api
from src.gemini_query import get_answer_gemini
from src.resume_prompts import get_name, get_email, get_work_experience_resume, get_education_resume, get_phone_number
from utils import get_skills, extract_text_from_pdf

# Load secrets from Streamlit's secrets management
AUTH_TOKEN = st.secrets["airtable"]["auth_token"]
BASE_ID = st.secrets["airtable"]["base_id"]
TABLE_ID = st.secrets["airtable"]["table_id"]

def upload_to_airtable(data):
    """Upload data to Airtable."""
    try:
        api = Api(AUTH_TOKEN)
        table = api.table(BASE_ID, TABLE_ID)
        table.create(data)
        st.success("Data uploaded successfully to Airtable.")
    except Api.ApiError as e:
        st.error("Failed to upload data to Airtable. Please check your API credentials and try again.")
        st.error(f"Airtable API error: {e}")
    except Exception as e:
        st.error("An unexpected error occurred while uploading data to Airtable.")
        st.error(f"Error: {e}")

def process_resume(resume_path, drive_location):
    """Process an individual resume."""
    try:
        # Extract text from the resume
        resume_text = extract_text_from_pdf(resume_path)
        
        # Extract data from resume
        name_string = get_answer_gemini(get_name(resume_text))
        email_string = get_email(resume_text)
        phone_number_string = get_phone_number(resume_text)
        work_exp_string = get_answer_gemini(get_work_experience_resume(resume_text))
        education_string = get_answer_gemini(get_education_resume(resume_text))
        skills_string = ",".join(get_skills(resume_text))

        data = {
            'Name': name_string,
            'Email': email_string,
            'Phone Number': phone_number_string,
            'Work Experience': work_exp_string,
            'Education': education_string,
            'Skills': skills_string,
            'Resume Path': drive_location
        }

        upload_to_airtable(data)
        
        # Remove the processed resume file
        if os.path.exists(resume_path):
            os.remove(resume_path)
            
    except Exception as e:
        st.error(f"Error processing resume {resume_path}.")
        st.error(f"Details: {e}")

def process_resumes_from_zip(zip_path, drive_location):
    """Process multiple resumes from a zip file."""
    try:
        # Create a temporary directory for extracting the zip file
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            for root, _, files in os.walk(temp_dir):
                for filename in files:
                    if filename.endswith(".pdf"):
                        resume_path = os.path.join(root, filename)
                        process_resume(resume_path, drive_location)
                        
    except zipfile.BadZipFile as e:
        st.error("The zip file is corrupted or not a valid zip file.")
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Error processing resumes from zip file: {e}")

def main():
    """Main function to run the Streamlit app."""
    st.title('Resume Processing App')

    try:
        # Get zip file from user input
        uploaded_file = st.file_uploader("Upload a zip file containing resumes (PDF format)", type="zip")

        # Get drive location from user input
        drive_location = st.text_input("Enter the drive folder of the resumes")

        # Process the uploaded zip file
        if uploaded_file and drive_location:
            try:
                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name
                process_resumes_from_zip(tmp_file_path, drive_location)
                st.success("Resume processing complete.")
                os.remove(tmp_file_path)
            except Exception as e:
                st.error(f"Error during file upload or processing: {e}")
        else:
            if not uploaded_file:
                st.warning("Please upload a zip file.")
            if not drive_location:
                st.warning("Please enter the drive folder location.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

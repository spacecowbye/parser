import re
def get_name(resume):
    '''
    Prompt to find the name of the candidate
    '''
    prompt = """
    Extract and return the name of the candidate from the provided resume text. If the name is not found, return 'N/A'.
    Just return the name, nothing else in the response. 
    """
    return prompt + '\n' + resume

def get_work_experience_resume(resume):
    ''' 
    Prompt to find the work experience from the resume 
    '''
    prompt = """
    Extract and return all the job history from the provided resume text. Do not include any additional information. If no job history is found, return 'N/A'. Only output text 
    """
    return prompt + '\n' + resume

def get_education_resume(resume):
    ''' 
    Prompt to find the education from the resume 
    '''
    prompt = """
    Extract and return all degrees, universities from the provided resume text. If no education information is found, return 'N/A'. Only output text
    """
    return prompt + '\n' + resume


def get_email(resume):
    """
    Find email id using regex
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, resume)
    if match:
        return match.group(0)
    else:
        return 'N/A'

def get_phone_number(resume):
    """
    Find phone number using regex
    """
    phone_pattern = r'(\+?\d{1,4}[-.\s]?)?(\(?\d{1,4}\)?[-.\s]?)?[\d\-.\s]{7,}'
    match = re.search(phone_pattern, resume)
    if match:
        return match.group(0)
    else:
        return 'N/A'


    
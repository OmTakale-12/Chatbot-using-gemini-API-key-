import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.title('AstraAI - Your Personal AI Assistant, Anytime, Anywhere!')

# Input API Key
gemini_api_key = st.sidebar.text_input('Gemini API Key', type='password')

#gemini_api_key=AIzaSyC3amubwBsVBmHfMYP3vJSawyBWw-NPUW0

# Configure Gemini API
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

    def generate_response(input_text):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(input_text)
            st.info(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

    with st.form('my_form'):
        text = st.text_area('Enter text:', '...')
        submitted = st.form_submit_button('Submit')

        if not gemini_api_key:
            st.warning('Please enter your Gemini API key!', icon='⚠')
        else:
            generate_response(text)
#radio
st.radio("How much rating out of 5 you give to our app",["1","2","3","4","5"])


#text_area
st.text_area("What improvements should be done in this")

#text
st.text("Thank you for your valuable time and response !")

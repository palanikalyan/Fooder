import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = st.secrets["AIzaSyBzjYd_lcDJz6jzpNho54INTCT4psk58SU"])

model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image):
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text


st.set_page_config(
    page_title="Fooder",
    page_icon="🌟"
)
st.header("✨ Image Insights ✨")
st.markdown("""
This app retrieves the information from the uploaded image and answers your question related to the image using Google Gemini.
""")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
input=st.text_input("Input Prompt (optional): ",key="input")


submit=st.button("Give me insights of the image!")

if submit or input:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)



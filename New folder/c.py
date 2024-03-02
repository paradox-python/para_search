import streamlit as st
import pyautogui as p
import time
from gtts import gTTS
import io
st.set_page_config(
    page_title="Universal Unique", 
    page_icon='🔎',
    layout="wide")
with st.container():
    st.title("Universal Unique")
    st.markdown(
        "<h4 style='text-align: center; color: #3366ff;'>Explore the Universe of Features 🔎</h4>",
        unsafe_allow_html=True,
    )
    
    # Dropdown for selection
    u = st.selectbox("Search Here",["Select Option","Camera","open application","Text Convert Into Voice","Snow","Balloons","Code"])

    # Condition based on selection
    
    if 'snow' in u.lower():
        with st.expander("Snow", expanded=True):
            st.write("Let it snow!")
            while True:
                st.snow()
                time.sleep(4)

    elif 'balloon' in u.lower():
        with st.expander("Balloons", expanded=True):
            st.write("Enjoy the balloons!")
            while True:
                st.balloons()
                time.sleep(2)

    elif 'camera' in u.lower():
        with st.expander("Camera", expanded=True):
            cl, cr = st.columns(2)
            with cl:
                picture = st.camera_input("Take a picture")
            with cr:
                if st.button("Show Photos"):
                    if picture:
                        img = st.image(picture, width=250)
                        st.write("You Can download Photo")
                        st.download_button("Download Now", file_name='image.png', data=picture, mime='image/png')
                    else:
                        st.warning("There are no photos.")

    elif 'code' in u.lower():
        with st.expander("Code Snippet", expanded=True):
            st.code("print('Hello World!')", language="python")
    elif 'text convert into voice' in u.lower():
        with st.expander("Text Convert Into Voice", expanded=True):
            text_input = st.text_input("Enter Text to convert to audio")
            if text_input:
                tts = gTTS(text_input)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                st.audio(audio_bytes, format='audio/mpeg', start_time=0)
                st.download_button(label="Download Audio", data=audio_bytes.getvalue(), file_name='audio.mp3', mime='audio/mp3')
    elif 'open application' in u:
        with st.expander("Enter application name you want to open",expanded=True):
         sea = st.text_input('Enter Here')
         if sea:
          st.write("Opening Application...")
          p.press('win')
          time.sleep(1)
          p.write(sea)
          time.sleep(1)
          p.press('enter')

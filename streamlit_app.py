import streamlit as st
import pandas as pd

# Global variables
DATA_TYPES = ["Table", "Text", "Image", "Video", "Audio"]
FAMOUS_APPS = ["Instagram", "YouTube", "Pinterest", "TikTok", "Spotify", "Netflix", "Twitter", "ChatGPT"]
DATA_TYPES_OF_APPS = ["Image", "Video", "Image", "Video", "Audio", "Video", "Text", "Text"]

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("How is this different from text?")

################################################
################################################
st.header("Part 1 of app - Soul searching")

st.write("I want to build a mini version of a famous app.")
st.write("What apps come to mind?")
apps_table = pd.DataFrame({"App Name": FAMOUS_APPS, "Data Type": DATA_TYPES_OF_APPS})
edited_df = st.data_editor(apps_table, 
                           num_rows="dynamic",
                           use_container_width=True,
                           column_config={
                               "App Name": st.column_config.TextColumn("App Name", help="Name of the app"),
                               "Data Type": st.column_config.SelectboxColumn("Data Type", options=DATA_TYPES, help="Type of data the app uses"),
                           })

################################################
st.write("What is my favourite data type?")
favourite_data_type = None

# favourite_data_type = st.selectbox("Data types", DATA_TYPES)
col1, col2 = st.columns(2)
with col1: 
    while favourite_data_type is None:
        favourite_data_type = st.radio("Data types", DATA_TYPES)

with col2:
    if favourite_data_type:
        st.metric("Favourite data type", favourite_data_type)

################################################

st.write("What is my favourite app that uses this data type?")
favourite_app = None
apps_favourite_type = [app for app, dtype in zip(FAMOUS_APPS, DATA_TYPES_OF_APPS) if dtype == favourite_data_type]
favourite_app = st.selectbox("Apps", apps_favourite_type)


st.write("What is the user value that this data type delivers?")


st.divider()
st.header("Part 2 of app")
table = st.file_uploader("Upload a CSV file", type=["csv"])
text = st.text_area("Describe your app idea in a few sentences", placeholder="My app is a ...")
speech = st.audio_input("Describe your app idea in a few sentences (optional)")
image = st.camera_input("Take a picture of your app idea")
prompt = st.text_input("Describe your app idea in a few sentences (optional)", placeholder="My app is a ...")
if prompt:
    st.write("You entered:", prompt)

clicked = st.button("Completed")
if clicked:
    st.balloons()
    st.write("Thanks for completing the app idea!")
    st.write("You can now download your app idea as a CSV file.")
    st.download_button("Download CSV", edited_df.to_csv(index=False), "app_idea.csv", "text/csv")
 
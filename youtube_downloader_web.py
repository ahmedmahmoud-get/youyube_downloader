import streamlit as st
from pytube import YouTube

""" Ready to deploy. """

styles = """
<style>
[class="css-ue6h4q e1y5xkzn3"] {
display: none;
}
</style>
"""

st.markdown(styles, unsafe_allow_html=True)


urls = st.text_input(
    "", placeholder="Enter youtube urls here, Seperated by comma ,").split(",")
col1, col2 = st.columns([5, 1])
output_path = col1.text_input("", placeholder="Enter output folder path here")
save_btn = col2.button("Download")
condition = save_btn and urls and urls != "" and output_path and output_path != ""
if condition:
    for num, url in enumerate(urls):
        st.write(f"Video number {num + 1} is downloading ...")
        youtube = YouTube(url)
        youtube_download = youtube.streams.get_highest_resolution()
        youtube_download = youtube.streams.get_audio_only()
        youtube_download.download(output_path)
        st.write(
            f"Video {num + 1} - {youtube.title} has been downloaded successfully.")
    st.success("All videos have been downloaded successfully.")

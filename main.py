import streamlit as st
from ultralytics import YOLO
import altair as alt
from pathlib import Path
import tempfile

# Load a model
model = YOLO('yolov8n.pt')  # load an official detection model
 # load a custom model

# Track with the model
sfa = st.file_uploader("", type=['mp4', 'avi', 'mov'])
col1, col2, col3 = st.columns(3)
with col2:
    button_sfa = st.button('Analyse')
if button_sfa:
  with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
              fp = Path(tmp_file.name)
              fp.write_bytes(sfa.getvalue())
  results = model.track(source=tmp_file.name, show=True) 
  video_file = open('myvideo.mp4', 'rb')
  video_bytes = results.read()

  st.video(video_bytes)

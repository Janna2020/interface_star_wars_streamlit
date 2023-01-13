from tkinter.tix import IMAGE
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('STAR WARS')

video_file = open('Video_star.mov', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

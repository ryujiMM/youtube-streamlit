import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("アプリ")
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    time.sleep(0.03)
'Done!!'

expander = st.expander("Q:いつ生まれた？")
expander.write('?')
expander = st.expander("Q:どこで生まれた？")
expander.write('?')
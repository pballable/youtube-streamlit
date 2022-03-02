# cd C:/Users/pballkun/OneDrive/pysamples/Youtube/いまにゅのプログラミング塾/Streamlit
from cv2 import exp
import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(1)

'Done!!!!!'


left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2内容を書く')

expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3内容を書く')
# if st.checkbox('Show Image'):
#     Img = Image.open('主なHTMLタグ.png')
#     st.image(Img , caption='Kohei Imanishi', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：',text,'です。'

# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition





#Write() 表の細かい設定はできない
#dataframe() 表の縦横の長さを指定できる
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
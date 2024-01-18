import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

plt.style.use('ggplot')

data = {
    'num':[x for x in range(1,11)],
    'square':[x**2 for x in range(1,11)],
    'twice':[x*2 for x in range(1,11)],
    'thrice':[x*3 for x in range(1,11)]
}

rad = st.sidebar.radio('Navigation',['Home','About Us'])
if rad == 'Home':
    df = pd.DataFrame(data = data)

    # adding widget
    st.sidebar.selectbox('Select a number ',[1,2,3,4,5])

    col = st.sidebar.multiselect('Select a Column',df.columns)

    plt.plot(df['num'],df[col])
    st.pyplot()

if rad == 'About Us':
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    
    st.write('You are here in about us page')
    st.error('Error')
    st.success('Show Sucess')
    st.info('Information')
    st.exception(RuntimeError('This is an Error'))
    st.warning('This is a warning')

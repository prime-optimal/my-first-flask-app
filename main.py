import streamlit as st
import pandas

data = {
    'Series_1': [1, 3, 4, 5, 7],
    'Series 2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)



st.title('This is Streamlit, baby')
st.subheader('Introducing Streamlit, which is LIT')
st.write('This is our first web app.  And its in python')

st.write(df)
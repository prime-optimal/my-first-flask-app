import streamlit as st
import pandas

data = {
    'Series_1': [1, 3, 4, 5, 7],
    'Series 2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)



st.title('This is Streamlit, baby')
st.subheader('Introducing Tools, which is LIT')
st.write('These streamlit apps should be OBS overlays and plugins')

st.write(df)
st.line_chart(df)

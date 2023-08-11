import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('H')

st.title('10 most common explanations on the Streamlit forum')
st.subheader('Example code')

st.write('This is a collection of code snippets from a [Streamlit Blog]'\
         '(https://blog.streamlit.io/10-most-common-explanations-on-the-streamlit-forum) '\
         'post.')

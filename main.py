import streamlit
#display or write something on to the streamlit.write()
streamlit.write("hello!")
st.write("<h1>Hello world</h1>",unsafe_allow_html=True)
#ing colour of test
st.write("<h1ss style='color:red;'>hello world</h1>",unsafe_allow_html=True)
st.file_uploader("upload file")

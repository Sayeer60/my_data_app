import streamlit as st
st.header("Hello! My name is Sayeer Ahmed")
st.snow()
name = st.text_input(" ","enter your name")
clk_btn=st.button("click here")
if clk_btn==True:
    st.header("wellcome to my data app mr. "+name)
   

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
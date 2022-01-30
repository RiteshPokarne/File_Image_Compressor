from huffman import HuffmanCoding
from img import image
import sys
import streamlit as st






st.set_page_config(layout = "wide")

st.title("File and Image Compressor")
st.markdown("*")

col1,col2,col3,col4,col5 = st.columns([0.5,2,2,2,0.5])
col1.text("")
col5.text("")

if col2.checkbox('File Compression', value = False):
    i = col2.text_input("File Path: ", key="File")
    if col2.button('Compress File', key="File"):
        h = HuffmanCoding(i)
        output_path = h.compress()




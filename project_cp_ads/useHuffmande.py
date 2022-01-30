from huffman import HuffmanCoding
from img import image
import sys
import streamlit as st






st.set_page_config(layout = "wide")

st.title("File  Decompressor")
st.markdown("*")

col1,col2,col3,col4,col5 = st.columns([0.5,2,2,2,0.5])
col1.text("")
col5.text("")



if col2.checkbox('File Decompression', value = False):
    j = col2.text_input("File Path: ", key="File_decomp")
    if col2.button('Decompress File', key="File_decomp"):
        h = HuffmanCoding(j)
        output_path = h.compress()
       
        decom_path = h.decompress(output_path)





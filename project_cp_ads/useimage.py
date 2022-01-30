from huffman import HuffmanCoding
from img import image
import sys
import streamlit as st



# path = "sample.txt"

# h = HuffmanCoding(path)

# output_path = h.compress()
# print("Compressed file path: " + output_path)

# decom_path = h.decompress(output_path)
# print("Decompressed file path: " + decom_path)

# path_img = "lena.png"

# i=image(path_img)


# i.compress_img()


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

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


if col3.checkbox('File Decompression', value = False):
    j = col3.text_input("File Path: ", key="File_decomp")
    if col3.button('Decompress File', key="File_decomp"):
        h = HuffmanCoding(j)
        decom_path = h.decompress(j)

if col4.checkbox('Image Compression', value = False):
    k = col4.text_input("Image Path: ", key="Image")
    if col4.button('Compress Image', key="Image"):
        img_=image(k)
        img_.compress_img()


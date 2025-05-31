import streamlit as st

st.title("🎈hai welcome to pethouse")
st.write(
    "ngoding seru bersama ayu dewi"
)
st.image("1dc14417c4032a266dbacc8fe2dd05b0.jpg", width=200)

st.tittle("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka

if (angka % 2) == 0:
    st.write(f"(angka) adalah Bilangan Genap")
else :
    st.write(f"(angka) adalah Bilangan Ganjil") -!

st.title("pethouse always miaw miaw") 
st.header("Aplikasi menilai ganjil/genap") 
angka= st.number_input("70:", value=0, step=1) 

if(angka % 2) == 0:
  st.write(f"{2,4,6,8,10} adalah jumlah angka genap") 
else:
  st.write(f"{1,3,5,7,9} adalah jumlah angka ganjil")


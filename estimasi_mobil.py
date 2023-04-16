import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('input tahun mobil')
mileage = st.number_input('input km Mobil')
tax = st.number_input('input pajak mobil')
mpg = st.number_input('input Konsumsi BBM Mobil')
engineSize = st.number_input('input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi Harga Mobil Bekas Dalam Ponds : ', predict)
    st.write ('Estimasi Harga Mobil Bekas Dalam IDR (Juta) : ', predict*19000)

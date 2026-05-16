import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
try:
    with open('model_mobil.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("File 'model_mobil.pkl' tidak ditemukan di folder yang sama!")

st.set_page_config(page_title="Car Price Predictor", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #28a745; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #218838; color: white; }
    .result-card { background-color: #fff9c4; padding: 20px; border-radius: 15px; border: 2px solid #fbc02d; text-align: center; margin-bottom: 20px; }
    .info-card { background-color: #072942; padding: 20px; border-radius: 15px; border: 2px solid #2196f3; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Judul utama yang sudah diatur rata tengah
st.markdown("<h1 style='text-align: center;'>Sistem Prediksi Harga Manufaktur Mobil</h1>", unsafe_allow_html=True)
st.write("---")

col_kiri, col_kanan = st.columns([1, 1], gap="large")

with col_kiri:
    st.markdown("### 📝 Input Spesifikasi")
    with st.container():
        # Membagi inputan menjadi 2 sub-kolom berjejer (Kiri & Kanan)
        sub_col1, sub_col2 = st.columns(2)
        
        with sub_col1:
            v1 = st.text_input("Engine Size (L)", placeholder="e.g. 2.0")
            v3 = st.text_input("Wheelbase (inch)", placeholder="e.g. 105")
            v5 = st.text_input("Length (inch)", placeholder="e.g. 180")
            v7 = st.text_input("Fuel Capacity (gal)", placeholder="e.g. 15")
            
        with sub_col2:
            v2 = st.text_input("Horsepower (HP)", placeholder="e.g. 150")
            v4 = st.text_input("Width (inch)", placeholder="e.g. 70")
            v6 = st.text_input("Curb Weight (ton)", placeholder="e.g. 1.5")
            v8 = st.text_input("Fuel Efficiency (mpg)", placeholder="e.g. 28")
        
        # Tombol tetap di bawah, melebar penuh melewati kedua sub-kolom
        st.write("") # Kasih sedikit jarak kosong
        hitung = st.button("HITUNG HARGA MOBIL")

with col_kanan:
    st.markdown("### 📊 Hasil Analisis")
    
    if hitung:
        try:
            # Konversi input teks ke float agar bisa diproses model AI
            inputs = [float(x) for x in [v1, v2, v3, v4, v5, v6, v7, v8]]
            
            input_data = np.array([inputs])
            prediksi = model.predict(input_data)[0]
            
            # Tampilan Hasil (Kotak Kuning sesuai coretan dosen)
            st.markdown(f"""
                <div class="result-card">
                    <p style="margin:0; font-size: 1.2rem; color: #856404; font-weight: bold;">PERKIRAAN HARGA JUAL</p>
                    <h1 style="color: #fbc02d; font-size: 3.5rem; margin:0;">${prediksi:.3f}</h1>
                    <p style="color: #856404;">(dalam ribuan USD)</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Detail Spesifikasi Input yang Benar & Sesuai nama asli variabel
            st.write("#### Detail Spesifikasi Input:")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Engine Size:** {v1} L")
                st.write(f"**Horsepower:** {v2} HP")
                st.write(f"**Wheelbase:** {v3} in")
                st.write(f"**Width:** {v4} in")
            with col_b:
                st.write(f"**Length:** {v5} in")
                st.write(f"**Curb Weight:** {v6} ton")
                st.write(f"**Fuel Capacity:** {v7} gal")
                st.write(f"**Fuel Efficiency:** {v8} mpg")
                
        except ValueError:
            st.error("⚠️ Pastikan semua kolom diisi dengan angka dan tidak boleh ada yang kosong!")
        except Exception as e:
            st.error(f"Terjadi kesalahan teknis: {e}")
            
    else:
        st.info("Silakan isi data spesifikasi di sebelah kiri dan klik tombol untuk melihat hasil prediksi.")

    # Kotak Biru Identitas (Teks Putih & Terang agar terbaca jelas)
    st.markdown(f"""
        <div class="info-card" style="margin-top: 30px;">
            <p style="margin:0; font-weight: bold; color: #4dabf7; font-size: 1.1rem;">SISTEM INI DIBUAT OLEH:</p>
            <p style="margin:5px 0 0 0; font-size: 1rem;">NAMA : <b>SEKAR AYU FATMASARI</b></p>
            <p style="margin:3px 0 0 0; font-size: 1rem;">NPM : <b>237006054</b></p>
        </div>
    """, unsafe_allow_html=True)
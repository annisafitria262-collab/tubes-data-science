import streamlit as st
import pandas as pd
import joblib
import os
import time

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Prediksi Kualitas Tidur",
    page_icon="😴",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================
st.markdown("""
<style>
.main { padding-top: 1rem; }
.title-box { 
    background: linear-gradient(135deg,#1e3a8a,#0d9488); 
    padding: 25px; 
    border-radius: 15px; 
    text-align:center; 
    margin-bottom:20px; 
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15); 
}
.title-box h1{ color:white; margin:0; }
.title-box p{ color:white; margin-top:8px; }
.stButton > button { 
    width:100%; 
    border-radius:12px; 
    height:50px; 
    font-size:18px; 
    font-weight:bold; 
}
</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================
st.markdown("""
<div class="title-box">
    <h1>🩺 AI Sleep Quality Predictor</h1>
    <p>Analisis kualitas tidur berdasarkan aktivitas harian Anda</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# LOAD MODEL
# =====================================
@st.cache_resource
def load_pipeline():
    path = "models/model_final.pkl"
    if not os.path.exists(path): return None
    return joblib.load(path)

pipeline = load_pipeline()
if pipeline is None:
    st.error("❌ File model_final.pkl tidak ditemukan di folder models")
    st.stop()

# =====================================
# POPUP HASIL
# =====================================
@st.dialog("🧠 Hasil Analisis AI")
def tampilkan_hasil(status, tips):
    if status == "baik":
        st.balloons()
        st.success("🎉 KUALITAS TIDUR BAIK!")
        st.markdown("""
        # 😴✨🏆
        ### Hebat!
        Pola tidurmu menunjukkan kondisi yang sehat. Pertahankan kebiasaan baik ini ya 💪
        """)
        if os.path.exists("assets/happy_sleep.gif"):
            st.image("assets/happy_sleep.gif", width=280)
        st.info("🌟 AI menilai kualitas tidurmu dalam kondisi baik. Tetap konsisten dan pertahankan pola hidup sehat!")
        st.markdown("""
        ### 🎯 Apresiasi Untuk Kamu
        ✅ Pola tidurmu cukup baik
        ✅ Aktivitas harianmu mendukung kualitas istirahat
        ✅ Pertahankan kebiasaan positif ini
        🏆 Good Job!
        """)
    else:
        st.snow()
        st.error("😵‍💫 KUALITAS TIDUR KURANG BAIK")
        st.markdown("""
        # 🌙😟💤
        ### Jangan Khawatir
        Hasil ini bukan diagnosis medis. Kualitas tidur masih bisa diperbaiki secara bertahap.
        """)
        if os.path.exists("assets/insomnia.gif"):
            st.image("assets/insomnia.gif", width=280)
        st.warning("💡 Saran Personal Untuk Kamu")
        if len(tips) == 0:
            st.info("Cobalah menjaga konsistensi waktu tidur dan mengurangi aktivitas sebelum tidur.")
        for tip in tips:
            st.info(tip)
        st.markdown("""
        ### 🌙 Langkah Kecil Yang Bisa Dicoba
        ✅ Tidur dan bangun pada jam yang sama
        ✅ Kurangi screen time sebelum tidur
        ✅ Kurangi konsumsi kafein malam hari
        ✅ Kelola stres dengan relaksasi atau olahraga ringan
        💪 Sedikit perubahan bisa memberi dampak besar.
        """)
    st.divider()
    st.caption("🤖 Analisis dilakukan menggunakan model Machine Learning Decision Tree")

# =====================================
# FORM INPUT
# =====================================
with st.form("form_prediksi"):
    st.subheader("📝 Data Aktivitas Harian")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Usia", min_value=15, max_value=80, value=25, step=1)
        gender = st.selectbox("Jenis Kelamin", ["Female", "Male"])
        occupation = st.selectbox("Pekerjaan", ["Designer", "Doctor", "Freelancer", "Manager", "Researcher", "Software Engineer", "Student", "Teacher"])
        sleep_duration_hours = st.number_input("Durasi Tidur (Jam)", min_value=1, max_value=24, value=7, step=1)
        phone_usage = st.number_input("Penggunaan HP Sebelum Tidur (Menit)", min_value=0, max_value=300, value=30, step=1)
        daily_screen = st.number_input("Screen Time Harian (Jam)", min_value=0, max_value=24, value=5, step=1)

    with col2:
        stress_level = st.slider("Level Stres (1: Santai - 10: Depresi)", 1, 10, 5, help="1: Stres biasa saja | 10: Depresi")
        mental_fatigue = st.slider("Kelelahan Mental (1: Segar - 10: Sangat Lelah)", 1, 10, 3, help="1: Sangat Segar | 10: Sangat Lelah Mental")
        physical_activity = st.number_input("Aktivitas Fisik (Menit)", min_value=0, max_value=300, value=45, step=1)
        caffeine = st.number_input("Konsumsi Kafein (Gelas)", min_value=0, max_value=10, value=1, step=1)
        notifications = st.number_input("Jumlah Notifikasi per Hari", min_value=0, max_value=500, value=50, step=1)

    submit = st.form_submit_button("🔍 Analisis Kualitas Tidur")

# =====================================
# PREDIKSI
# =====================================
if submit:
    data_input = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "occupation": [occupation],
        "daily_screen_time_hours": [float(daily_screen)],
        "phone_usage_before_sleep_minutes": [float(phone_usage)],
        "sleep_duration_hours": [float(sleep_duration_hours)],
        "stress_level": [float(stress_level)],
        "caffeine_intake_cups": [float(caffeine)],
        "physical_activity_minutes": [float(physical_activity)],
        "notifications_received_per_day": [float(notifications)],
        "mental_fatigue_score": [float(mental_fatigue)]
    })

    try:
        with st.spinner("🧠 AI sedang menganalisis pola tidur Anda..."):
            time.sleep(2)
            hasil = pipeline.predict(data_input)
            
        tips = []
        if stress_level >= 7: tips.append("🧘 Tingkat stres cukup tinggi. Cobalah relaksasi sebelum tidur.")
        if daily_screen >= 8: tips.append("📱 Kurangi screen time minimal 1 jam sebelum tidur.")
        if caffeine >= 3: tips.append("☕ Hindari konsumsi kafein pada malam hari.")
        if sleep_duration_hours < 6: tips.append("😴 Durasi tidur masih kurang dari rekomendasi 7–9 jam.")
        if phone_usage > 90: tips.append("📵 Penggunaan HP sebelum tidur cukup tinggi.")
        if notifications > 150: tips.append("🔔 Notifikasi berlebihan dapat meningkatkan distraksi.")

        if hasil[0] == 0:
            tampilkan_hasil("baik", tips)
        else:
            tampilkan_hasil("buruk", tips)

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat prediksi: {e}")
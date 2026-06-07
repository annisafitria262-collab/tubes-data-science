import streamlit as st

st.set_page_config(page_title="SVM Performance", layout="wide")

# Panggil file CSS eksternal khusus milik SVM (Kunci Desain & Warna Identik)
with open("assets/svm.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
    <div class="slide-header">
        <h1>Strategic Deep Dive: <span>Support Vector Machine</span> Analytics</h1>
        <p>Analisis Optimasi Hyperplane Berdimensi Tinggi dan Kestablian Klasifikasi Linear (Aqila)</p>
    </div>
""", unsafe_allow_html=True)

# --- SEKSI KPI METRICS (Angka Riil SVM) ---
st.markdown('<div class="slide-section-title">Quantitative Performance Benchmark</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-value">87.67%</div>
            <div class="kpi-label">Akurasi Global</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">43.13%</div>
            <div class="kpi-label">Presisi Kelas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">68.09%</div>
            <div class="kpi-label">Recall / Sensitivitas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">0.5281</div>
            <div class="kpi-label">F1-Score Harmonik</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- GRID DUA KOLOM KONTEN ---
col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    # Dibungkus utuh dalam satu blok string HTML agar rigid dan aman dari kotak hantu melar
    st.markdown("""
        <div class="chart-card-clean">
            <h3>📈 F1-Score Reliability Comparison (Data Test)</h3>
            <div class="static-chart-box">
                <div class="chart-row">
                    <div class="chart-label">K-NN (Zahara)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 45.6%;">45.65%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">SVM (Aqila)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill winner" style="width: 52.8%;">52.81%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">Neural Network (Athaya)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 53.1%;">53.13%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">Decision Tree (Anisa)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 87.7%;">87.77%</div></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class="chart-card-clean">
            <h3>💡 Analisis Ruang Fitur & Hyperplane</h3>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Model <b>Support Vector Machine</b> (SVM) mencatatkan keunggulan kestabilan di awal fase pengujian murni, 
                berhasil meraup nilai <b>Global Accuracy tertinggi sebesar 87.67%</b> di antara seluruh model.
            </p>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Meskipun akurasi globalnya mendominasi, nilai metrik penyeimbang murni (F1-Score) miliknya tertahan di angka <b>52.81%</b>. Hal ini dikarenakan batas pemisahan linear belum sepenuhnya fleksibel memisahkan data yang bertumpuk tebal.
            </p>
            <div class="status-callout">
                📌 <b>Karakteristik Model:</b> Kemampuan SVM mengunci margin pembatas (*hyperplane*) optimal memberikan kestabilan prediksi global yang sangat konsisten, menjadikannya model alternatif berakurasi tinggi yang sangat solid.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SEKSI TABEL COMPARATIVE (Highlight Pindah ke Baris SVM) ---
st.markdown('<div class="slide-section-title">Comparative Performance Matrix</div>', unsafe_allow_html=True)

st.markdown("""
    <table class="clean-table">
        <thead>
            <tr>
                <th>Algoritma Eksperimen</th>
                <th>Accuracy</th>
                <th>Precision</th>
                <th>Recall</th>
                <th>F1-Score Final</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>K-Nearest Neighbors (Zahara)</td>
                <td>84.60%</td>
                <td>35.53%</td>
                <td>63.82%</td>
                <td>0.4565</td>
            </tr>
            <tr class="winner-row">
                <td>🛡️ Support Vector Machine (Aqila)</td>
                <td>87.67%</td>
                <td>43.13%</td>
                <td>68.09%</td>
                <td>0.5281</td>
            </tr>
            <tr>
                <td>Neural Network (Athaya)</td>
                <td>87.00%</td>
                <td>41.86%</td>
                <td>72.70%</td>
                <td>0.5313</td>
            </tr>
            <tr>
                <td>Decision Tree (Anisa)</td>
                <td>85.87%</td>
                <td>91.52%</td>
                <td>85.87%</td>
                <td>0.8777</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- EXPANDER DETAIL ---
with st.expander("🛠️ Detail Pengaturan Parameter & Kernel SVM"):
    st.markdown("""
    * **Fungsi Kernel:** Pemanfaatan fungsi kernel (seperti RBF atau Linear) untuk memetakan sebaran pola tidur ke dalam ruang dimensi yang lebih tinggi.
    * **Parameter Regularisasi (C):** Konfigurasi bobot penalti dioptimalkan guna menyeimbangkan margin pembatas kelas dan meminimalkan galat klasifikasi pada data latih.
    * **Sifat Batas:** Sangat kokoh terhadap pengaruh data pencilan (*outliers*) yang berada jauh dari garis batas tepi *support vectors*.
    """)
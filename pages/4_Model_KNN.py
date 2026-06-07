import streamlit as st

st.set_page_config(page_title="KNN Performance", layout="wide")

# PANGGIL KUNCI: Pakai file CSS milik Decision Tree agar UI & warna kembar identik 100%
with open("assets/decision.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER BANNER (Warna & Bentuk Sama Persis) ---
st.markdown("""
    <div class="slide-header">
        <h1>Strategic Deep Dive: <span>K-Nearest Neighbors</span> Analytics</h1>
        <p>Analisis Spasial Data Berbasis Kalkulasi Kedekatan Jarak Metrik Variabel (Zahara)</p>
    </div>
""", unsafe_allow_html=True)

# --- SEKSI KPI METRICS (Angka Riil KNN) ---
st.markdown('<div class="slide-section-title">Quantitative Performance Benchmark</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-value">84.60%</div>
            <div class="kpi-label">Akurasi Global</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">35.53%</div>
            <div class="kpi-label">Presisi Kelas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">63.82%</div>
            <div class="kpi-label">Recall / Sensitivitas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">0.4565</div>
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
                    <div class="chart-bar-bg"><div class="chart-bar-fill winner" style="width: 45.6%;">45.65%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">SVM (Aqila)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 52.8%;">52.81%</div></div>
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
            <h3>💡 Karakteristik Spasial & Kedekatan Jarak</h3>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Model <b>K-Nearest Neighbors</b> (K-NN) dilatih dengan mengukur kedekatan spasial antar sampel data tidur. 
                Melalui pengujian murni, organisasi algoritma ini menembus nilai <b>Global Accuracy sebesar 84.60%</b>.
            </p>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Meskipun akurasi globalnya bersaing, nilai F1-Score harmoniknya tertahan di angka <b>45.65%</b>. K-NN sangat sensitif terhadap representasi kerapatan dimensi data, sehingga variasi fitur non-linear memerlukan batasan skala jarak yang jauh lebih ketat agar klasifikasi lokal tidak bias.
            </p>
            <div class="status-callout">
                📌 <b>Karakteristik Model:</b> Sebagai model berbasis instans murni (*instance-based learning*), K-NN sangat bergantung pada normalisasi skala data. Model ini memberikan wawasan penting tentang bagaimana kemiripan jarak fitur memengaruhi penentuan kualitas tidur kelompok.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SEKSI TABEL COMPARATIVE (Highlight Pindah ke Baris K-NN) ---
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
            <tr class="winner-row">
                <td>📈 K-Nearest Neighbors (Zahara)</td>
                <td>84.60%</td>
                <td>35.53%</td>
                <td>63.82%</td>
                <td>0.4565</td>
            </tr>
            <tr>
                <td>Support Vector Machine (Aqila)</td>
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
with st.expander("🛠️ Detail Pengaturan Jarak & Nilai Parameter K"):
    st.markdown("""
    * **Metrik Pengukuran Jarak:** Perhitungan kemiripan antar sample fitur kualitas tidur dihitung menggunakan kalkulasi metrik jarak murni seperti *Euclidean* atau *Manhattan Distance*.
    * **Penentuan Konstanta K:** Optimasi jumlah tetangga terdekat ($K$) dikunci menggunakan skema pencarian cross-validation guna meredam efek *noise* lokal data.
    * **Skalabilitas Fitur:** Membutuhkan penanganan standardisasi fitur yang ketat agar variabel dengan satuan besar tidak mendominasi kalkulasi ruang spasial.
    """)
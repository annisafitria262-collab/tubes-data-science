import streamlit as st

st.set_page_config(page_title="Neural Network Performance", layout="wide")

# Panggil file CSS eksternal khusus milik Neural Network
with open("assets/network.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
    <div class="slide-header">
        <h1>Strategic Deep Dive: <span>Neural Network</span> Analytics</h1>
        <p>Eksplorasi Arsitektur Multi-Layer Perceptron dan Analisis Batas Klasifikasi Jaringan (Athaya)</p>
    </div>
""", unsafe_allow_html=True)

# --- SEKSI KPI METRICS ---
st.markdown('<div class="slide-section-title">Quantitative Performance Benchmark</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-value">87.00%</div>
            <div class="kpi-label">Akurasi Global</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">41.86%</div>
            <div class="kpi-label">Presisi Kelas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">72.70%</div>
            <div class="kpi-label">Recall / Sensitivitas</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-value">0.5313</div>
            <div class="kpi-label">F1-Score Harmonik</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- GRID DUA KOLOM KONTEN ---
col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    # FIX TOTAL: Seluruh komponen grafik dibungkus utuh dalam satu blok string HTML agar tidak bocor layout
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
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 52.8%;">52.81%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">Neural Network (Athaya)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill winner" style="width: 53.1%;">53.13%</div></div>
                </div>
                <div class="chart-row">
                    <div class="chart-label">Decision Tree (Anisa)</div>
                    <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 87.7%;">87.77%</div></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # FIX TOTAL: Sisi kanan juga disatukan utuh blok HTML-nya biar adem sejajar
    st.markdown("""
        <div class="chart-card-clean">
            <h3>💡 Jaringan Saraf & Batas Prediksi</h3>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Model <b>Neural Network</b> yang dikembangkan menggunakan arsitektur <i>Multi-Layer Perceptron</i> (MLP) 
                berhasil mencatatkan Akurasi Global yang tinggi sebesar <b>87.00%</b>.
            </p>
            <p style="font-size: 0.9rem; color: #475569; margin-bottom: 12px; line-height: 1.6;">
                Meskipun demikian, jika diperhatikan nilai Presisinya tertahan di angka <b>41.86%</b>. Hal ini menunjukkan bahwa jaringan saraf tiruan cenderung menghasilkan banyak *False Positive* saat memisahkan sinyal kelas minoritas pada data pengujian murni.
            </p>
            <div class="status-callout">
                ⚠️ <b>Evaluasi Arsitektur:</b> Tingginya nilai ROC-AUC (0.9197) mengonfirmasi bahwa model memiliki kapasitas pemisahan yang kuat, namun memerlukan optimasi ambang batas (*threshold tuning*) yang lebih ketat agar nilai F1-Score murni dapat bersaing dengan Decision Tree.
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SEKSI TABEL COMPARATIVE ---
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
            <tr>
                <td>Support Vector Machine (Aqila)</td>
                <td>87.67%</td>
                <td>43.13%</td>
                <td>68.09%</td>
                <td>0.5281</td>
            </tr>
            <tr class="winner-row">
                <td>🧠 Neural Network (Athaya)</td>
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

# --- EXPANDER DETAIL (Murni Bawaan Streamlit Tanpa HTML Kustom) ---
with st.expander("🛠️ Detail Arsitektur & Koneksi Layer MLP"):
    st.markdown("""
    * **Hidden Layer Configuration:** Menggunakan kombinasi neuron tersembunyi yang dilatih dengan optimasi fungsi loss.
    * **Fungsi Aktivasi:** Penerapan fungsi non-linear (seperti ReLU atau Logistic) untuk menangkap interaksi kompleks antar fitur pola tidur.
    * **Skema Regularisasi:** Pembatasan bobot diaplikasikan untuk meredam kecenderungan overfitting selama proses propagasi balik (*backpropagation*).
    """)
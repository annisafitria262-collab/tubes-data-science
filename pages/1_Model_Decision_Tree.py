import streamlit as st

st.set_page_config(page_title="Decision Tree Analytics", layout="wide")

# Panggil file CSS eksternal khusus milik Decision Tree
with open("assets/decision.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
    <div class="slide-header">
        <h1>Strategic Deep Dive: <span>Decision Tree</span> Analytics</h1>
        <p>Optimasi Arsitektur dan Evaluasi Kuantitatif Model Terbaik Kelompok (Anisa)</p>
    </div>
""", unsafe_allow_html=True)

# --- SEKTI KPI METRICS ---
st.markdown('<div class="slide-section-title">Quantitative Performance Benchmark</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card highlight-border">
            <div class="kpi-value">85.87%</div>
            <div class="kpi-label">Akurasi Global</div>
        </div>
        <div class="kpi-card highlight-border">
            <div class="kpi-value">91.52%</div>
            <div class="kpi-label">Presisi Kelas</div>
        </div>
        <div class="kpi-card highlight-border">
            <div class="kpi-value">85.87%</div>
            <div class="kpi-label">Recall / Sensitivitas</div>
        </div>
        <div class="kpi-card highlight-border">
            <div class="kpi-value">0.8777</div>
            <div class="kpi-label">F1-Score Harmonik</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- GRID DUA KOLOM CONTEN ---
col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.markdown('<h3>📈 F1-Score Reliability Comparison (Data Test)</h3>', unsafe_allow_html=True)
    
    # GRAFIK PURBAKALA KUSTOM CSS (100% AMAN DARI BUG ZOOM/SCROLL MOUSE)
    st.markdown("""
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
                <div class="chart-bar-bg"><div class="chart-bar-fill" style="width: 53.1%;">53.13%</div></div>
            </div>
            <div class="chart-row">
                <div class="chart-label">Decision Tree (Anisa)</div>
                <div class="chart-bar-bg"><div class="chart-bar-fill winner" style="width: 87.7%;">87.77%</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.markdown('<h3>💡 Setting the Group Benchmark</h3>', unsafe_allow_html=True)
    st.markdown("""
    Berbeda dengan algoritma berbasis jarak spasial (K-NN) atau pemisahan linear (SVM), 
    <b>Decision Tree</b> bekerja lewat pembagian partisi data secara lokal (recursive partitioning). 
    <br><br>
    Strategi ini terbukti sangat sukses mengenali pola non-linear pada dataset kesehatan tidur kelompok kita, 
    serta berhasil meredam efek ketimpangan kelas target setelah dikombinasikan dengan metode SMOTE.
    """)
    
    st.markdown("""
        <div class="status-callout">
            <b>Rekomendasi Utama:</b> Berdasarkan capaian F1-Score (0.8777) yang unggul telak di atas rata-rata kelompok, 
            arsitektur pohon keputusan ini resmi dikunci ke dalam file <b>model.pkl</b> sebagai mesin penggerak utama.
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
            <tr>
                <td>Neural Network (Athaya)</td>
                <td>87.00%</td>
                <td>41.86%</td>
                <td>72.70%</td>
                <td>0.5313</td>
            </tr>
            <tr class="winner-row">
                <td>🌳 Decision Tree (Anisa)</td>
                <td>85.87%</td>
                <td>91.52%</td>
                <td>85.87%</td>
                <td>0.8777</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)

# --- EXPANDER DETAIL ---
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("🛠️ Detail Metodologi & Spesifikasi Hyperparameter Tuning"):
    st.markdown("""
    * **Pencarian Parameter:** GridSearchCV dioptimalkan dengan skema 10-Fold Cross Validation.
    * **Kriteria Cabang:** Pengujian berbasis indeks ketidakmurnian Gini (*Gini Impurity*) dan perolehan informasi (*Entropy*).
    * **Penanganan Imbalance:** Data di-resampling penuh menggunakan sintesis sampel minoritas (SMOTE) sebelum fase pelatihan lokal.
    """)
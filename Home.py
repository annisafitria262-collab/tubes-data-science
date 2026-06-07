import streamlit as st

st.set_page_config(page_title="Sleep Analytics - Home", layout="wide")

# Memuat file penata gaya responsif assets/home.css
with open("assets/home.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- 1. HERO BANNER INTERNASIONAL ---
st.markdown("""
    <div class="global-hero-wrapper">
        <div class="global-hero-tag">Tugas Besar Data Science Kelompok</div>
        <div class="global-hero-title">Elevating Sleep Quality<br>Through Multi-Architecture Classification</div>
        <div class="global-hero-subtitle">Eksperimen komparatif tingkat tinggi oleh Team Jobes dalam mengekstrak wawasan prediktif efisiensi istirahat manusia berbasis algoritma cerdas.</div>
    </div>
""", unsafe_allow_html=True)

# --- 2. ROSTER PERKENALAN TIM (RESPONSIF TEPAT DI BAWAH HERO) ---
st.markdown("""
    <div class="international-team-grid">
        <div class="glass-member-card">
            <div class="member-identity">Zahara</div>
            <div class="member-assignment">K-Nearest Neighbors</div>
        </div>
        <div class="glass-member-card">
            <div class="member-identity">Anisa</div>
            <div class="member-assignment">Decision Tree</div>
        </div>
        <div class="glass-member-card">
            <div class="member-identity">Athaya</div>
            <div class="member-assignment">Neural Network</div>
        </div>
        <div class="glass-member-card">
            <div class="member-identity">Aqila</div>
            <div class="member-assignment">Support Vector Machine</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 3. BARIS PERTAMA: PENJELASAN LATAR BELAKANG & DEFINISI DATASET DETAIL ---
col_background, col_dataset = st.columns([1.1, 0.9], gap="large")

with col_background:
    st.markdown("""
        <div class="chart-card-clean">
            <h3>🎯 Latar Belakang & Urgensi Penelitian Masalah</h3>
            <p>
                Kualitas efisiensi istirahat malam merupakan parameter krusial yang menentukan stabilitas fisiologis, 
                fokus kognitif, dan produktivitas harian manusia. Pola interaksi multivariat antara durasi tidur, 
                ritme denyut jantung harian, dan akumulasi tingkat stres psikologis sering kali membentuk relasi non-linear 
                yang tidak dapat ditarik kesimpulannya menggunakan statistik deskriptif konvensional.
                <br><br>
                Oleh karena itu, platform analisis ini dikembangkan oleh kelompok kami guna mengekstrak wawasan prediktif dari kompleksitas 
                faktor-faktor perilaku harian tersebut. Dengan memanfaatkan data riil hasil pengujian empiris (<b>bukan simulasi data dummy</b>), 
                proyek ini memfasilitasi penemuan model kecerdasan buatan paling presisi yang siap diintegrasikan ke dalam arsitektur sistem utama sistem produksi aplikasi.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_dataset:
    st.markdown("""
        <div class="chart-card-clean">
            <h3>📊 Dataset Definition & Task Classification Specification</h3>
            <p>
                Eksperimen komparatif kelompok kami secara tegas dispesifikasikan untuk menyelesaikan <b>Tugas Klasifikasi Supervised Multivariat</b>, 
                dan bukan merupakan analisis regresi numerik kontinuitas. Algoritma dioptimalkan menggunakan label target biner guna memisahkan 
                kondisi kenyamanan tidur pengguna ke dalam dua kategori mutlak, yaitu:
            </p>
            <p style="font-size:0.85rem; color:#475569; line-height:1.6; margin-top:10px;">
                • <b>Kelas Target Terikat (Labels):</b> <i>Comfortable Sleep</i> (Tidur Berkualitas) atau <i>Uncomfortable Sleep</i> (Tidur Tidak Nyaman).<br>
                • <b>Atribut Fitur Pengukuran (Prediktor):</b> Atribut numerik riil mencakup <i>Sleep Duration</i> (jam), <i>Heart Rate</i> (bpm), <i>Stress Level</i>, <i>Physical Activity Level</i>, dan <i>Daily Steps</i>.<br>
                • <b>Integritas Distribusi Data:</b> Seluruh sampel telah melalui tahapan normalisasi fitur serta penyeimbangan kelas menggunakan teknik SMOTE over-sampling guna memitigasi bias klasifikasi pada model algoritma.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. BARIS KEDUA: TABEL MATRIKS LEADERBOARD & DIAGRAM NATIVE POHON ANISA ---
st.markdown('<div class="slide-section-title">Global Performance Evaluation & Real Decision Tree</div>', unsafe_allow_html=True)
col_table, col_tree = st.columns([1.1, 0.9], gap="large")

with col_table:
    st.markdown("""
        <div class="clean-table-wrapper">
            <table class="clean-table">
                <thead>
                    <tr>
                        <th>Machine Learning Model</th>
                        <th>Accuracy</th>
                        <th>Precision</th>
                        <th>Recall</th>
                        <th>F1-Score Final</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>K-Nearest Neighbors (Zahara)</td><td>84.60%</td><td>35.53%</td><td>63.82%</td><td>0.4565</td></tr>
                    <tr><td>Support Vector Machine (Aqila)</td><td>87.67%</td><td>43.13%</td><td>68.09%</td><td>0.5281</td></tr>
                    <tr><td>Neural Network (Athaya)</td><td>87.00%</td><td>41.86%</td><td>72.70%</td><td>0.5313</td></tr>
                    <tr class="winner-row">
                        <td>🌳 Decision Tree (Anisa) <span class="badge-winner">CHAMPION</span></td>
                        <td>85.87%</td>
                        <td>91.52%</td>
                        <td>85.87%</td>
                        <td>0.8777</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="status-callout">
            🏆 <b>Rekomendasi Utama Model Produksi:</b><br>
            Berdasarkan evaluasi kuantitatif kelompok kami, model <b>Decision Tree (Anisa)</b> resmi dipilih sebagai arsitektur final. Model ini mencatatkan nilai <b>Harmonic F1-Score tertinggi sebesar 0.8777</b>, membuktikan ketajaman mutlak arsitektur pohon keputusan dalam menangani data imbalance dan memetakan aturan percabangan kelas target setelah dikombinasikan dengan metode HPO SMOTE ($n = 21.564 \text{ sampel}$).
        </div>
    """, unsafe_allow_html=True)

with col_tree:
    # Merender objek Source dot_data asli pengerjaan kalian menggunakan native engine graphviz Streamlit
    with st.container(border=True):
        st.write("### 🌲 Real Exported Graphviz Tree - Anisa")
        dot_code = """
        digraph Tree {
        node [shape=box, style="filled, rounded", color="black", fontname="helvetica"] ;
        edge [fontname="helvetica"] ;
        0 [label=<x<sub>0</sub> &le; 0.876<br/>entropy = 1.0<br/>samples = 21564<br/>value = [10782, 10782]>, fillcolor="#ffffff"] ;
        1 [label=<x<sub>4</sub> &le; 0.088<br/>entropy = 0.177<br/>samples = 8442<br/>value = [8217, 225]>, fillcolor="#e6853f"] ;
        0 -> 1 [label="True"] ;
        2 [label=<x<sub>4</sub> &le; -0.59<br/>entropy = 0.004<br/>samples = 5825<br/>value = [5823, 2]>, fillcolor="#e58139"] ;
        1 -> 2 ;
        3 [label=<entropy = 0.0<br/>samples = 3668<br/>value = [3668, 0]>, fillcolor="#e58139"] ;
        2 -> 3 ;
        4 [label=<entropy = 0.011<br/>samples = 2157<br/>value = [2155, 2]>, fillcolor="#e5813a"] ;
        2 -> 4 ;
        5 [label=<entropy = 0.42<br/>samples = 2617<br/>value = [2394, 223]>, fillcolor="#e78c4a"] ;
        1 -> 5 ;
        6 [label=<x<sub>2</sub> &le; -0.421<br/>entropy = 0.713<br/>samples = 13122<br/>value = [2565, 10557]>, fillcolor="#68b4eb"] ;
        0 -> 6 [label="False"] ;
        7 [label=<entropy = 0.988<br/>samples = 2314<br/>value = [1009, 1305]>, fillcolor="#d2e9f9"] ;
        6 -> 7 ;
        8 [label=<x<sub>1</sub> &le; 0.851<br/>entropy = 0.595<br/>samples = 10808<br/>value = [1556, 9252]>, fillcolor="#5baee9"] ;
        6 -> 8 ;
        }
        """
        st.graphviz_chart(dot_code, use_container_width=True)

# --- 5. DATA SCIENCE PIPELINE WORKFLOW (RESPONSIF STEPPER) ---
st.markdown('<div class="slide-section-title">🛠️ Data Science Pipeline Workflow</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="pipeline-grid">
        <div class="pipeline-step">
            <div class="step-icon">🔍</div>
            <div class="step-title">1. Data Exploration</div>
            <div class="step-desc">Pbersihan pencilan riil dan seleksi signifikansi korelasi prediktor menggunakan metode ANOVA.</div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">⚖️</div>
            <div class="step-title">2. Data Balancing</div>
            <div class="step-desc">Penerapan teknik SMOTE Over-sampling untuk mengantisipasi ketimpangan distribusi kelas target.</div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">🧪</div>
            <div class="step-title">3. Model Experiment</div>
            <div class="step-desc">Pelatihan komparatif paralel dan pengujian silang kuantitatif berbasis skema 10-Fold Cross Validation.</div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">🚀</div>
            <div class="step-title">4. Model Deployment</div>
            <div class="step-desc">Penyimpanan arsitektur terbaik pohon keputusan ke format model.pkl untuk otomatisasi sistem produksi prediksi.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. INTERNATIONAL FOOTER ---
st.markdown("""
    <div class="premium-footer-zone">
        <p>© 2026 Team Jobes Sleep Analytics Platform • Built with Premium International Tech Portal Aesthetics</p>
    </div>
""", unsafe_allow_html=True)
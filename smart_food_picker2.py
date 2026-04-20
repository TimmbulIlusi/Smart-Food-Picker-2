import streamlit as st

st.title("Smart Food Picker 🍽️")
st.markdown("### 🧠 Sistem Rekomendasi Makanan Berbasis Rule-Based")
st.write("Pilih nutrisi, budget, dan fakta gizi untuk mendapatkan rekomendasi terbaik.")

# ================= INPUT =================
nutrisi = st.selectbox(
    "Pilih Kebutuhan Nutrisi:",
    ["Protein", "Karbohidrat", "Vitamin", "Lemak Sehat", "Serat"]
)

budget = st.number_input("Masukkan Budget (Rp):", min_value=0)

fakta_dipilih = st.multiselect(
    "Pilih Kandungan Gizi yang Diinginkan:",
    ["Protein", "Vitamin B", "Kalsium", "Zat Besi", "Serat", "Omega-3"]
)

# ================= FAKTA (DATA MAKANAN) =================
makanan = [
    {"nama": "Tempe", "kategori": "Protein", "harga": 5000, "berat": "±250g",
     "gizi": ["Protein", "Zat Besi", "Serat"]},

    {"nama": "Tahu", "kategori": "Protein", "harga": 5000, "berat": "±250g",
     "gizi": ["Protein", "Kalsium"]},

    {"nama": "Telur", "kategori": "Protein", "harga": 15000, "berat": "±10 butir",
     "gizi": ["Protein", "Vitamin B"]},

    {"nama": "Daging Ayam", "kategori": "Protein", "harga": 40000, "berat": "±1 kg",
     "gizi": ["Protein"]},

    {"nama": "Salmon", "kategori": "Protein", "harga": 80000, "berat": "±500g",
     "gizi": ["Protein", "Omega-3"]},

    {"nama": "Nasi Putih", "kategori": "Karbohidrat", "harga": 5000, "berat": "1 porsi",
     "gizi": []},

    {"nama": "Kentang", "kategori": "Karbohidrat", "harga": 12000, "berat": "±500g",
     "gizi": ["Serat"]},

    {"nama": "Roti Gandum", "kategori": "Karbohidrat", "harga": 25000, "berat": "±500g",
     "gizi": ["Serat"]},

    {"nama": "Quinoa", "kategori": "Karbohidrat", "harga": 60000, "berat": "±500g",
     "gizi": ["Protein", "Serat"]},

    {"nama": "Pisang", "kategori": "Vitamin", "harga": 5000, "berat": "±300g",
     "gizi": ["Serat"]},

    {"nama": "Jeruk", "kategori": "Vitamin", "harga": 15000, "berat": "±500g",
     "gizi": ["Vitamin B"]},

    {"nama": "Apel", "kategori": "Vitamin", "harga": 30000, "berat": "±500g",
     "gizi": ["Serat"]},

    {"nama": "Alpukat", "kategori": "Lemak Sehat", "harga": 50000, "berat": "±500g",
     "gizi": ["Lemak Sehat"]},

    {"nama": "Almond", "kategori": "Lemak Sehat", "harga": 90000, "berat": "±250g",
     "gizi": ["Lemak Sehat", "Omega-3"]},

    {"nama": "Bayam", "kategori": "Serat", "harga": 5000, "berat": "1 ikat",
     "gizi": ["Zat Besi", "Serat"]},

    {"nama": "Brokoli", "kategori": "Serat", "harga": 30000, "berat": "±500g",
     "gizi": ["Serat", "Vitamin B"]},
]

# ================= PROSES =================
if st.button("Dapatkan Rekomendasi"):

    if budget < 5000:
        st.error("❌ Budget minimal Rp5.000 ya.")
    
    else:
        st.info("🔍 Menganalisis kebutuhan Anda...")
        st.success("💡 Pilihan yang tersedia:")

        ditemukan = False
        terbaik = None

        for item in makanan:

            # ================= RULE 1 =================
            # IF kategori sesuai DAN budget cukup
            if nutrisi == item["kategori"] and budget >= item["harga"]:

                # ================= RULE 2 =================
                # IF fakta dipilih → harus cocok semua
                cocok = True
                for f in fakta_dipilih:
                    if f not in item["gizi"]:
                        cocok = False

                if cocok:
                    ditemukan = True

                    st.write(f"🍽️ {item['nama']} (Rp{item['harga']} / {item['berat']})")
                    st.write(f"👉 Kandungan: {', '.join(item['gizi']) if item['gizi'] else 'Umum'}")

                    # ================= RULE 3 =================
                    # cari yang paling mahal dalam budget (optimal)
                    if terbaik is None or item["harga"] > terbaik["harga"]:
                        terbaik = item

        # ================= RULE 4 =================
        if not ditemukan:
            st.warning("⚠️ Tidak ada makanan yang sesuai dengan pilihan Anda")

        # ================= RULE 5 =================
        if terbaik:
            st.markdown("---")
            st.success(f"⭐ Rekomendasi Utama: {terbaik['nama']}")
            st.write("👉 Dipilih untuk memaksimalkan budget Anda")

        # ================= RULE 6 =================
        if budget > 50000:
            st.info("💡 Budget besar memberi lebih banyak variasi makanan")

st.markdown("---")
st.caption("Smart Food Picker")

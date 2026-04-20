import streamlit as st

st.title("Smart Food Picker 🍽️")
st.markdown("### 🥗 Sistem Rekomendasi Makanan Sesuai dengan Kebutuhan Anda")
st.write("Pilih nutrisi, budget, dan fakta gizi untuk mendapatkan rekomendasi terbaik.")

# ================= INPUT =================
nutrisi = st.selectbox(
    "Pilih Kebutuhan Nutrisi:",
    ["Protein", "Karbohidrat", "Vitamin", "Lemak Sehat", "Serat"]
)

budget = st.number_input("Masukkan Budget (Rp):", min_value=0)

fakta_dipilih = st.multiselect(
    "Pilih Kandungan Gizi yang Diinginkan:",
    [
        "Protein",
        "Karbohidrat",
        "Vitamin A",
        "Vitamin B",
        "Vitamin C",
        "Vitamin D",
        "Vitamin E",
        "Kalsium",
        "Zat Besi",
        "Serat",
        "Omega-3",
        "Lemak Sehat"
    ]
)

# ================= FAKTA =================
makanan = [
    {"nama": "Tempe", "kategori": "Protein", "harga": 5000, "berat": "±250g",
     "gizi": ["Protein", "Vitamin B", "Zat Besi", "Serat"]},

    {"nama": "Tahu", "kategori": "Protein", "harga": 5000, "berat": "±250g",
     "gizi": ["Protein", "Kalsium", "Zat Besi"]},

    {"nama": "Telur", "kategori": "Protein", "harga": 15000, "berat": "±10 butir",
     "gizi": ["Protein", "Vitamin B", "Vitamin D", "Vitamin A"]},

    {"nama": "Daging Ayam", "kategori": "Protein", "harga": 40000, "berat": "±1 kg",
     "gizi": ["Protein", "Vitamin B", "Zat Besi"]},

    {"nama": "Salmon", "kategori": "Protein", "harga": 80000, "berat": "±500g",
     "gizi": ["Protein", "Vitamin D", "Vitamin B", "Omega-3"]},

    {"nama": "Nasi Putih", "kategori": "Karbohidrat", "harga": 5000, "berat": "1 porsi",
     "gizi": ["Karbohidrat"]},

    {"nama": "Kentang", "kategori": "Karbohidrat", "harga": 12000, "berat": "±500g",
     "gizi": ["Karbohidrat", "Vitamin C", "Vitamin B", "Serat"]},

    {"nama": "Roti Gandum", "kategori": "Karbohidrat", "harga": 25000, "berat": "±500g",
     "gizi": ["Karbohidrat", "Serat", "Vitamin B"]},

    {"nama": "Quinoa", "kategori": "Karbohidrat", "harga": 60000, "berat": "±500g",
     "gizi": ["Karbohidrat", "Protein", "Serat", "Vitamin B"]},

    {"nama": "Pisang", "kategori": "Vitamin", "harga": 5000, "berat": "±300g",
     "gizi": ["Vitamin B", "Vitamin C", "Serat"]},

    {"nama": "Jeruk", "kategori": "Vitamin", "harga": 15000, "berat": "±500g",
     "gizi": ["Vitamin C", "Vitamin B", "Serat"]},

    {"nama": "Apel", "kategori": "Vitamin", "harga": 30000, "berat": "±500g",
     "gizi": ["Vitamin C", "Serat"]},

    {"nama": "Alpukat", "kategori": "Lemak Sehat", "harga": 50000, "berat": "±500g",
     "gizi": ["Lemak Sehat", "Vitamin E", "Vitamin B"]},

    {"nama": "Almond", "kategori": "Lemak Sehat", "harga": 90000, "berat": "±250g",
     "gizi": ["Lemak Sehat", "Omega-3", "Vitamin E"]},

    {"nama": "Bayam", "kategori": "Serat", "harga": 5000, "berat": "1 ikat",
     "gizi": ["Zat Besi", "Serat", "Vitamin A", "Vitamin C"]},

    {"nama": "Brokoli", "kategori": "Serat", "harga": 30000, "berat": "±500g",
     "gizi": ["Serat", "Vitamin C", "Vitamin A", "Vitamin B"]},
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

            # RULE 1: kategori + budget
            if nutrisi == item["kategori"] and budget >= item["harga"]:

                # RULE 2: fleksibel (minimal cocok salah satu)
                if fakta_dipilih:
                    cocok = any(f in item["gizi"] for f in fakta_dipilih)
                else:
                    cocok = True

                if cocok:
                    ditemukan = True

                    st.write(f"🍽️ {item['nama']} (Rp{item['harga']} / {item['berat']})")
                    st.write(f"🧬 Kandungan gizi: {', '.join(item['gizi'])}")

                    # RULE 3: pilih terbaik (maksimalkan budget)
                    if terbaik is None or item["harga"] > terbaik["harga"]:
                        terbaik = item

        # RULE 4
        if not ditemukan:
            st.warning("⚠️ Tidak ada makanan yang sesuai dengan pilihan Anda")

        # ================= REKOMENDASI UTAMA =================
        if terbaik:
            st.markdown("---")
            st.success(f"⭐ Rekomendasi Utama: {terbaik['nama']}")

            alasan = []

            alasan.append(f"✔ Sesuai kebutuhan nutrisi: {nutrisi}")
            alasan.append(f"✔ Harga sesuai budget (Rp{terbaik['harga']})")

            if fakta_dipilih:
                cocok = [f for f in fakta_dipilih if f in terbaik["gizi"]]
                if cocok:
                    alasan.append(f"✔ Mengandung gizi yang dipilih: {', '.join(cocok)}")

            alasan.append("✔ Memaksimalkan penggunaan budget")
            alasan.append(f"✔ Kandungan gizi utama: {', '.join(terbaik['gizi'])}")

            st.write("📌 Alasan rekomendasi:")
            for a in alasan:
                st.write(a)

        # RULE 5
        if budget > 50000:
            st.info("💡 Budget besar memberi lebih banyak variasi makanan")

st.markdown("---")
st.caption("Smart Food Picker | Eat Healthy, Spend Smartly! 🌽")

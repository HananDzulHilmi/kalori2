import streamlit as st
import random

# Judul Aplikasi
st.title("🍽️ Kalkulator Kebutuhan Kalori & Rekomendasi Menu Sehat")

st.markdown("""
Halo! Masukkan berat badan dan tinggi badanmu di bawah ini untuk menghitung kebutuhan kalori harianmu.
Aplikasi ini juga akan memberikan rekomendasi makanan dengan prinsip 4 sehat 5 sempurna 🍚🍗🥬🍎🥛
""")

# Input berat dan tinggi
berat = st.number_input("Masukkan berat badan (kg)", min_value=1.0, step=0.1)
tinggi = st.number_input("Masukkan tinggi badan (cm)", min_value=1.0, step=0.1)

# Tombol Hitung
if st.button("Hitung Kebutuhan Kalori & Tampilkan Menu"):
    if berat > 0 and tinggi > 0:
        bmr = 10 * berat + 6.25 * tinggi - 5 * 25 + 5  # Rumus BMR laki-laki usia 25 thn
        kalori_harian = round(bmr * 1.2)  # asumsi aktivitas ringan
        st.success(f"Kebutuhan kalori harianmu: {kalori_harian} kkal")

        st.markdown("## 🥗 Rekomendasi Menu 4 Sehat 5 Sempurna")

        # Data makanan: (nama, kalori, berat)
        karbo = [
            ("🍚 Nasi Putih", "175 kkal", "150 gram"),
            ("🍚 Nasi Merah", "160 kkal", "150 gram"),
            ("🌽 Nasi Jagung", "155 kkal", "150 gram"),
            ("🥔 Kentang Rebus", "140 kkal", "150 gram"),
            ("🌿 Singkong Kukus", "135 kkal", "150 gram"),
            ("🥣 Oatmeal", "150 kkal", "40 gram"),
            ("🍞 Roti Gandum", "120 kkal", "60 gram"),
            ("🍙 Lontong", "130 kkal", "150 gram"),
            ("🍜 Mie Jagung", "145 kkal", "100 gram"),
            ("🍠 Ubi Rebus", "110 kkal", "100 gram"),
        ]

        lauk = [
            ("🍳 Telur Dadar", "180 kkal", "60 gram"),
            ("🍽️ Tempe Goreng", "200 kkal", "80 gram"),
            ("🍢 Tahu Bacem", "160 kkal", "80 gram"),
            ("🍗 Ayam Rebus", "190 kkal", "100 gram"),
            ("🐟 Ikan Bakar", "180 kkal", "100 gram"),
            ("🥩 Daging Sapi Panggang", "250 kkal", "100 gram"),
            ("🦐 Udang Saus Tiram", "170 kkal", "100 gram"),
            ("🐟 Tuna Kukus", "160 kkal", "100 gram"),
            ("🍗 Ayam Kukus", "175 kkal", "100 gram"),
            ("🥚 Telur Rebus", "90 kkal", "50 gram"),
        ]

        sayur = [
            ("🥬 Sayur Bayam", "40 kkal", "100 gram"),
            ("🥦 Tumis Kangkung", "45 kkal", "100 gram"),
            ("🥕 Capcay", "60 kkal", "120 gram"),
            ("🍲 Sayur Asem", "50 kkal", "150 gram"),
            ("🥣 Sup Wortel", "55 kkal", "120 gram"),
            ("🥗 Gado-Gado", "120 kkal", "200 gram"),
            ("🥒 Lalapan", "30 kkal", "50 gram"),
            ("🍛 Sayur Lodeh", "70 kkal", "150 gram"),
            ("🥦 Tumis Brokoli", "60 kkal", "100 gram"),
            ("🥗 Urap Sayur", "50 kkal", "100 gram"),
        ]

        buah = [
            ("🍌 Pisang", "90 kkal", "100 gram"),
            ("🍎 Apel", "80 kkal", "125 gram"),
            ("🍈 Pepaya", "70 kkal", "150 gram"),
            ("🍊 Jeruk", "60 kkal", "130 gram"),
            ("🍉 Semangka", "50 kkal", "200 gram"),
            ("🍈 Melon", "55 kkal", "150 gram"),
            ("🍍 Nanas", "60 kkal", "150 gram"),
            ("🥭 Mangga", "90 kkal", "150 gram"),
            ("🍇 Anggur", "70 kkal", "100 gram"),
            ("🍎 Salak", "65 kkal", "100 gram"),
        ]

        susu = [
            ("🥛 Susu Sapi", "120 kkal", "200 gram"),
            ("🌱 Susu Kedelai", "100 kkal", "200 gram"),
            ("🍶 Yogurt", "110 kkal", "150 gram"),
            ("🥛 Kefir", "100 kkal", "150 gram"),
            ("🌰 Susu Almond", "80 kkal", "200 gram"),
            ("🥤 Susu UHT", "130 kkal", "250 gram"),
            ("🥛 Susu Skim", "90 kkal", "200 gram"),
            ("🥄 Susu Bubuk", "150 kkal", "25 gram"),
            ("🍫 Susu Coklat", "160 kkal", "250 gram"),
            ("🥛 Susu Full Cream", "140 kkal", "200 gram"),
        ]

        # Ambil acak masing-masing 1 dari tiap kategori
        selected_karbo = random.choice(karbo)
        selected_lauk = random.choice(lauk)
        selected_sayur = random.choice(sayur)
        selected_buah = random.choice(buah)
        selected_susu = random.choice(susu)

        menu = [selected_karbo, selected_lauk, selected_sayur, selected_buah, selected_susu]

        total_kalori = 0

        # Tampilkan menu
        for nama, kalori, berat in menu:
            st.markdown(f"**{nama}** - {kalori}, {berat}")
            total_kalori += int(kalori.split()[0])

        st.markdown(f"### 🔢 Total Kalori dari menu di atas: {total_kalori} kkal")
        if total_kalori > kalori_harian:
            st.warning("Total kalori dari menu ini melebihi kebutuhan harianmu.")
        elif total_kalori < kalori_harian:
            st.info("Total kalori dari menu ini masih di bawah kebutuhan harianmu.")
        else:
            st.success("Total kalori dari menu ini sesuai dengan kebutuhan harianmu.")
    else:
        st.error("Masukkan berat dan tinggi yang valid dulu ya 😊")

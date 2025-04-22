import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalkulator Kalori", layout="centered")

st.title("🍽️ Kalkulator Kalori & Menu 4 Sehat 5 Sempurna")

# Sidebar - Riwayat
st.sidebar.header("📜 Riwayat Menu")
if 'history' not in st.session_state:
    st.session_state['history'] = []

for i, entry in enumerate(st.session_state['history']):
    st.sidebar.markdown(f"### Menu {i+1}")
    for item in entry['menu']:
        st.sidebar.markdown(f"- {item[0]}: {item[1]} | {item[2]}")
    st.sidebar.markdown(f"**Total: {entry['total']} kkal**")

# Input berat & tinggi
berat = st.number_input("Berat Badan (kg)", min_value=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=1.0)

if st.button("Hitung Kalori & Tampilkan Menu"):
    if berat > 0 and tinggi > 0:
        bmr = 10 * berat + 6.25 * tinggi - 5 * 25 + 5  # Asumsi pria, usia 25
        kebutuhan_kalori = round(bmr * 1.2)
        st.success(f"🔢 Kebutuhan Kalori Harianmu: {kebutuhan_kalori} kkal")

        # Data makanan (nama, kalori, berat)
        karbo = [
            ("🍚 Nasi Putih", "175 kkal", "150 gram"),
            ("🍞 Roti Gandum", "120 kkal", "60 gram"),
            ("🥣 Oatmeal", "150 kkal", "40 gram"),
            ("🥔 Kentang Rebus", "140 kkal", "150 gram"),
            ("🍠 Ubi Rebus", "110 kkal", "100 gram")
        ]

        lauk = [
            ("🍳 Telur Dadar", "180 kkal", "60 gram"),
            ("🍽️ Tempe Goreng", "200 kkal", "80 gram"),
            ("🐟 Ikan Bakar", "180 kkal", "100 gram"),
            ("🍗 Ayam Kukus", "175 kkal", "100 gram"),
            ("🥩 Daging Sapi", "250 kkal", "100 gram")
        ]

        sayur = [
            ("🥬 Sayur Bayam", "40 kkal", "100 gram"),
            ("🥦 Tumis Brokoli", "60 kkal", "100 gram"),
            ("🍲 Sayur Asem", "50 kkal", "150 gram"),
            ("🥗 Urap Sayur", "50 kkal", "100 gram"),
            ("🥕 Capcay", "60 kkal", "120 gram")
        ]

        buah = [
            ("🍌 Pisang", "90 kkal", "100 gram"),
            ("🍎 Apel", "80 kkal", "125 gram"),
            ("🍊 Jeruk", "60 kkal", "130 gram"),
            ("🍈 Pepaya", "70 kkal", "150 gram"),
            ("🍇 Anggur", "70 kkal", "100 gram")
        ]

        susu = [
            ("🥛 Susu Sapi", "120 kkal", "200 gram"),
            ("🌱 Susu Kedelai", "100 kkal", "200 gram"),
            ("🍶 Yogurt", "110 kkal", "150 gram"),
            ("🌰 Susu Almond", "80 kkal", "200 gram"),
            ("🥛 Susu Full Cream", "140 kkal", "200 gram")
        ]

        # Pilih acak masing-masing
        selected_karbo = random.choice(karbo)
        selected_lauk = random.choice(lauk)
        selected_sayur = random.choice(sayur)
        selected_buah = random.choice(buah)
        selected_susu = random.choice(susu)

        menu = [selected_karbo, selected_lauk, selected_sayur, selected_buah, selected_susu]

        st.subheader("🍱 Rekomendasi Menu")
        total_kalori = 0
        kalori_list = []
        label_list = ["Karbo", "Lauk", "Sayur", "Buah", "Susu"]

        for item in menu:
            nama, kalori, berat = item
            kal = int(kalori.split()[0])
            kalori_list.append(kal)
            total_kalori += kal
            st.markdown(f"✅ **{nama}** — {kalori}, {berat}")

        st.markdown(f"### 🔢 Total Kalori Menu: **{total_kalori} kkal**")
        if total_kalori > kebutuhan_kalori:
            st.warning("⚠️ Menu melebihi kebutuhan kalori harianmu.")
        elif total_kalori < kebutuhan_kalori:
            st.info("ℹ️ Menu di bawah kebutuhan kalori.")
        else:
            st.success("✅ Menu sesuai kebutuhan kalori harianmu.")

        # Pie Chart
        fig, ax = plt.subplots()
        ax.pie(kalori_list, labels=label_list, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

        if st.button("💾 Simpan Menu Ini"):
            st.session_state['history'].append({
                "menu": menu,
                "total": total_kalori
            })
            st.success("✅ Menu disimpan ke riwayat!")
    else:
        st.error("Masukkan berat dan tinggi yang valid dulu ya, Sayang 😘")

import streamlit as st
import random
import matplotlib.pyplot as plt

# Title
st.title("🍽️ Kalkulator Kalori & Rekomendasi Menu 4 Sehat 5 Sempurna")

st.markdown("Masukkan berat dan tinggi badanmu untuk menghitung kebutuhan kalori harian 💪")

# Sidebar - History Menu
st.sidebar.header("📜 Riwayat Menu")
if 'history' not in st.session_state:
    st.session_state['history'] = []

for i, menu in enumerate(st.session_state['history']):
    st.sidebar.markdown(f"### Menu {i+1}")
    for item in menu['menu']:
        st.sidebar.markdown(f"- {item[0]}: {item[1]}, {item[2]}")
    st.sidebar.markdown(f"Total Kalori: **{menu['total']} kkal**")

# Input berat dan tinggi
berat = st.number_input("Berat Badan (kg)", min_value=1.0, step=0.1)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=1.0, step=0.1)

if st.button("🔍 Hitung & Rekomendasikan Menu"):
    if berat > 0 and tinggi > 0:
        bmr = 10 * berat + 6.25 * tinggi - 5 * 25 + 5
        kalori_harian = round(bmr * 1.2)
        st.success(f"✅ Kebutuhan kalori harianmu: {kalori_harian} kkal")

        st.markdown("## 🥗 Rekomendasi Menu 4 Sehat 5 Sempurna")

        # Data makanan
        karbo = [("🍚 Nasi Putih", "175 kkal", "150 gram"), ...]  # disingkat
        lauk = [("🍳 Telur Dadar", "180 kkal", "60 gram"), ...]
        sayur = [("🥬 Sayur Bayam", "40 kkal", "100 gram"), ...]
        buah = [("🍌 Pisang", "90 kkal", "100 gram"), ...]
        susu = [("🥛 Susu Sapi", "120 kkal", "200 gram"), ...]

        selected_karbo = random.choice(karbo)
        selected_lauk = random.choice(lauk)
        selected_sayur = random.choice(sayur)
        selected_buah = random.choice(buah)
        selected_susu = random.choice(susu)

        menu = [selected_karbo, selected_lauk, selected_sayur, selected_buah, selected_susu]
        labels = ["Karbo", "Lauk", "Sayur", "Buah", "Susu"]
        kalori_values = [int(item[1].split()[0]) for item in menu]
        total_kalori = sum(kalori_values)

        for item in menu:
            st.markdown(f"- **{item[0]}** — {item[1]}, {item[2]}")

        st.markdown(f"### 🔢 Total Kalori Menu: {total_kalori} kkal")
        if total_kalori > kalori_harian:
            st.warning("⚠️ Kalori melebihi kebutuhan harian.")
        elif total_kalori < kalori_harian:
            st.info("ℹ️ Kalori di bawah kebutuhan harian.")
        else:
            st.success("✅ Kalori pas!")

        # Chart Pie
        fig, ax = plt.subplots()
        ax.pie(kalori_values, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

        if st.button("💾 Simpan Menu Ini"):
            st.session_state['history'].append({
                "menu": menu,
                "total": total_kalori
            })
            st.success("Menu berhasil disimpan ke riwayat! 📝")
    else:
        st.error("Masukkan berat & tinggi yang valid dulu ya 😊")

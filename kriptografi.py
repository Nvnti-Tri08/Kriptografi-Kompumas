import streamlit as st

st.set_page_config(page_title="Kriptografi Ciphertext", page_icon="🔐", layout="centered")

# Fungsi Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

st.title("🔒 Kriptografi Ciphertext")
st.markdown(
    "Aplikasi Caesar Cipher sederhana untuk enkripsi dan dekripsi pesan. "
    "Pilih mode dan masukkan pesan untuk melihat hasilnya." 
)
st.write("---")

col1, col2 = st.columns([3, 1])
with col1:
    mode = st.radio("Mode", ["Enkripsi", "Dekripsi"], index=0)
    input_label = "Masukkan Pesan asli" if mode == "Enkripsi" else "Masukkan Ciphertext"
    input_placeholder = "Contoh: halo dunia" if mode == "Enkripsi" else "Contoh: kdyr gxqlx"
    pesan = st.text_area(input_label, height=180, placeholder=input_placeholder)
with col2:
    kunci = st.number_input("Kunci (Shift)", min_value=1, max_value=25, value=3, help="Nilai kunci antara 1 sampai 25")
    st.markdown(
        "**Petunjuk:**\n"
        "- Jika pilih `Enkripsi`, masukkan teks asli.\n"
        "- Jika pilih `Dekripsi`, masukkan ciphertext yang sudah terenkripsi.\n"
        "- Karakter selain huruf tetap sama."
    )

if pesan.strip():
    if mode == "Enkripsi":
        hasil = caesar_encrypt(pesan, kunci)
        label = "Ciphertext"
        note = "Silakan simpan hasil enkripsi atau kirim ke penerima."
    else:
        hasil = caesar_decrypt(pesan, kunci)
        label = "Hasil Dekripsi"
        note = (
            "Hasil dekripsi benar hanya jika input adalah ciphertext yang dibuat oleh enkripsi. "
            "Jika kamu memasukkan teks asli, hasilnya akan terlihat acak karena itu bukan ciphertext."
        )

    st.success("Pesan berhasil diproses!")
    st.markdown("---")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader(label)
        st.code(hasil, language="text")
        st.success(note)
    with col_b:
        st.subheader("Detail")
        st.write("Mode:", mode)
        st.write("Kunci yang digunakan:")
        st.code(str(kunci), language="text")

    st.markdown(
        "### Tips:\n"
        "- Untuk mengembalikan pesan, pilih mode `Dekripsi` dan gunakan kunci yang sama.\n"
        "- Jika memasukkan ciphertext di mode `Enkripsi`, hasilnya akan menjadi teks terenkripsi dua kali."
    )
else:
    st.warning("Silakan masukkan pesan terlebih dahulu.")

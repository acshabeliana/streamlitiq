import csv
import streamlit as st

# Fungsi untuk menghitung nilai IQ dan kategori
def kalkulator_iq(skor_mentah, mean, std_dev):
    z = (skor_mentah - mean) / std_dev
    iq = round(100 + 15 * z)
    
    if iq > 110:
        category = "Di Atas Rata-Rata"
        outcome = 3
    elif 90 <= iq <= 110:
        category = "Rata-Rata"
        outcome = 2
    else:
        category = "Di Bawah Rata-Rata"
        outcome = 1
    
    return iq, category, outcome

# Fungsi untuk memproses skor mentah
def input(skor_mentah):
    try:
        # Membaca data dari file CSV
        file_name = "data_iq.csv"  # Pastikan file CSV ada di folder yang sama dengan script
        with open(file_name, mode="r") as file:
            reader = csv.DictReader(file)
            scores = [int(row["Skor Mentah"]) for row in reader]
            mean = sum(scores) / len(scores)
            variance = sum((x - mean) ** 2 for x in scores) / len(scores)
            std_dev = variance ** 0.5
        
        # Hitung IQ dan kategori
        iq, category, outcome = kalkulator_iq(skor_mentah, mean, std_dev)
        
        # Tampilkan hasil
        st.write(f"Nilai IQ: {iq}")
        st.write(f"Kategori: {category}")
        st.write(f"Outcome: {outcome}")
    except FileNotFoundError:
        st.error("File data_iq.csv tidak ditemukan. Pastikan file tersedia di direktori.")
    except ValueError:
        st.error("Masukkan nilai mentah berupa angka!")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# Streamlit 
def main():
    st.title("Aplikasi Penghitung IQ")
    
    # menginput skor mentah
    skor_mentah = st.number_input("Masukkan Skor Mentah", min_value=0, max_value=200, step=1)
    
    # Tombol untuk memproses skor
    if st.button("Hitung IQ"):
        process_input(skor_mentah)

if __name__ == "__main__":
    main()

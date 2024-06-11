# PyFy Tech: Platform Multimedia Berbasis Flask untuk Pengolahan Gambar dan Video
![Screenshot 2024-06-10 235153](https://github.com/athalie-aurora/PyFy_Tech/assets/119656945/21978e5b-c047-4328-a280-6128eaf437bc)

PyFy Tech adalah platform multimedia berbasis Flask yang memungkinkan pengguna untuk mengelola dan memanipulasi berbagai jenis media seperti gambar dan video dengan mudah dan efisien. Aplikasi ini memanfaatkan teknologi canggih seperti TensorFlow, PyTesseract, dan OpenCV untuk menyediakan berbagai solusi pengolahan citra digital.

## Dokumentasi

### Fitur Utama:

- **Prediksi Gambar**: Menggunakan model VGG16 yang telah dilatih untuk mengenali berbagai objek dalam gambar.
- **Ekstraksi Teks dari Gambar**: Memanfaatkan PyTesseract untuk mengekstraksi teks dari gambar.
- **Deteksi Video**: Menggunakan OpenCV untuk mendeteksi dan melacak objek dalam video.

### Modul Utama:

1. **Prediksi Gambar**:
   - Pengguna mengunggah gambar melalui antarmuka web.
   - Sistem melakukan praproses pada gambar dan menggunakan model VGG16 untuk melakukan prediksi objek dalam gambar.
   - Hasil prediksi ditampilkan dengan label dan probabilitasnya.
![Screenshot 2024-06-10 234318](https://github.com/athalie-aurora/PyFy_Tech/assets/119656945/7d190e30-9ccc-4237-9448-e24599a8d33e)

2. **Ekstraksi Teks dari Gambar**:
   - Pengguna mengunggah gambar yang berisi teks.
   - Sistem menggunakan PyTesseract untuk mengekstraksi teks dari gambar.
   - Teks yang diekstraksi dapat diunduh dalam format teks.
![Screenshot 2024-06-10 234356](https://github.com/athalie-aurora/PyFy_Tech/assets/119656945/b79e6076-73b7-476e-a8c6-c3095fb64e44)



3. **Deteksi Video**:
   - Pengguna dapat merekam video menggunakan kamera komputer.
   - Video yang direkam disimpan dan dapat diunduh oleh pengguna.
![Screenshot 2024-06-11 201322](https://github.com/athalie-aurora/PyFy_Tech/assets/119656945/e3b3f72f-fcd3-4538-807b-e52b2b284e7f)



## Instalasi

Clone repositori ini atau unduh skrip:

```bash
git clone https://github.com/athalie-aurora/PyFy_Tech.git
```

Navigasi ke direktori proyek:

```bash
cd PyFy_Tech
```

Aktifkan lingkungan virtual [unduh disini](https://drive.google.com/file/d/1Z50xfLk-JBQcNRGXKdMfezVJlJuHTAJ7/view?usp=sharing) 

```bash
python .venv\Scripts\activate
```

atau buat lingkungan virtual baru

```bash
python -m venv [nama_venv]
```


## Penggunaan

Jalankan aplikasi menggunakan perintah berikut:

```bash
python app.py
```

Jika berhasil, dapat akses aplikasi di browser pada alamat:
```bash
http://localhost:3000
```


atau ketik di browser


```bash
127.0.0.1:3000/hello
```



# Athalie Aurora NIM 221511003 - Pengolahan Citra Digital





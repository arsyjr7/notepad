# Noteapp Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Customization](#customization)
4. [Running the Application](#running-the-application)
5. [Deployment](#deployment)

---

## Introduction
**Noteapp** adalah aplikasi sederhana untuk mencatat dan mengelola catatan menggunakan Flask dan Supabase sebagai backend. Aplikasi ini memiliki fitur untuk menambahkan dan menghapus catatan.

---

## Setup

### Prerequisites
Pastikan Anda memiliki hal berikut:
- Python 3.8 atau lebih baru
- Virtual environment (opsional, tetapi disarankan)
- Supabase account dan project
- Git (opsional)

### Langkah-langkah Setup
1. **Clone Repository**  
   Clone repository ini ke komputer Anda:
   ```bash
   git clone <repository-url>
   cd notepad
   ```

2. **Buat Virtual Environment (Opsional)**  
   Buat dan aktifkan virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # Untuk Linux/Mac
   venv\Scripts\activate    # Untuk Windows
   ```

3. **Install Dependencies**  
   Install semua dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi Supabase**  
   - Buat file `.env` di root folder (jika belum ada).
   - Tambahkan variabel berikut ke dalam file `.env`:
     ```
     SUPABASE_URL=<your-supabase-url>
     SUPABASE_KEY=<your-supabase-key>
     ```
   - Ganti `<your-supabase-url>` dan `<your-supabase-key>` dengan kredensial dari Supabase Anda.

5. **Setup Database di Supabase**  
   - Buat tabel bernama `noteapp` di Supabase.
   - Tambahkan kolom berikut:
     - `id` (integer, primary key, auto-increment)
     - `text` (text)

---

## Customization

### Mengubah Tampilan
- **CSS**: Anda dapat mengubah tampilan aplikasi dengan memodifikasi file `static/style.css`.
- **HTML**: Untuk mengubah struktur halaman, edit file `templates/index.html`.

### Menambahkan Fitur Baru
- Tambahkan route baru di file `app.py` untuk fitur tambahan.
- Pastikan untuk menyesuaikan database Supabase jika diperlukan.

---

## Running the Application

1. **Jalankan Aplikasi**  
   Gunakan perintah berikut untuk menjalankan aplikasi:
   ```bash
   python app.py
   ```

2. **Akses Aplikasi**  
   Buka browser Anda dan akses aplikasi di:
   ```
   http://127.0.0.1:5000
   ```

---

## Deployment

### Heroku Deployment
1. **Buat File `Procfile`**  
   Pastikan file `Procfile` sudah ada dengan isi berikut:
   ```
   web: python app.py
   ```

2. **Install Heroku CLI**  
   Download dan install Heroku CLI dari [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Login ke Heroku**  
   Login ke akun Heroku Anda:
   ```bash
   heroku login
   ```

4. **Buat Aplikasi di Heroku**  
   Buat aplikasi baru:
   ```bash
   heroku create
   ```

5. **Push ke Heroku**  
   Deploy aplikasi ke Heroku:
   ```bash
   git add .
   git commit -m "Deploy Noteapp"
   git push heroku main
   ```

6. **Tambahkan Config Vars**  
   Tambahkan `SUPABASE_URL` dan `SUPABASE_KEY` ke Config Vars di dashboard Heroku.

7. **Akses Aplikasi**  
   Aplikasi Anda akan tersedia di URL yang diberikan oleh Heroku.

---

## Troubleshooting
- **Error: Missing Environment Variables**  
  Pastikan file `.env` sudah diisi dengan benar.
- **Database Issues**  
  Periksa apakah tabel `noteapp` sudah dibuat di Supabase dengan struktur yang benar.

---
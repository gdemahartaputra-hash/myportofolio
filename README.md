Nama : Gde Maharta Putra Wicaksana Ridjasa

NPM : 2506549051

Kelas : PBP A

Jadwal:
- Senin (15.00-16.40)
- Rabu (16.00-17.40)

### Tugas 1 

1. Ya, saya menggunakan elemen semantik seperti \<header>, \<nav>, \<main>, \<section>, dan \<footer> yang terlihat di struktur halaman: \<header class="site-header"> untuk navbar, \<main> yang membungkus tiga \<section> (Profile, Education, Experience) masing-masing dengan id unik untuk anchor navigation, dan \<footer class="site-footer"> di bagian bawah.

    Elemen-elemen ini membantu karena:

    - \<section> memisahkan konten berdasarkan topik yang jelas (profil, riwayat pendidikan, pengalaman), sehingga browser bisa memahami "blok" konten tanpa harus menebak dari class CSS saja
    - \<nav> menandai kumpulan link navigasi, membedakannya dari sekadar deretan \<a> biasa
    - Struktur ini juga memudahkan saya sendiri saat maintenance agar saya tahu persis section mana yang harus diedit tanpa membaca ulang seluruh dokumen
    
    Saya tidak menggunakan elemen \<article> atau \<aside> karena seluruh isi portofolio ini merupakan satu kesatuan narasi utama. Tidak ada konten mandiri yang dirancang untuk didistribusikan secara terpisah seperti kriteria \<article>, maupun informasi pendukung yang berada di luar alur baca utama seperti kriteria \<aside>. Oleh karena itu, pengelompokan menggunakan \<section> sudah tepat untuk merepresentasikan struktur halaman.

2. Tantangan utama justru muncul dari pola interaksi berbasis :hover yang saya pakai di section Experience. Detail pengalaman (.experience-detail) sengaja disembunyikan (max-height: 0; opacity: 0;) dan baru muncul saat card di-hover (.experience-item:hover .experience-detail), termasuk ikon "+" yang berputar jadi "×". Masalahnya, :hover tidak punya konsep yang sama di perangkat sentuh (mobile/tablet), tidak ada mouse yang bisa "melayang" di atas elemen. Ini artinya, tanpa penyesuaian lebih lanjut, pengguna mobile bisa jadi tidak akan pernah melihat isi detail pengalaman saya sama sekali, karena tidak ada cara untuk memicu state hover tersebut lewat sentuhan.

    Tantangan kedua ada di section Education: logo sekolah (.education-logo) saya buat ukuran tetap 200px x 200px dengan position: absolute di sisi kanan card, dan .education-list punya padding-left: 3.5rem yang juga nilai tetap (fixed rem, bukan relatif terhadap lebar layar). Karena saya belum menambahkan media query khusus untuk section ini, di layar sempit logo sebesar itu berpotensi overflow keluar dari card atau menabrak teks nama sekolah, alih-alih menyesuaikan ukurannya secara proporsional.

    Untuk mengevaluasi mana yang harus diprioritaskan, saya melihatnya dari sudut pandang: elemen yang murni dekoratif (seperti logo besar atau efek hover "+") boleh disederhanakan/disembunyikan di mobile, tapi elemen yang membawa informasi inti (nama sekolah, tahun, deskripsi pengalaman) harus tetap bisa diakses dengan cara apa pun. Hal ini menjadi catatan penting untuk saya perbaiki, karena saat ini pola hover-only itu belum punya fallback untuk mobile.

3. Karena semua konten (nama sekolah, pengalaman kerja, deskripsi) di-hardcode langsung di file HTML, setiap kali ada update, misalnya menambah pengalaman kerja baru, saya harus mengedit HTML secara manual dan push ulang. Tidak ada cara bagi saya (atau orang lain) untuk menambah/mengubah data tanpa menyentuh kode langsung. Pada link mail dan CV, keduanya hanya static link (ke Google Docs dan mailto), tidak ada form kontak yang benar-benar mengirim/menyimpan pesan.

    Berdasarkan batasan ini, fungsionalitas dinamis yang paling ingin saya siapkan adalah integrasi basis data untuk data riwayat agar dapat diperbarui melalui panel admin Django, serta formulir kontak fungsional untuk menggantikan link statis mailto.

---

# Dokumentasi

# Portfolio Website Gde Maharta Putra Wicaksana Ridjasa

Website portofolio pribadi yang dibangun sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform (PBP), Fakultas Ilmu Komputer, Universitas Indonesia.

## Deskripsi Proyek

Website ini menampilkan profil, riwayat pendidikan, dan pengalaman (experience) pemilik, dengan pendekatan desain minimalis dan beberapa interaksi animasi (scroll-driven animation, AOS, dan efek hover custom).

## Tech Stack

- HTML5 & CSS3 (custom, tanpa framework CSS)
- AOS (Animate On Scroll) untuk animasi scroll pada section Experience
- Font: Playfair Display & Space Grotesk (Google Fonts)

## Setup / Menjalankan Proyek

1. Clone repository ini:
   ```bash
   git clone <url-repo-ini>
   cd myportofolio


## Progress

### Commit 1: Modifikasi Desain
- Menyusun ulang layout dan palet warna dasar pada `style.css`.
- Menentukan tipografi (Playfair Display) dan struktur awal `index.html`.

### Commit 2: Pembuatan Education Section
- Membangun struktur HTML `education-item` untuk riwayat pendidikan.
- Menambahkan styling dasar section Education.
- Mengimplementasikan animasi `@keyframes educationPulse` berbasis scroll-driven animation (`animation-timeline: view()`) agar tiap item pendidikan "berdenyut" mengikuti posisi scroll di viewport.

### Commit 3: Penambahan Logo pada Education Section
- Menambahkan logo institusi (universitas, SMA, SMP, SD) pada tiap `education-item`.
- Menyesuaikan layout agar logo dan teks selaras secara visual.

### Commit 4: Pembuatan Experience Section
- Membangun struktur HTML section Experience.
- Mengintegrasikan library AOS (Animate On Scroll) dengan animasi `flip-down` pada tiap `experience-item`.
- Menerapkan styling accordion (hover-based expand/collapse) untuk menampilkan detail experience.
- Menambahkan efek hover "terangkat" (neobrutalism-style shadow) pada tiap `experience-item`.

## AI Disclosure
Tools yang digunakan: Claude Code (model Claude Sonnet 5), digunakan sebagai pair-programming assistant selama pengerjaan section Education dan Experience.

Strategi prompting: Saya menggunakan AI terutama untuk dua hal (1) meminta penjelasan konsep/mekanisme kode yang sudah ada atau baru ditambahkan, dan (2) melakukan debugging saat ada bagian yang tidak berjalan sesuai ekspektasi. Contoh pertanyaan yang saya ajukan selama proses:

### Beberapa AI Interaction Log


### 1. Pertanyaan pemahaman konsep scroll-driven animation

**Prompt:**
> "jelaskan kepada saya terkait @keyframes educationPulse yang anda gunakan sebagai animation dari setiap education-item"

**Konteks & tujuan:** Memastikan saya memahami mekanisme animasi yang sudah ada di `style.css` sebelum melanjutkan pekerjaan lain, bukan sekadar menerima kode tanpa mengerti cara kerjanya.

**Ringkasan hasil:** AI menjelaskan bahwa animasi ini berbasis CSS scroll-driven animation (`animation-timeline: view()`, `animation-range: cover 0% cover 100%`), bukan animasi berbasis waktu karena progress-nya mengikuti posisi elemen relatif terhadap viewport saat scroll. Keyframe 0%/100% membuat item pudar & mengecil saat masuk/keluar viewport, 50% membuat item menyala penuh saat berada di tengah layar. Juga dijelaskan keterbatasan dukungan browser untuk `animation-timeline: view()`.

**Dampak ke kode:** Tidak ada perubahan kode, murni sesi pemahaman.

---

### 2. Permintaan implementasi: integrasi AOS pada section Experience

**Prompt:**
> "Sekarang, saya ingin membuat bagian experience tetapi saya sekarang ingin menggunakan framework aos (https://michalsnik.github.io/aos/). Saya ingin setiap experience saya menggunakan animation flip-down dari aos."

**Ringkasan hasil:** AI memberikan langkah integrasi AOS: menambahkan `aos.css` di `<head>`, `aos.js` + `AOS.init()` sebelum `</body>`, dan atribut `data-aos="flip-down"` beserta `data-aos-delay` bertahap pada tiap `.experience-item`. AI juga menandai potensi inkonsistensi gaya animasi antara section Education (scroll-driven, berdenyut terus) dan Experience (AOS, sekali trigger).

**Dampak ke kode:** Kode diberikan sebagai referensi untuk diterapkan manual ke `index.html`.

---

### 3. Pertanyaan pemahaman konsep fungsi tag `<script>`

**Prompt:**
> "\<script> memangnya untuk apa?"

**Konteks & tujuan:** Menggali pemahaman kenapa perlu dua `<script>` terpisah (satu memuat library AOS, satu memanggil `AOS.init()`), bukan sekadar menyalin kode yang diberikan.

**Ringkasan hasil:** AI menjelaskan perbedaan fungsi kedua script: yang pertama memuat kode library AOS itu sendiri (tanpa ini, `AOS` sebagai objek tidak pernah ada); yang kedua mengaktifkan AOS dengan konfigurasi (`duration`, `once`). Juga dijelaskan alasan penempatan di akhir `<body>` agar seluruh elemen HTML sudah terbentuk sebelum AOS mulai mengobservasi elemen dengan `data-aos`.

**Dampak ke kode:** Tidak ada perubahan kode. Sesi pemahaman, tetapi pemahaman ini yang kemudian membantu proses debugging di prompt #5.

---

### 4. Permintaan implementasi: efek hover "terangkat"

**Prompt (disertai screenshot referensi visual):**
> "saya juga ingin ketika di hover ada ilusi terangkat seperti ini"

**Ringkasan hasil:** AI menjelaskan teknik "neobrutalism hover" (kombinasi `transform: translate()` + `box-shadow` solid offset yang membesar saat hover) dan memberikan CSS pengganti untuk `.experience-item:hover`.

**Dampak ke kode:** Referensi CSS untuk `style.css`, diterapkan manual.

---

### 5. Pertanyaan debugging: section Experience tidak tampil

**Prompt (disertai screenshot halaman kosong):**
> "kok gak muncul apa apa?"

**Konteks & tujuan:** Melaporkan bug nyata di halaman (judul "Experiences" tampil, tapi seluruh `experience-item` tidak terlihat sama sekali) untuk didiagnosis.

**Ringkasan hasil:** AI membaca ulang `index.html` secara langsung dan menemukan bahwa script `<script src=".../aos.js">` (pemuat library) hilang, hanya `AOS.init()` yang ada tanpa `AOS` pernah terdefinisi. Karena `aos.css` membuat semua elemen `[data-aos]` default `opacity: 0` sampai class `aos-animate` ditambahkan oleh JS, dan JS-nya tidak pernah berjalan, seluruh item tetap transparan selamanya. Solusi: menambahkan kembali baris `<script src="...aos.js">` sebelum `AOS.init()`.

**Dampak ke kode:** Perbaikan langsung teridentifikasi untuk `index.html`, diterapkan manual dan dikonfirmasi lewat DevTools Console.


## Ringkasan Peran AI

AI digunakan sebagai pair-programmer untuk: (1) menjelaskan mekanisme kode yang kompleks (scroll-driven animation, siklus hidup script AOS) sebelum digunakan, (2) menyusun draf kode CSS/HTML berdasarkan kebutuhan yang dijelaskan, dan (3) membantu diagnosis satu bug nyata (AOS tidak jalan). Kode yang disarankan ditinjau dan diterapkan secara manual oleh saya ke file proyek melalui panduan oleh AI.
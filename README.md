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
Nama : Gde Maharta Putra Wicaksana Ridjasa

NPM : 2506549051

Kelas : PBP A

Jadwal:
- Senin (15.00-16.40)
- Rabu (16.00-17.40)

# Tugas 1 

1. Ya, saya menggunakan elemen semantik seperti \<header>, \<nav>, \<main>, \<section>, dan \<footer> yang terlihat di struktur halaman: \<header class="site-header"> untuk navbar, \<main> yang membungkus tiga \<section> (Profile, Education, Experience) masing-masing dengan id unik untuk anchor navigation, dan \<footer class="site-footer"> di bagian bawah.

    Elemen-elemen ini membantu karena:

    - \<section> memisahkan konten berdasarkan topik yang jelas (profil, riwayat pendidikan, pengalaman), sehingga browser bisa memahami "blok" konten tanpa harus menebak dari class CSS saja
    - \<nav> menandai kumpulan link navigasi, membedakannya dari sekadar deretan \<a> biasa
    - Struktur ini juga memudahkan saya sendiri saat maintenance agar saya tahu persis section mana yang harus diedit tanpa membaca ulang seluruh dokumen
    
    Saya tidak menggunakan elemen \<article> atau \<aside> karena seluruh isi portofolio ini merupakan satu kesatuan narasi utama. Tidak ada konten mandiri yang dirancang untuk didistribusikan secara terpisah seperti kriteria \<article>, maupun informasi pendukung yang berada di luar alur baca utama seperti kriteria \<aside>. Oleh karena itu, pengelompokan menggunakan \<section> sudah tepat untuk merepresentasikan struktur halaman.

2. Tantangan utama justru muncul dari pola interaksi berbasis :hover yang saya pakai di section Experience. Detail pengalaman (.experience-detail) sengaja disembunyikan (max-height: 0; opacity: 0;) dan baru muncul saat card di-hover (.experience-item:hover .experience-detail), termasuk ikon "+" yang berputar jadi "×". Masalahnya, :hover tidak punya konsep yang sama di perangkat sentuh (mobile/tablet), tidak ada mouse yang bisa "melayang" di atas elemen. Ini artinya, tanpa penyesuaian lebih lanjut, pengguna mobile bisa jadi tidak akan pernah melihat isi detail pengalaman saya sama sekali, karena tidak ada cara untuk memicu state hover tersebut lewat sentuhan.

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

---
# Tugas 2

1. Alur dimulai ketika browser mengirim HTTP request ke server Django untuk sebuah path tertentu (misalnya `/education/`). Request ini pertama kali ditangkap oleh **urls.py proyek** (`portofolio/urls.py`), yang berperan sebagai router utama, di sini path kosong (`""`) di-*include* ke `main.urls`, sehingga semua path lain didelegasikan ke **urls.py aplikasi** (`main/urls.py`). Di urls.py aplikasi inilah path spesifik (misalnya `"education/"`) dicocokkan dengan sebuah **view** function (`show_education`) berdasarkan pattern yang terdaftar. View kemudian mengambil data dari **model** (`Education.objects.all().order_by('-started_year')`), yang merepresentasikan struktur data di database, lalu membungkus hasilnya ke dalam sebuah `context` (dictionary). Context ini diteruskan ke **template** (`education.html`) melalui `render()`, di mana data tersebut dirender menjadi HTML final sesuai logika tampilan (loop, kondisional, dsb). HTML jadi inilah yang dikirim kembali sebagai response dan ditampilkan browser kepada pengguna.

2. Data sebaiknya disimpan di model, bukan ditulis langsung di template, karena model memisahkan **data** dari **presentasi** (prinsip separation of concerns). Jika data di-hardcode di template, setiap penambahan atau perubahan data (misalnya menambah riwayat pendidikan baru) mengharuskan saya mengedit kode HTML secara manual dan melakukan deploy ulang karena rawan human error dan tidak scalable. Dengan model, data tersimpan di database dan dapat diubah lewat Django Admin tanpa menyentuh kode sama sekali, sehingga pemeliharaan jadi jauh lebih mudah dan aman (validasi tipe data ditangani otomatis oleh Django), serta memungkinkan pengembangan lanjutan seperti pencarian, filter, atau relasi antar data yang tidak mungkin dilakukan jika data hanya berupa teks statis di HTML.

3. `makemigrations` bertugas **membaca perubahan pada model** (`models.py`) dan menerjemahkannya menjadi file migrasi (blueprint perubahan skema database), tanpa benar-benar menyentuh database. Sementara `migrate` bertugas **menerapkan** file migrasi tersebut ke database sesungguhnya, sehingga skema tabel benar-benar berubah sesuai definisi model. Contoh kasus: saat saya menambahkan model `Education` baru (dengan field seperti `school_name`, `started_year`, `ended_year`) sekaligus mengubah `category` pada model `Experience` yang sudah ada dan perubahan ini tidak akan tercermin di database sampai saya menjalankan `makemigrations` (menghasilkan file migrasi baru yang mendeskripsikan pembuatan tabel Education dan perubahan kolom Experience), lalu `migrate` (benar-benar membuat tabel `main_education` dan mengubah struktur tabel `main_experience` di database).

## Progress

### Commit 1: Penambahan Model Education
- Menambahkan model `Education` pada `models.py` dengan field `school_name`, `major`, `grade`, `category` (choices jenjang pendidikan), `thumbnail`, `started_year`, dan `ended_year`.
- Menambahkan property `is_ongoing` untuk menentukan status pendidikan yang masih berlangsung, mengikuti pola yang sama dengan model `Experience`.

### Commit 2: Migration untuk Model Education
- Menjalankan `makemigrations` dan `migrate` untuk menerapkan model `Education` ke database, sekaligus menyesuaikan perubahan pada field `category` milik `Experience`.

### Commit 3: Pembuatan View dan Template Education
- Membuat view `show_education` yang mengambil seluruh data `Education`, mengurutkannya berdasarkan `started_year` secara menurun, dan meneruskannya ke context.
- Membuat template `education.html` untuk menampilkan riwayat pendidikan, termasuk logika kondisional untuk menampilkan status "masih berlangsung" saat `ended_year` kosong.
- Mendaftarkan path `education/` pada `urls.py` aplikasi `main`.

### Commit 4: Penulisan Unit Test
- Menambahkan minimal tiga kasus pengujian baru untuk memastikan halaman Education dapat diakses, menampilkan data dengan benar, dan menampilkan pesan yang sesuai saat data kosong.

## AI Disclosure

Tools yang digunakan: Claude Code (model Claude Sonnet 5), digunakan sebagai pair-programming assistant selama pengerjaan Education Section berbasis Django (model, view, dan pemahaman unit test).

Strategi prompting: Sama seperti Tugas 1, saya menggunakan AI terutama untuk meminta penjelasan konsep/mekanisme sebelum menuliskan implementasinya sendiri, bukan meminta kode akhir secara langsung. Contoh pertanyaan yang saya ajukan selama proses:

### Beberapa AI Interaction Log

### 1. Pertanyaan konsep: pengurutan data dan format tampilan rentang tahun

**Prompt:**
> "Bagaimana cara membuat started_year yang menentukan urutan education, kemudian started_year tersebut beserta dengan ended_year muncul di tampilan seperti started_year - ended_year?"

**Konteks & tujuan:** Memahami dua konsep berbeda yang perlu dipisahkan sebelum menulis kode: bagaimana mengontrol urutan data hasil query, dan bagaimana menampilkan dua field (`started_year`, `ended_year`) sebagai satu rentang tahun di template.

**Ringkasan hasil:** AI menjelaskan bahwa urutan QuerySet tidak terjamin secara default sehingga perlu method pengurutan eksplisit berdasarkan field acuan (menaik atau menurun), dan bahwa penggabungan `started_year - ended_year` murni logika template, bukan logika model, sehingga saya perlu tag kondisional di template untuk menangani kasus `ended_year` kosong (masih berlangsung) dengan memanfaatkan property `is_ongoing` yang sudah ada di model.

**Dampak ke kode:** Tidak ada kode yang diberikan langsung; hanya penjelasan konsep untuk saya implementasikan sendiri di `views.py` dan `education.html`.

---

### 2. Pertanyaan lanjutan: penerapan pengurutan di view.py

**Prompt:**
> "Selanjutnya untuk di bagian view.py. Bagaimana cara menampilkan Education section berdasarkan urutan?"

**Konteks & tujuan:** Menindaklanjuti pertanyaan sebelumnya secara lebih spesifik ke lokasi implementasinya, yaitu view yang menangani halaman Education.

**Ringkasan hasil:** AI menjelaskan bahwa pengurutan perlu dirangkai langsung saat pengambilan queryset (bukan diurutkan manual setelah data diambil, agar Django yang menangani di level query database), dan mengarahkan saya untuk mengikuti pola context yang sama seperti `show_experience` agar konsisten.

**Dampak ke kode:** Belum ada kode konkret, masih berupa arahan konsep untuk saya terapkan sendiri.

---

### 3. Permintaan syntax spesifik: method pengurutan menurun

**Prompt:**
> "arah urutannya adalah paling baru (paling atas) sampai dengan palling lama (paling bawah). Apa syntax untuk order tersebut?"

**Konteks & tujuan:** Setelah memahami konsepnya, saya butuh kepastian syntax persis untuk method QuerySet Django yang sesuai dengan arah urutan yang saya inginkan.

**Ringkasan hasil:** AI memberikan syntax `order_by('-started_year')`, menjelaskan bahwa tanda minus menandakan urutan menurun (nilai terbesar/terbaru dulu), berbeda dengan tanpa tanda minus yang menghasilkan urutan menaik.

**Dampak ke kode:** Syntax ini saya terapkan langsung pada queryset di `show_education` (`main/views.py`).

---

### 4. Pertanyaan pemahaman konsep: fungsi `reverse()` pada unit test

**Prompt:**
> "Apa maksud dari reverse pada self.client.get(reverse(\"main:show_experience\"))?"

**Konteks & tujuan:** Memahami fungsi `reverse()` yang muncul di `tests.py` sebelum menulis unit test serupa untuk Education, bukan sekadar meniru pola tanpa mengerti maksudnya.

**Ringkasan hasil:** AI menjelaskan bahwa `reverse()` mengubah nama URL (`app_name:url_name` yang didefinisikan di `urls.py`) menjadi path sebenarnya, sehingga test maupun template tidak perlu hardcode path secara manual dan tetap valid meskipun path di `urls.py` berubah di kemudian hari.

**Dampak ke kode:** Tidak ada perubahan kode langsung; pemahaman ini yang kemudian saya terapkan saat menulis unit test untuk halaman Education (`test_education_url_is_accessible`, dsb.) di `tests.py`.

## Ringkasan Peran AI

Untuk Tugas 2, AI digunakan sebagai pair-programmer untuk: (1) menjelaskan konsep pengurutan data (QuerySet ordering) dan pemisahan logika data vs tampilan, (2) memberikan syntax spesifik Django saat konsepnya sudah dipahami, dan (3) menjelaskan mekanisme `reverse()` pada unit test. Seluruh implementasi (model, view, template, unit test) tetap saya tuliskan sendiri berdasarkan penjelasan konsep dari AI, bukan hasil salin-tempel kode jadi dari AI.

---
# Tugas 3

1. `ModelForm` lebih disukai dibanding form HTML manual karena ia menghasilkan field form secara otomatis berdasarkan definisi model (`fields`, `widgets`, `labels` cukup dikonfigurasi sekali di `Meta`), sehingga validasi tipe data (misalnya `URLField` memvalidasi format URL, `PositiveIntegerField` menolak angka negatif) ditangani otomatis oleh Django tanpa saya menulis ulang logic validasi di HTML maupun view. Ini juga menjaga konsistensi: jika field di model berubah, form ikut menyesuaikan tanpa saya harus mengedit HTML satu per satu. Form manual rawan human error (nama field tidak sinkron dengan model, validasi tidak lengkap) dan lebih banyak kode yang harus dipelihara.

    `{% csrf_token %}` wajib disertakan karena Django menerapkan proteksi CSRF (Cross-Site Request Forgery) secara default untuk semua request `POST`. Tanpa token ini, Django akan menolak submit form dengan error 403 Forbidden. Token ini berfungsi sebagai bukti bahwa request `POST` benar-benar berasal dari form yang di-render oleh server yang sama (bukan dari situs pihak ketiga yang mencoba mengirim request atas nama pengguna yang sudah login), karena token unik ini digenerate per sesi/per form dan divalidasi ulang di sisi server saat form disubmit.

2. JSON lebih disukai dibanding XML dalam pengembangan web modern karena strukturnya jauh lebih ringkas (tidak perlu closing tag berulang seperti XML), sehingga ukuran payload lebih kecil dan lebih cepat ditransfer maupun di-parse. JSON juga native di JavaScript (`JSON.parse()`/`JSON.stringify()` sudah bawaan browser), sehingga sangat alami dipakai di aplikasi web modern yang banyak mengandalkan AJAX/fetch di sisi client. Hampir semua bahasa pemrograman modern (termasuk Python lewat `json` atau `serializers.serialize("json", ...)` di Django) punya dukungan JSON bawaan, membuatnya jadi format pertukaran data de facto antara backend dan frontend maupun antar layanan (API).

3. Ketika sebuah view mengembalikan data portofolio dalam format JSON (seperti `get_projects_json`, `get_experience_json`, `get_education_json`), alurnya adalah: (1) view mengambil data dari database dalam bentuk queryset/objek model Django (`Model.objects.all()`), (2) objek-objek ini **diserialisasi** menggunakan `serializers.serialize("json", queryset)` menjadi string JSON, karena objek model Django adalah objek Python kompleks (instance class) yang tidak bisa langsung dikirim sebagai response HTTP atau dipahami oleh client perlu diubah dulu menjadi format teks universal yang bisa dibaca lintas platform/bahasa, (3) string JSON ini dikembalikan lewat `HttpResponse` dengan `content_type="application/json"` agar client tahu cara menginterpretasikan isi response. Di sisi lain, saat data ini perlu ditampilkan kembali di halaman HTML (seperti `show_projects`, `show_experience`, `show_education`), string JSON tersebut perlu **dideserialisasi** kembali (`serializers.deserialize("json", ...)`) menjadi objek Python agar atributnya (`.title`, `.description`, dst.) bisa diakses dan dirender di template. Proses serialisasi-deserialisasi ini penting karena memisahkan representasi data (JSON, netral platform) dari representasi objek internal Django, sehingga data yang sama bisa dikonsumsi baik oleh halaman web (lewat deserialisasi) maupun oleh client lain seperti aplikasi mobile atau AJAX (langsung dari endpoint JSON mentah).

## Progress

### Commit 1:
- Menambahkan `ExperienceForm` dan `EducationForm` (`ModelForm`) pada `forms.py`, mengikuti pola `ProjectForm` yang sudah ada, lengkap dengan `labels` dan `widgets` kustom.
- Menambahkan view `create_experience`, `update_experience`, `delete_experience`, `create_education`, `update_education`, `delete_education` pada `views.py`.
- Mendaftarkan path terkait (`experience/add/`, `experience/<uuid:experience_id>/update/`, `experience/<uuid:experience_id>/delete/`, serta padanannya untuk education) pada `urls.py`.
- Menambahkan `get_experience_json` dan `get_education_json` yang menyerialisasi queryset menjadi JSON, didaftarkan pada path `api/experience/` dan `api/education/`.
- Mengubah `show_experience` dan `show_education` agar mengambil data lewat endpoint JSON tersebut lalu mendeserialisasinya kembali sebelum dikirim ke template, mengikuti pola `show_projects`.
- Membuat `experience_form.html` dan `education_form.html` yang mendukung mode create maupun update dalam satu template (`action` form berubah sesuai ada/tidaknya instance).
- Membuat komponen `experience_delete_modal.html` dan `education_delete_modal.html`, mengikuti pola `project_delete_modal.html`.
- Menambahkan tombol "Tambah", "Edit", dan modal konfirmasi hapus pada `experience.html` dan `education.html`.

## AI Disclosure

Tools yang digunakan: Claude Code (model Claude Sonnet 5).

Untuk Tugas 3 ini, saya cukup sering berdiskusi dengan AI, terutama saat membangun fitur CRUD untuk Experience dan Education berdasarkan pola yang sudah saya buat di bagian Projects.

**Saya:** "Saya sudah selesai bikin form buat Projects. Nah, sekarang saya bingung mulai dari mana buat bikin form yang sama buat Experience sama Education. Apakah polanya bisa persis sama?"

**AI:** Polanya bisa sama karena ketiganya sama-sama pakai `ModelForm`. Bedanya cuma field yang tersedia di tiap model, Experience punya `category` dan `thumbnail`, Education punya `started_year`/`ended_year`. Selama field di `Meta.fields` disesuaikan dengan model masing-masing, struktur form, view create, dan template-nya bisa direplikasi langsung.

---

**Saya:** "Terus kalau misal user mau ubah data yang sudah ada gimana? Apa formnya beda sendiri atau bisa pakai yang sama?"

**AI:** Bisa pakai form yang sama. Django `ModelForm` menerima parameter `instance=`, kalau diisi objek yang sudah ada, form otomatis terisi data lama dan saat disimpan akan meng-update baris itu, bukan membuat baru. Jadi cukup satu view dengan percabangan: kalau ada `instance`, berarti mode edit; kalau tidak, mode tambah baru.

---

**Saya:** "Terus buat hapus data gimana? Saya pengen ada konfirmasi dulu sebelum kehapus, biar gak kepencet gak sengaja."

**AI:** Bisa pakai elemen `popover` bawaan HTML sebagai modal konfirmasi, tanpa perlu JavaScript tambahan. Tombol "Hapus" membuka popover berisi pertanyaan konfirmasi, baru di dalamnya ada form kecil `method="post"` yang benar-benar memanggil view delete kalau user menekan "Ya, Hapus".

---

**Saya:** "Terakhir, saya masih agak bingung soal JSON ini. Kenapa harus diubah ke JSON dulu, terus diubah balik lagi? Kok muter-muter gitu?"

**AI:** Karena tujuannya beda-beda. Endpoint JSON (`get_experience_json`, dst.) itu buat siapa pun yang butuh data mentah, bisa dipakai aplikasi lain, AJAX, atau sekadar dicek manual lewat browser. Sementara halaman HTML (`show_experience`) butuh objek Python asli supaya bisa dipakai method-nya (`is_ongoing`, `get_category_display`), jadi data JSON itu perlu "dibongkar" lagi jadi objek lewat `deserialize()` sebelum dikirim ke template.

## Ringkasan Peran AI

AI berperan sebagai partner diskusi sekaligus penulis draf kode untuk fitur CRUD Experience dan Education (form, view, URL, template, modal konfirmasi hapus), berdasarkan pola yang sudah saya bangun sendiri di bagian Projects. Saya yang menempatkan, menyesuaikan, dan menguji kode tersebut langsung di proyek.

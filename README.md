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

1. Clone repository dan masuk ke foldernya:
   ```bash
   git clone <url-repo-ini>
   cd myportofolio
   ```
2. Buat dan aktifkan virtual environment:
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS / Linux
   source env/bin/activate
   ```
3. Install dependency, termasuk Django REST Framework (`djangorestframework~=3.18.3`):
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Siapkan database dan akun pemilik portofolio:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. (Opsional) Buat grup `Editor` lewat `/admin/`, lalu tambahkan akun yang boleh mengubah data.
6. Jalankan server di `http://localhost:8000`:
   ```bash
   python manage.py runserver
   ```
7. Jalankan test (gunakan `test main`, bukan `test` saja):
   ```bash
   python manage.py test main
   ```

Endpoint API dapat dibuka langsung di browser lewat Browsable API DRF, misalnya `/api/v1/experience/` dan `/api/v1/projects/`. Tambahkan `?format=json` untuk melihat JSON mentah.


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

---
# Tugas 4

## Progress

### Commit 1: Manajemen Hak Akses & Peran pada Projects
- Menambahkan view `update_project` yang membolehkan superuser maupun anggota grup `Editor` mengubah data project, sementara `create_project` dan `delete_project` tetap dibatasi hanya untuk superuser.
- Menambahkan pengecekan `request.user.is_superuser` / keanggotaan grup `Editor` (`request.user.groups.filter(name="Editor").exists()`) di sisi server, memicu `PermissionDenied` (403) untuk peran yang tidak berhak, dan `@login_required` untuk mengarahkan pengunjung tanpa login ke halaman login.
- Mendaftarkan path `projects/<uuid:project_id>/update/` pada `urls.py`.
- Menjadikan `projects_form.html` reusable untuk mode create maupun update (mengikuti pola `experience_form.html` yang sudah ada), dan mengirim variabel `is_editor` dari `show_projects` ke context agar `project.html` bisa menyembunyikan tombol Tambah/Edit/Hapus dari pengguna yang tidak berhak.

### Commit 2: Manajemen Hak Akses & Peran pada Experience
- Menerapkan pola yang sama seperti Projects pada `create_experience`, `update_experience`, dan `delete_experience`: `@login_required` untuk seluruh aksi, dibatasi hanya superuser untuk create/delete, dan superuser atau grup `Editor` untuk update.
- Mengirim variabel `is_editor` dari `show_experience` ke context, dan menyesuaikan `experience.html` agar tombol Tambah/Edit/Hapus hanya tampil untuk peran yang berhak.

### Commit 3: Fitur Interaktif Pemberian Star pada Experience
- Menambahkan relasi `ManyToManyField` ke `User` (`starred_by`, `related_name="starred_experiences"`) pada model `Experience`, mengikuti pola yang sudah ada pada `Project`, beserta migrasi database.
- Menambahkan view `toggle_star_experience` (`@login_required`, method POST) untuk memberi/membatalkan star, memastikan satu user hanya bisa memiliki satu status star per experience (mengandalkan sifat unik keanggotaan `ManyToManyField`).
- Membuat komponen `experience_star.html` yang menampilkan jumlah total star dan status star pengguna saat ini, mengikuti pola `project_star.html`.

### Commit 4: Review Integritas API & Keamanan Data
- Meninjau ulang `get_experience_json`, `get_education_json`, dan `get_projects_json` untuk memastikan tidak ada data sensitif milik user (seperti password) yang ikut terserialisasi, mengingat `get_projects_json` menggunakan `use_natural_foreign_keys=True` yang berpotensi menampilkan username lewat relasi `starred_by`.

## AI Disclosure

Tools yang digunakan: Claude Code (model Claude Sonnet 5), digunakan sebagai pair-programming assistant untuk memahami dan menerapkan pola otorisasi berbasis peran pada Tugas 4.

Strategi prompting: Berbeda dari tugas-tugas sebelumnya, kali ini saya lebih sering meminta AI untuk **menjelaskan pola dan memberi contoh kode sebagai referensi**, lalu saya yang menuliskan ulang dan menerapkannya sendiri ke file proyek, bukan meminta AI langsung mengedit file. Saya juga meminta AI menjelaskan konsep-konsep yang belum saya pahami sepenuhnya di tengah proses.

### Beberapa AI Interaction Log

### 1. Pertanyaan pemahaman: fungsi variabel `is_editor` di context

**Prompt:**
> "fungsi 'is_editor' di context di show_projects apa?"

**Konteks & tujuan:** Memahami kenapa pengecekan grup harus dihitung di Python (view), bukan langsung di template.

**Ringkasan hasil:** AI menjelaskan bahwa template Django tidak bisa memanggil method dengan argumen (`groups.filter(name="Editor")`), sehingga nilai boolean harus dihitung dulu di view lalu dikirim lewat context ke template.

**Dampak ke kode:** Tidak ada kode baru; pemahaman ini menjadi dasar saat saya menerapkan `is_editor` secara manual ke `show_experience`.

---

### 2. Permintaan cara pengujian: pembatasan hak akses di sisi server

**Prompt:**
> "gimana cara ngetesnya ya?" (terkait pembatasan hak akses 4 peran)

**Ringkasan hasil:** AI menyarankan skema pengujian manual: menyiapkan akun untuk tiap peran (pengunjung, user biasa, editor, superuser), mengakses URL aksi terproteksi secara langsung (bukan lewat tombol UI yang sudah disembunyikan), dan memverifikasi respons (redirect ke login vs 403) sesuai matriks peran.

**Dampak ke kode:** Tidak ada perubahan kode; digunakan sebagai panduan pengujian manual saya sendiri.

---

### 3. Permintaan review: keamanan endpoint JSON

**Prompt:**
> "periksa bagian [Integritas API & Keamanan Data]... sekarang"

**Ringkasan hasil:** AI meninjau `get_experience_json`, `get_education_json`, dan `get_projects_json`, menyoroti bahwa `use_natural_foreign_keys=True` pada `get_projects_json` berpotensi menampilkan username (bukan sekadar ID) lewat relasi `starred_by`, dan menyarankan opsi membatasi field yang diserialisasi.

**Dampak ke kode:** Rekomendasi diberikan; keputusan penerapan perbaikan (atau tidak) saya lakukan sendiri.

## Ringkasan Peran AI

Untuk Tugas 4, AI berperan sebagai pemandu konsep dan penyedia contoh kode referensi untuk pola otorisasi berbasis peran (grup `Editor`, pembatasan `is_superuser`), pengujian manual hak akses di sisi server, replikasi fitur star ke bagian Experience, serta review keamanan endpoint JSON. Seluruh perubahan pada `models.py`, `views.py`, `urls.py`, dan template tetap saya tuliskan dan terapkan sendiri secara manual ke proyek, termasuk menjalankan migrasi database dan pengujian di server lokal.

---
# Tugas 5

1. **Debouncing** adalah teknik menunda eksekusi sebuah fungsi sampai tidak ada event baru selama jeda waktu tertentu. Setiap event baru membatalkan timer sebelumnya (`clearTimeout`) dan memulainya lagi (`setTimeout`), sehingga fungsi hanya berjalan sekali setelah pengguna berhenti. Pada pencarian AJAX, ini penting karena tanpa debouncing setiap karakter yang diketik memicu satu request ke server. Mencari "Django" berarti enam request berturut-turut, padahal lima hasil pertama langsung tidak terpakai. Request berlebih membebani server dan jaringan, membuat tampilan berkedip karena daftar terus dirender ulang, dan membuka risiko response lama tiba setelah response baru lalu menimpa hasilnya. Dengan debouncing (300 ms di proyek ini), hanya satu request dikirim setelah pengguna selesai mengetik. Kombinasi dengan `AbortController` membatalkan request sebelumnya yang belum selesai. Debouncing berbeda dari throttling: debouncing menunggu event berhenti, sedangkan throttling membatasi fungsi hanya berjalan sekali per interval.

2. **`await`** menghentikan eksekusi di dalam `async function` sampai Promise yang ditunggu selesai, lalu mengembalikan nilai hasilnya. Pada `const response = await fetch(url)`, baris berikutnya baru berjalan setelah server membalas dan `response` berisi objek `Response` yang asli. Hal yang sama berlaku pada `await response.json()` untuk membaca body. Jika `await` tidak digunakan, `fetch()` tetap berjalan di belakang layar, tetapi kode di bawahnya langsung dieksekusi tanpa menunggu. Variabel `response` hanya berisi objek `Promise` (status pending), bukan `Response`. Akibatnya `response.ok` bernilai `undefined` sehingga pemeriksaan error salah, dan `response.json()` gagal karena Promise tidak punya method itu. Data yang dirender juga kosong atau salah. Error dari fetch yang gagal pun tidak tertangkap oleh `try/catch` karena Promise-nya tidak ditunggu.

3. **XSS (Cross-Site Scripting)** adalah serangan ketika penyerang menyisipkan kode JavaScript ke halaman web sehingga kode itu dijalankan di browser pengguna lain. Salah satu jenisnya adalah stored XSS, yaitu payload (misalnya judul `<img src="x" onerror="alert('XSS!')">`) disimpan ke database lalu dieksekusi setiap kali data itu ditampilkan. Dampaknya serius karena JavaScript tersebut bisa membaca cookie yang tidak ber-flag HttpOnly, termasuk `csrftoken`, lalu mengirim request POST atas nama korban, sehingga proteksi CSRF ikut tidak efektif. Data yang ditampilkan lewat AJAX lebih rentan karena template Django melakukan auto-escaping, yaitu `<` dan `>` diubah menjadi `&lt;` dan `&gt;`, sehingga browser menampilkannya sebagai teks. Saat data diambil lewat `fetch()` lalu disisipkan ke `innerHTML`, template Django tidak ikut campur, sehingga tidak ada escaping otomatis dan browser menganggap tag di dalam data sebagai HTML sungguhan. Karena itu, di proyek ini setiap nilai teks dari JSON dibungkus `escapeHtml`, dan input dibersihkan di server dengan `strip_tags` pada method `clean_<field>` di `ExperienceForm` sebagai lapisan pertahanan kedua.

## Progress

### Commit 1: Penerapan AJAX, debouncing, modal, toast, dan perlindungan XSS pada Experience
- Mengubah `get_experience_json` agar menyusun JSON secara manual dengan `JsonResponse`, termasuk `star_count`, `is_starred`, `starred_by_names`, `category_display`, dan `is_ongoing`, serta mendukung filter `?title=`.
- Menyederhanakan `show_experience` agar hanya merender kerangka halaman, dan mengubah `experience.html` menjadi wadah kosong dengan state loading, error, empty, dan grid yang diisi lewat `fetch()`.
- Menambahkan pencarian berdasarkan judul lewat AJAX dengan debouncing 300 ms dan `AbortController`.
- Membuat komponen `experience_form_modal.html` (Popover API) dan view `create_experience_ajax` (`@require_POST`, pemeriksaan `is_superuser` di dalam view, validasi `ExperienceForm`, respons 201/400/403) dengan route `experience/add-ajax/`.
- Mengirim form dengan `fetch()` dan `FormData` beserta header `X-CSRFToken`, memperbarui daftar tanpa reload, serta menampilkan toast untuk sukses dan pesan error dari server.
- Menambahkan `escapeHtml` pada setiap nilai yang disisipkan ke `innerHTML`, serta `clean_title` dan `clean_description` berbasis `strip_tags` pada `ExperienceForm`.

## AI Disclosure

Tools yang digunakan: Claude Code (model Claude Sonnet 5.5), digunakan untuk mereview kebenaran pengerjaan Tugas 05 terhadap instruksi tugas dan membandingkannya dengan hasil pengerjaan tutorial 5 sebagai panduan pengerjaan tugas 05.


---
# Tugas 6

### Tugas 6

1. **REST (Representational State Transfer)** adalah gaya arsitektur untuk merancang web API, bukan library atau format data. Tiga gagasan utamanya yang saya terapkan: data diperlakukan sebagai *resource* yang ditunjuk oleh URL (`/api/v1/experience/` untuk kumpulan, `/api/v1/experience/<uuid>/` untuk satu data), HTTP method menyatakan tindakan (GET membaca, POST membuat, PUT/PATCH mengubah, DELETE menghapus) sehingga tindakan tidak ditulis di URL, dan klien bertukar *representasi* data (JSON), bukan objek Python. Mengembalikan JSON saja belum cukup untuk disebut RESTful. Endpoint Tugas 5 saya seperti `POST /experience/add-ajax/` dan `POST /experience/<uuid>/delete/` memang mengembalikan JSON atau redirect, tetapi tindakannya ditulis di URL dan semua perubahan memakai POST. Di Tugas 6 keduanya menjadi `POST /api/v1/experience/` dan `DELETE /api/v1/experience/<uuid>/`, dengan status HTTP yang bermakna (201, 204, 400, 403, 404).

    **PUT** mengirim representasi pengganti yang utuh, sehingga semua field wajib harus dikirim. Di test saya, PUT yang hanya berisi `title` ditolak dengan 400 karena `description` wajib. **PATCH** hanya mengirim field yang ingin diubah (`partial=True` di serializer), field lain tetap memakai nilai lama. PUT cocok saat klien memang memegang seluruh data dan ingin menggantinya, misalnya form edit yang mengirim semua field sekaligus. PATCH cocok untuk perubahan sebagian, misalnya Editor yang hanya mengganti kategori pengalaman dari `internship` menjadi `part-time`. Modal edit di halaman Experience saya memakai PATCH.

2. **Serializer** pada DRF bekerja dua arah. Saat GET, serializer mengubah objek model menjadi tipe data Python yang siap dirender menjadi JSON (*serialization*). Saat POST/PUT/PATCH, serializer memvalidasi `request.data` lalu menyimpannya lewat `.save()` (*deserialization*). Di `ExperienceSerializer`, saya menentukan `fields` secara eksplisit, membuat `id` dan `started_at` read-only, menambahkan `category_display` dan `is_ongoing` sebagai field read-only, serta memvalidasi `title` dan `description` dengan `strip_tags` di `validate_<field>`. Field star (`star_count`, `is_starred`, `starred_by_names`) saya ekstrak ke `StarInfoMixin` agar dipakai bersama oleh `ProjectSerializer` dan `ExperienceSerializer`.

    Dibandingkan merakit dictionary manual dengan `JsonResponse` seperti di Tutorial 05, keuntungannya: (1) kontrak data ditulis sekali dan dipakai untuk daftar, detail, maupun hasil create/update, sehingga tidak ada perulangan `data.append({...})` yang bisa tidak sinkron; (2) validasi input dan pesan error per field (`{"title": ["..."]}`) dihasilkan otomatis, termasuk validasi bawaan dari model seperti `URLField` dan pilihan `category`; (3) field read-only otomatis diabaikan saat input, sehingga klien tidak bisa memalsukan `star_count`; dan (4) logika yang sama bisa dipakai ulang lewat mixin, bukan disalin ke setiap view.

3. **Autentikasi** menjawab "siapa pengirim request ini", sedangkan **otorisasi** menjawab "bolehkah ia melakukan tindakan ini". Di DRF keduanya dipisahkan: authentication class (`SessionAuthentication`) membaca session Django lalu mengisi `request.user`, kemudian permission class (`IsPortfolioOwnerOrEditorOrReadOnly`, `IsAuthenticated`) memutuskan apakah request diteruskan ke isi view. Pengunjung tanpa login tidak ditolak di tahap autentikasi, tetapi diperlakukan sebagai anonim dan baru ditolak di tahap permission dengan 403.

    Hak akses harus diperiksa di server karena menyembunyikan tombol di template hanya mengatur tampilan. Siapa pun tetap bisa mengirim request langsung, misalnya lewat DevTools Console, `curl`, atau Browsable API, tanpa pernah melihat tombolnya. Jika server tidak memeriksa, pengguna biasa bisa mengirim `DELETE /api/v1/experience/<uuid>/` dan datanya benar-benar terhapus. Karena itu test saya (`test_guest_and_visitor_cannot_write`, `test_editor_can_update_but_not_create_or_delete`) memanggil API secara langsung dan memeriksa isi database, bukan hanya memastikan tombolnya tidak tampil.

4. `SessionAuthentication` mengandalkan cookie session yang **dikirim otomatis oleh browser** ke domain kita, termasuk ketika request dipicu oleh halaman dari situs lain. Tanpa token CSRF, situs jahat bisa membuat korban yang sedang login mengirim `POST` atau `DELETE` ke API portofolio, dan server akan menganggapnya sah karena cookie session-nya valid. Token CSRF membuktikan bahwa request berasal dari halaman kita sendiri, karena situs lain tidak bisa membaca nilai cookie `csrftoken` untuk mengisi header `X-CSRFToken`. Karena itu `sendExperience()` selalu menyertakan header tersebut, dan saya menambahkan `{% csrf_token %}` di halaman agar cookie-nya tetap terbentuk untuk pengguna biasa dan Editor yang tidak melihat form.

    `force_authenticate` melewati proses autentikasi: `APIClient` langsung menetapkan `request.user` tanpa session dan tanpa login, sehingga pemeriksaan CSRF milik `SessionAuthentication` tidak pernah dijalankan. Test dengan `force_authenticate` hanya membuktikan logika permission, bukan perlindungan CSRF. Untuk membuktikannya, saya memakai `APIClient(enforce_csrf_checks=True)` dan `.login()` yang membuat session sungguhan. `test_session_write_without_csrf_is_rejected` membuktikan PATCH dari Editor tanpa token ditolak 403 dan data tidak berubah, sedangkan `test_session_write_with_csrf_succeeds` membuktikan request dengan token yang benar diterima.


## Progress

### Commit 1: Serializer dan API DRF untuk Experience
- Menambahkan `ExperienceSerializer` (`ModelSerializer`) dengan `fields` eksplisit, field read-only `category_display`, `is_ongoing`, `star_count`, `is_starred`, dan `starred_by_names`, serta validasi `title` dan `description` berbasis `strip_tags`.
- Menambahkan API view berbasis fungsi `experience_list` (GET, POST, pencarian `?title=`), `experience_detail` (GET, PUT, PATCH, DELETE), dan `experience_star` (POST) dengan `SessionAuthentication`.
- Memasang `IsPortfolioOwnerOrEditorOrReadOnly` pada daftar/detail dan `IsAuthenticated` pada star, lalu mendaftarkan route `api:experience-list`, `api:experience-detail`, dan `api:experience-star` di bawah `/api/v1/experience/`.

### Commit 2: Integrasi halaman Experience dengan API DRF
- Mengubah `experience.html` agar menampilkan, mencari, menambah, memberi star, dan menghapus data lewat `/api/v1/experience/` tanpa reload, dengan kontrak JSON baru (`experience.id`, `experience.title`, bukan `item.fields`/`item.pk`).
- Menambahkan mode edit pada modal form yang mengirim PATCH, sehingga Editor dan pemilik dapat mengubah data dari halaman yang sama.
- Menyatukan request tulis di `sendExperience()` yang selalu mengirim JSON, header `X-CSRFToken`, dan menampilkan error 400/403 lewat toast. Menambahkan `{% csrf_token %}` di halaman agar cookie CSRF tetap terbentuk untuk pengguna biasa.

### Commit 3: Test API Experience
- Menambahkan `ExperienceAPITest` (`APITestCase`) yang menguji setiap peran: pengunjung dan pengguna biasa ditolak menulis, Editor boleh PUT/PATCH tetapi ditolak POST/DELETE, dan pemilik boleh membuat, mengubah, serta menghapus data, dengan pemeriksaan isi database pada setiap penolakan.
- Menguji validasi input, star (termasuk penolakan pengunjung dan 405 untuk GET), field read-only, 404, serta CSRF dengan `APIClient(enforce_csrf_checks=True)` dan `.login()`.
- Menyesuaikan test halaman Experience di `tests.py` dengan endpoint API baru.

### Commit 4–5: Refactor serializer dan view
- Mengekstrak `StarInfoMixin` agar field star dipakai bersama oleh `ProjectSerializer` dan `ExperienceSerializer`, serta helper `clean_text` untuk validasi teks dan `toggle_star` untuk logika star di kedua endpoint.
- Memperjelas pesan error di toast dengan menyertakan nama field (misalnya "Judul: ...").

### Commit 6–7: Fitur tambahan di halaman Experience
- Menambahkan filter kategori lewat parameter `?category=` di API dan dropdown di halaman.
- Memperbarui hanya kartu yang diberi star dari response API, tanpa memuat ulang seluruh daftar.
- Mengganti `window.confirm` dengan modal konfirmasi hapus, serta menampilkan error validasi di bawah field yang salah di dalam modal.

### Commit 8: Test tambahan
- Menambahkan test filter kategori dan test yang membuktikan jumlah query tidak bertambah seiring jumlah data (pencegahan N+1 query lewat `prefetch_related("starred_by")`).

### Commit 9–10: Docstring dan perbaikan
- Menambahkan docstring pada modul, kelas, dan view di `serializers.py`, `permissions.py`, dan `api_views.py`. Docstring ini sebenarnya disebut di commit refactor sebelumnya, tetapi baru benar-benar ikut di commit ini.
- Mengembalikan listener pencarian debounce yang sempat terhapus, dan merapikan pemanggilan `fetchExperience()` serta label modal.

# AI Disclosure & Analisis Kritis Keterbatasan AI

Dalam pengerjaan Tugas 6, saya menggunakan **Claude Code** sebagai AI coding assistant yang membantu proses pengembangan proyek. Penggunaan AI dilakukan dengan menjadikan panduan resmi Tugas 6 sebagai acuan agar implementasi tetap sesuai dengan instruksi, kebutuhan, dan kriteria penilaian yang telah ditentukan. Selain membantu proses pengerjaan, Claude Code juga digunakan untuk meninjau dan memeriksa kembali hasil implementasi guna meningkatkan ketelitian serta meminimalkan kesalahan.

### Tools yang Digunakan:
- **Claude Code:** Digunakan sebagai pendamping dalam proses pengembangan, pemberi arahan teknis, serta alat bantu untuk melakukan pemeriksaan dan evaluasi terhadap hasil pengerjaan.

### Bagian yang Dibantu AI:

1. **Pemahaman Instruksi dan Analisis Kebutuhan:** Membantu memahami panduan Tugas 6, mengidentifikasi kebutuhan implementasi, serta memastikan fitur dan komponen yang dikembangkan mengacu pada ketentuan tugas.

2. **Pendampingan Implementasi:** Memberikan arahan, rekomendasi, dan alternatif solusi teknis selama proses pengembangan proyek. Setiap implementasi tetap diarahkan berdasarkan kebutuhan proyek dan panduan tugas.

3. **Identifikasi dan Penyelesaian Kendala:** Membantu menganalisis error, mengidentifikasi kemungkinan penyebab permasalahan, serta memberikan rekomendasi perbaikan ketika ditemukan kendala selama proses pengerjaan.

4. **Code Review dan Pemeriksaan Akhir:** Melakukan peninjauan ulang terhadap kode dan hasil implementasi untuk memeriksa konsistensi struktur, ketepatan fungsionalitas, serta kesesuaiannya dengan panduan Tugas 6.

### Analisis Kritis Keterbatasan AI & Perbaikan Manual:

1. **Ketepatan terhadap Instruksi Tugas:** Rekomendasi AI tidak selalu secara otomatis mencerminkan seluruh ketentuan dalam panduan tugas. Oleh karena itu, saya tetap menjadikan panduan resmi Tugas 6 sebagai acuan utama dan meninjau kembali setiap rekomendasi yang diberikan.

2. **Kesesuaian Implementasi:** Solusi yang disarankan AI belum tentu menjadi pendekatan paling sesuai dengan kebutuhan proyek. Saya melakukan evaluasi terhadap setiap saran agar implementasi tidak menyimpang dari tujuan dan kebutuhan yang telah ditentukan.

3. **Potensi Kesalahan Kode:** Hasil analisis maupun rekomendasi perbaikan dari AI masih berpotensi mengandung kesalahan. Oleh karena itu, saya menggunakan Claude Code untuk melakukan pemeriksaan berulang dan memastikan bagian yang diperbaiki tetap konsisten dengan keseluruhan implementasi.

4. **Validasi Hasil Akhir:** Pemeriksaan yang dilakukan AI tidak sepenuhnya menjamin bahwa seluruh fungsionalitas berjalan sebagaimana mestinya. Saya tetap bertanggung jawab untuk meninjau hasil pengerjaan dan memastikan kesesuaiannya dengan ketentuan tugas.

### Kesimpulan Reflektif

Penggunaan Claude Code dalam pengerjaan Tugas 6 membantu saya menjalankan proses pengembangan secara lebih terarah dan teliti. AI tidak hanya dimanfaatkan sebagai pendamping dalam memahami panduan dan mengimplementasikan kebutuhan tugas, tetapi juga sebagai sarana untuk melakukan pemeriksaan ulang terhadap hasil pengerjaan. Meskipun demikian, AI tetap memiliki keterbatasan sehingga setiap rekomendasi perlu ditinjau secara kritis. Tanggung jawab atas keputusan implementasi, validasi, dan hasil akhir proyek tetap berada pada saya sebagai pengembang.
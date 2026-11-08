# IDENTIFIKASI 9 DATASET MACHINE LEARNING
**Kategori: Binary, Multiclass, dan Multilabel**

## A. Pengertian

- **Binary classification** adalah klasifikasi dengan satu target yang memiliki dua kelas.
- **Multiclass classification** adalah klasifikasi dengan satu target yang memiliki lebih dari dua kelas. Setiap data umumnya masuk ke satu kelas.
- **Multilabel classification** adalah klasifikasi ketika satu data dapat memiliki lebih dari satu label sekaligus.
- **Classification** digunakan jika target berupa kelas/kategori.
- **Regression** digunakan jika target berupa nilai angka kontinu yang ingin diprediksi.


---

# B. DATASET BINARY

## 1. Bank Note Authentication UCI Data

- **Tujuan:** Menentukan apakah uang kertas asli atau palsu.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target yang diprediksi berupa kategori keaslian uang, bukan angka kontinu.
- **Kategori:** Binary classification.
- **Alasan binary:** Target hanya memiliki dua kelas, yaitu uang asli dan uang palsu.
- **Output:** 1 kolom target (`class`) dengan 2 kemungkinan label:
  - `0` = uang asli.
  - `1` = uang palsu.
- **Ukuran dataset:** 1.372 baris dan 5 kolom.
- **Fitur:** 4 fitur input dan 1 kolom target.
  - `variance`: tingkat variasi pola gambar uang setelah transformasi wavelet.
  - `skewness`: tingkat kemencengan distribusi pola gambar.
  - `curtosis`: ukuran keruncingan distribusi pola gambar.
  - `entropy`: ukuran informasi atau keragaman pola gambar.
  - `class`: label keaslian uang (target).
- **Sumber:** https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data

## 2. Water Potability

- **Tujuan:** Memprediksi apakah air layak dikonsumsi atau tidak berdasarkan karakteristik kualitas air.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target berupa kategori air layak atau tidak layak minum.
- **Kategori:** Binary classification.
- **Alasan binary:** Hanya terdapat dua kelas pada kolom `Potability`, yaitu 0 dan 1.
- **Output:** 1 kolom target (`Potability`) dengan 2 kemungkinan label:
  - `0` = tidak layak diminum.
  - `1` = layak diminum.
- **Ukuran dataset:** 3.276 baris dan 10 kolom.
- **Fitur:** 9 fitur input dan 1 kolom target.
  - `ph`: tingkat keasaman atau kebasaan air.
  - `Hardness`: tingkat kesadahan air.
  - `Solids`: jumlah zat padat terlarut.
  - `Chloramines`: kadar kloramin.
  - `Sulfate`: kadar sulfat.
  - `Conductivity`: kemampuan air menghantarkan listrik.
  - `Organic_carbon`: kadar karbon organik.
  - `Trihalomethanes`: kadar trihalometana.
  - `Turbidity`: tingkat kekeruhan air.
  - `Potability`: status kelayakan air untuk diminum (target).
- **Sumber:** https://www.kaggle.com/datasets/adityakadiwal/water-potability

## 3. Heart Failure Prediction

- **Tujuan:** Memprediksi apakah seseorang memiliki indikasi penyakit jantung berdasarkan karakteristik kesehatan.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target `HeartDisease` berupa kategori ada atau tidaknya penyakit jantung.
- **Kategori:** Binary classification.
- **Alasan binary:** Target hanya memiliki dua kelas, yaitu 0 (tidak terindikasi penyakit jantung) dan 1 (terindikasi penyakit jantung).
- **Output:** 1 kolom target (`HeartDisease`) dengan 2 kemungkinan label:
  - `0` = tidak terindikasi penyakit jantung.
  - `1` = terindikasi penyakit jantung.
- **Ukuran dataset:** 918 baris dan 12 kolom.
- **Fitur:** 11 fitur input dan 1 kolom target.
  - `Age`: usia pasien.
  - `Sex`: jenis kelamin.
  - `ChestPainType`: jenis nyeri dada.
  - `RestingBP`: tekanan darah saat istirahat.
  - `Cholesterol`: kadar kolesterol.
  - `FastingBS`: kadar gula darah puasa dalam bentuk kategori 0/1.
  - `RestingECG`: hasil elektrokardiogram saat istirahat.
  - `MaxHR`: denyut jantung maksimum.
  - `ExerciseAngina`: ada atau tidaknya angina saat berolahraga.
  - `Oldpeak`: nilai depresi segmen ST.
  - `ST_Slope`: kemiringan segmen ST saat latihan.
  - `HeartDisease`: status penyakit jantung (target).
- **Sumber:** https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

---

# C. DATASET MULTICLASS

## 4. Iris Species

- **Tujuan:** Mengklasifikasikan jenis bunga Iris berdasarkan ukuran bagian bunganya.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target berupa nama jenis bunga, bukan nilai angka kontinu.
- **Kategori:** Multiclass classification.
- **Alasan multiclass:** Terdapat tiga kelas jenis bunga Iris.
- **Output:** 1 kolom target (`Species` atau `class`) dengan 3 kemungkinan label:
  - Iris-setosa.
  - Iris-versicolor.
  - Iris-virginica.
- **Ukuran dataset:** 150 baris dan 5 kolom.
- **Fitur:** 4 fitur input dan 1 kolom target.
  - `SepalLengthCm`: panjang kelopak bunga.
  - `SepalWidthCm`: lebar kelopak bunga.
  - `PetalLengthCm`: panjang mahkota bunga.
  - `PetalWidthCm`: lebar mahkota bunga.
  - `Species`: jenis bunga Iris (target).
- **Sumber:** https://www.kaggle.com/datasets/uciml/iris

## 5. Car Evaluation Data Set

- **Tujuan:** Mengklasifikasikan tingkat kelayakan atau penerimaan mobil berdasarkan beberapa karakteristik.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target berupa kategori tingkat penerimaan mobil.
- **Kategori:** Multiclass classification.
- **Alasan multiclass:** Target memiliki empat kelas, yaitu tidak layak, cukup, baik, dan sangat baik.
- **Output:** 1 kolom target (`class`) dengan 4 kemungkinan label:
  - `unacc` = tidak dapat diterima.
  - `acc` = dapat diterima.
  - `good` = baik.
  - `vgood` = sangat baik.
- **Ukuran dataset:** 1.728 baris dan 7 kolom.
- **Fitur:** 6 fitur input dan 1 kolom target.
  - `buying`: tingkat harga pembelian mobil.
  - `maint`: biaya perawatan mobil.
  - `doors`: jumlah pintu mobil.
  - `persons`: kapasitas penumpang.
  - `lug_boot`: ukuran bagasi.
  - `safety`: tingkat keamanan mobil.
  - `class`: kategori kelayakan mobil (target).
- **Sumber:** https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set

## 6. Flowers Recognition

- **Tujuan:** Mengenali dan mengklasifikasikan jenis bunga berdasarkan gambar.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Sistem menentukan kategori jenis bunga dari gambar yang diberikan.
- **Kategori:** Multiclass classification.
- **Alasan multiclass:** Dataset memiliki lima kelas bunga. Setiap gambar diberi satu label jenis bunga.
- **Output:** 1 label kelas untuk setiap gambar, dengan 5 kemungkinan label:
  - Daisy/chamomile.
  - Dandelion.
  - Rose.
  - Sunflower.
  - Tulip.
- **Ukuran dataset:** Sekitar 4.242 gambar menurut deskripsi dataset. Dataset disimpan sebagai file gambar dalam folder kelas, bukan tabel CSV biasa. Karena itu, jumlah kolom tabel tidak berlaku secara langsung. Jika dibuat tabel metadata sederhana, setiap baris dapat mewakili satu gambar dengan kolom nama file/lokasi gambar dan label.
- **Fitur:** Fitur berasal dari gambar, seperti informasi warna, bentuk, tekstur, dan pola visual bunga. Gambar perlu melalui proses pengolahan seperti resize dan normalisasi sebelum digunakan pada model.
- **Sumber:** https://www.kaggle.com/datasets/alxmamaev/flowers-recognition

---

# D. DATASET MULTILABEL

## 7. ArXiv Multi-Label Text Classification Datasets

- **Tujuan:** Mengelompokkan artikel atau abstrak penelitian ArXiv ke dalam satu atau beberapa kategori bidang ilmu.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target yang diprediksi adalah kategori/topik penelitian, bukan nilai numerik kontinu.
- **Kategori:** Multilabel classification.
- **Alasan multilabel:** Satu artikel penelitian dapat memiliki lebih dari satu kategori atau bidang ilmu sekaligus.
- **Output:** Beberapa label untuk satu artikel. Jumlah label yang tersedia bergantung pada versi/file yang digunakan. Deskripsi dataset menyebutkan versi 90K dan 34K; versi yang lebih sederhana juga menyediakan skenario 4 label. Jadi, jumlah label perlu dipastikan kembali dari file yang dipilih.
- **Ukuran dataset:** Tersedia versi sekitar 90.000 data dan versi sekitar 34.000 data. Jumlah kolom bergantung pada file dan versi yang diunduh; struktur datanya memuat informasi teks artikel (misalnya abstrak) dan kategori/label. Periksa file CSV sebelum menetapkan jumlah kolom final.
- **Fitur:**
  - Judul artikel: informasi topik penelitian.
  - Abstrak: ringkasan isi penelitian yang menjadi sumber informasi teks.
  - Kategori/subject: satu atau beberapa bidang/topik penelitian yang menjadi label target.
  - Teks biasanya perlu diubah menjadi representasi numerik, misalnya TF-IDF atau embedding, sebelum diproses model.
- **Sumber:** https://www.kaggle.com/datasets/kelixirr/arxiv-multi-label-text-classification-datasets

## 8. Birds (Zenodo)

- **Tujuan:** Memprediksi label burung berdasarkan karakteristik audio/suara.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target berupa label kategori burung yang dapat muncul pada satu rekaman.
- **Kategori:** Multilabel classification.
- **Alasan multilabel:** Satu data audio dapat dikaitkan dengan lebih dari satu label burung, sehingga beberapa label dapat bernilai aktif secara bersamaan.
- **Output:** 19 kolom label untuk setiap data. Setiap label menunjukkan ada atau tidaknya kategori burung tertentu. Satu data dapat memiliki lebih dari satu label aktif.
- **Ukuran dataset:** 645 baris dan 279 atribut/kolom, terdiri dari 260 fitur input dan 19 kolom label.
- **Fitur:** Fitur input merupakan karakteristik audio yang telah diekstraksi dari suara burung. Fitur tersebut digunakan untuk mengenali pola suara, sedangkan 19 kolom label menunjukkan kategori burung.
- **Sumber:** https://zenodo.org/records/21466113?preview_file=birds.zip

## 9. Emotions (Zenodo)

- **Tujuan:** Memprediksi emosi yang berkaitan dengan sebuah musik berdasarkan karakteristik audio.
- **Jenis Permasalahan:** Classification.
- **Alasan classification:** Target berupa kategori emosi yang dapat muncul pada musik.
- **Kategori:** Multilabel classification.
- **Alasan multilabel:** Satu lagu dapat memiliki lebih dari satu emosi sekaligus, misalnya bahagia dan menenangkan.
- **Output:** 6 kolom label emosi. Beberapa label dapat aktif pada satu data musik.
  - amazed-surprised.
  - happy-pleased.
  - relaxing-calm.
  - quiet-still.
  - sad-lonely.
  - angry-aggressive.
- **Ukuran dataset:** 593 baris dan 78 atribut/kolom, terdiri dari 72 fitur input dan 6 kolom label.
- **Fitur:** Fitur input merupakan karakteristik audio yang telah diekstraksi, seperti spectral centroid, spectral rolloff, spectral flux, MFCC, dan karakteristik audio lainnya. Enam kolom label menunjukkan emosi yang berkaitan dengan musik.
- **Sumber:** https://zenodo.org/records/21466113?preview_file=emotions.zip

---

# E. RINGKASAN 9 DATASET

| No. | Dataset | Kategori | Jenis Tugas | Jumlah Data | Jumlah Kolom/Atribut | Output |
|---|---|---|---|---:|---:|---|
| 1 | Bank Note Authentication | Binary | Classification | 1.372 baris | 5 kolom | 1 target, 2 kelas |
| 2 | Water Potability | Binary | Classification | 3.276 baris | 10 kolom | 1 target, 2 kelas |
| 3 | Heart Failure Prediction | Binary | Classification | 918 baris | 12 kolom | 1 target, 2 kelas |
| 4 | Iris Species | Multiclass | Classification | 150 baris | 5 kolom | 1 target, 3 kelas |
| 5 | Car Evaluation | Multiclass | Classification | 1.728 baris | 7 kolom | 1 target, 4 kelas |
| 6 | Flowers Recognition | Multiclass | Classification | ±4.242 gambar | Tidak berbentuk tabel CSV | 1 label per gambar, 5 kelas |
| 7 | ArXiv Multi-Label | Multilabel | Classification | ±34.000 atau ±90.000 data | Bergantung versi/file | Beberapa label; versi sederhana 4 label |
| 8 | Birds | Multilabel | Classification | 645 baris | 279 atribut | 19 label |
| 9 | Emotions | Multilabel | Classification | 593 baris | 78 atribut | 6 label |

---

# F. TABEL SUMBER DATASET

| No. | Nama Dataset | Platform/Sumber | Tautan |
|---|---|---|---|
| 1 | Bank Note Authentication | Kaggle / UCI | https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data |
| 2 | Water Potability | Kaggle | https://www.kaggle.com/datasets/adityakadiwal/water-potability |
| 3 | Heart Failure Prediction | Kaggle | https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction |
| 4 | Iris Species | Kaggle / UCI | https://www.kaggle.com/datasets/uciml/iris |
| 5 | Car Evaluation | Kaggle / UCI | https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set |
| 6 | Flowers Recognition | Kaggle | https://www.kaggle.com/datasets/alxmamaev/flowers-recognition |
| 7 | ArXiv Multi-Label Text Classification | Kaggle | https://www.kaggle.com/datasets/kelixirr/arxiv-multi-label-text-classification-datasets |
| 8 | Birds | Zenodo | https://zenodo.org/records/21466113 |
| 9 | Emotions | Zenodo | https://zenodo.org/records/21466113 |

---

# G. KESIMPULAN

Berdasarkan identifikasi sembilan dataset, seluruh dataset tersebut termasuk **classification**, bukan regression, karena target yang diprediksi berupa kelas atau kategori.

Perbedaannya terletak pada jumlah dan bentuk label:
1. **Binary:** satu kolom target dengan dua kemungkinan kelas.
2. **Multiclass:** satu kolom target dengan lebih dari dua kemungkinan kelas.
3. **Multilabel:** satu data dapat memiliki beberapa label sekaligus, sehingga target direpresentasikan dalam beberapa kolom label atau kumpulan label.

Jumlah baris dan kolom dapat berbeda bergantung pada versi dataset yang diunduh. Khusus dataset gambar Flowers Recognition, data berupa file gambar sehingga tidak memiliki struktur kolom CSV seperti dataset tabular. Untuk ArXiv, jumlah data dan label juga bergantung pada versi/file yang dipilih.

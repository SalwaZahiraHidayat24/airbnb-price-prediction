# Airbnb Price Prediction

## Deskripsi Proyek

Proyek ini merupakan tugas praktikum mata kuliah Machine Learning yang bertujuan untuk menganalisis dan memprediksi harga penginapan Airbnb di New York City menggunakan Python dan Jupyter Notebook. Praktikum ini mencakup pengolahan dan analisis data serta pembangunan model Machine Learning untuk mempelajari pola harga penginapan berdasarkan karakteristik yang terdapat dalam dataset.

## Sumber Dataset

Dataset yang digunakan adalah **New York City Airbnb Open Data** dari Kaggle.

- **Platform:** Kaggle
- **Pembuat dataset:** Dgomonov
- **Periode data:** 2019
- **Nama file:** `AB_NYC_2019.csv`
- **Tautan dataset:** [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

Dataset berisi informasi mengenai listing Airbnb di New York City, seperti lokasi penginapan, jenis kamar, harga, jumlah ulasan, dan ketersediaan penginapan.

## Tujuan Analisis

- Membersihkan data dari nilai yang hilang serta mengidentifikasi data duplikat dan outlier.
- Melakukan transformasi data numerik dan kategorikal.
- Memahami karakteristik dataset melalui Exploratory Data Analysis (EDA).
- Membagi dataset menjadi data latih dan data uji.
- Membangun model prediksi harga penginapan.
- Mengevaluasi performa model menggunakan MAE, RMSE, dan R² Score.
- Menyimpan model yang telah dilatih agar dapat digunakan kembali.

## Tools dan Libraries

- **Jupyter Notebook:** Menulis dan menjalankan kode Python.
- **Kaggle:** Sumber dataset.
- **Pandas:** Pengolahan dan manipulasi data.
- **NumPy:** Operasi numerik.
- **Matplotlib:** Visualisasi data.
- **Seaborn:** Visualisasi statistik.
- **Scikit-learn:** Preprocessing, pemodelan, dan evaluasi model.
- **Joblib:** Penyimpanan dan pemuatan model.

## Tahapan Analisis

1. Data Collecting
2. Data Loading
3. Data Cleaning
4. Data Transformation
5. Exploratory Data Analysis (EDA)
6. Data Splitting
7. Model Building
8. Model Evaluation
9. Model Saving

## Algoritma

Algoritma yang digunakan adalah **Random Forest Regressor**, yaitu algoritma *supervised learning* yang menggabungkan beberapa *decision tree* untuk menghasilkan prediksi nilai numerik. Algoritma ini digunakan untuk memprediksi harga penginapan Airbnb berdasarkan karakteristik yang tersedia dalam dataset.

## Hasil Evaluasi Model

Hasil evaluasi Random Forest Regressor pada data uji adalah sebagai berikut:

| Metrik | Hasil |
|---|---:|
| MAE | 0.5055 |
| RMSE | 0.6828 |
| R² Score | 0.5296 |

Model memperoleh R² Score sebesar 0,5296 atau sekitar 52,96%. Hasil ini menunjukkan bahwa model mampu menjelaskan sebagian variasi target pada data uji, tetapi performanya masih dapat ditingkatkan.

## Feature Importance

Berdasarkan hasil model, lima fitur dengan nilai kepentingan tertinggi adalah:

1. `room_type`
2. `longitude`
3. `latitude`
4. `name`
5. `host_id`

Fitur `room_type` memiliki nilai *feature importance* tertinggi, yang menunjukkan bahwa fitur tersebut paling banyak dimanfaatkan model dalam menghasilkan prediksi pada eksperimen ini.

## Struktur Repository

- **`README.md`**: Dokumentasi proyek dan penjelasan tahapan praktikum.
- **`Memprediksi Airbnb NYC.ipynb`**: Berisi kode Python dan hasil analisis praktikum.
- **`AB_NYC_2019.csv`**: Dataset Airbnb yang digunakan dalam proyek.
- **`model_airbnb.joblib`**: File model yang telah dilatih dan disimpan untuk digunakan kembali.

## Tujuan Pembelajaran

- Memahami tahapan pengolahan data dalam Machine Learning.
- Mampu melakukan *data cleaning*, *data transformation*, dan EDA.
- Memahami proses pembagian dataset menjadi data latih dan data uji.
- Mampu membangun model prediksi harga Airbnb menggunakan Random Forest Regressor.
- Mampu mengevaluasi model menggunakan MAE, RMSE, dan R² Score.
- Memahami cara menyimpan dan memuat kembali model Machine Learning.

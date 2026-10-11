Airbnb Price Prediction





Deskripsi Proyek

Proyek ini merupakan tugas praktikum mata kuliah Machine Learning yang bertujuan untuk menganalisis dan memprediksi harga penginapan Airbnb di New York City menggunakan Python dan Jupyter Notebook. Dengan Praktikum ini, dilakukan pengolahan dan analisis data serta pembangunan model machine learning untuk mempelajari pola harga penginapan berdasarkan karakteristik yang terdapat dalam dataset.





Sumber Dataset 

Dataset yang digunakan adalah New York City Airbnb Open Data dari Kaggle.



* Platform: Kaggle



* Pembuat dataset: Dgomonov



* Periode data: 2019



* Nama file: AB\_NYC\_2019.csv



Tautan dataset: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data



Dataset berisi informasi mengenai listing Airbnb di New York City, seperti lokasi penginapan, jenis kamar, harga, jumlah ulasan, dan ketersediaan penginapan.



Tujuan Analisis

1. Melakukan pembersihan data dari nilai yang hilang dan mengidentifikasi data duplikat serta outlier.
2. Melakukan transformasi data numerik dan kategorikal.
3. Memahami karakteristik dataset melalui Exploratory Data Analysis (EDA).
4. Membagi dataset menjadi data latih dan data uji.
5. Membangun model prediksi menggunakan Random Forest Regressor.
6. Mengevaluasi performa model menggunakan MAE, RMSE, dan R² Score.
7. Menyimpan model yang telah dilatih agar dapat digunakan kembali.



Tools dan Library

* Jupyter Notebook
* Kaggle
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib



Tahapan Analisis

1. Data Collecting
2. Data Loading
3. Data Cleaning
4. Data Transformation
5. Exploratory Data Analysis (EDA)
6. Data Splitting
7. Pembangunan Model 
8. Evaluasi Model



Algoritma

Algoritma yang digunakan dalam proyek ini adalah Random Forest Regressor, yaitu algoritma supervised learning yang menggabungkan beberapa decision tree untuk menghasilkan prediksi nilai numerik. Model ini digunakan untuk memprediksi harga penginapan Airbnb berdasarkan karakteristik yang terdapat dalam dataset.



Hasil Evaluasi Model



Hasil evaluasi Random Forest Regressor pada data uji

* MAE = 0.5055
* RMSE = 0.6828
* R² = 0.5296



Model memperoleh R² nilai sekitar 0,53, yang menunjukkan bahwa model mampu menjelaskan sekitar 52,96% variasi target pada data uji dalam konfigurasi eksperimen ini.



Feature Importance

Berdasarkan hasil model, fitur dengan nilai kepentingan tertinggi adalah:

1. room\_type
2. longitude
3. latitude
4. name
5. host\_id



Fitur room\_type memiliki nilai feature importance tertinggi. Hasil ini menunjukkan bahwa jenis kamar menjadi fitur yang paling banyak dimanfaatkan oleh model dalam proses prediksi pada analisis ini.



Struktur Repository

* README.md: Dokumentasi proyek dan penjelasan tahapan praktikum.
* Memprediksi Airbnb NYC.ipynb : Berisi kode Python dan hasil analisis praktikum.
* AB\_NYC\_2019.csv : Berisi kode Python dan hasil analisis praktikum.
* model\_airbnb.joblib : File model yang telah dilatih dan disimpan untuk digunakan kembali.



Tujuan Pembelajaran

1. Memahami tahapan pengolahan data dalam Machine Learning.
2. Mampu melakukan data cleaning, data transformation, dan Exploratory Data Analysis (EDA).
3. Memahami proses pembagian dataset menjadi data latih dan data uji.
4. Mampu membangun model prediksi harga Airbnb menggunakan Random Forest Regressor.
5. Mampu mengevaluasi performa model menggunakan MAE, RMSE, dan R² Score.
6. Memahami cara menyimpan dan memuat kembali model Machine Learning.




import streamlit as st
import pandas as pd
import joblib
import logging

logging.basisConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Harga Airbnb NYC",
    page_icon="🏠",
    layout="wide"
)


# Memuat model Pipeline dan daftar fitur
@st.cache_resource
def load_model():
    model = joblib.load("deployment/model_airbnb_pipeline_v2.joblib")
    features = joblib.load("deployment/feature_airbnb_pipeline_v2.joblib")
    return model, features

model, features = load_model()

# Inisialisasi monitoring per sesi pengguna
if "prediction_attempts" not in st.session_state:
    st.session_state.prediction_attempts = 0

if "prediction_successes" not in st.session_state:
    st.session_state.prediction_successes = 0

if "prediction_errors" not in st.session_state:
    st.session_state.prediction_errors = 0


# Judul aplikasi
st.title("Prediksi Harga Airbnb NYC")
st.write(
    "Aplikasi Machine Learning untuk memprediksi harga "
    "penginapan Airbnb di New York City."
)

st.divider()

st.subheader("Masukkan Data Airbnb")

# Form input
with st.form("form_prediksi"):
    input_data = {}

    col1, col2 = st.columns(2)

    for i, feature in enumerate(features):
        with col1 if i % 2 == 0 else col2:
            if feature in ["id", "host_id"]:
                input_data[feature] = st.number_input(
                    feature.replace("_", " ").title(),
                    min_value=0,
                    value=0,
                    step=1
                )
            elif feature in [
                "latitude", "longitude", "minimum_nights",
                "number_of_reviews", "reviews_per_month",
                "calculated_host_listings_count",
                "availability_365"
            ]:
                input_data[feature] = st.number_input(
                    feature.replace("_", " ").title(),
                    value=0.0,
                    format="%.4f"
                )
            else:
                input_data[feature] = st.text_input(
                    feature.replace("_", " ").title()
                )

    submit = st.form_submit_button("Prediksi Harga")


if submit:
    st.session_state.prediction_attempts += 1

    logger.info(
        "Prediction attempt #%s",
        st.session_state.prediction_attempts
    )

    try:
        data = pd.DataFrame([input_data], columns=features)
        prediction = model.predict(data)
        predicted_price = float(prediction[0])

        st.session_state.prediction_successes += 1

        logger.info(
            "Prediction successful | attempts=%s | successes=%s",
            st.session_state.prediction_attempts,
            st.session_state.prediction_successes
        )

        st.success("Prediksi berhasil dilakukan!")
        st.metric(
            label="Hasil Prediksi Harga",
            value=f"${predicted_price:,.2f} USD"
        )

    except Exception:
        st.session_state.prediction_errors += 1

        logger.exception(
            "Prediction failed | attempts=%s | errors=%s",
            st.session_state.prediction_attempts,
            st.session_state.prediction_errors
        )

        st.error(
            "Prediksi gagal. Periksa format input atau hubungi pengelola."
        )



# Dashboard monitoring
st.divider()
st.subheader("Monitoring Aplikasi")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Percobaan",
        st.session_state.prediction_attempts
    )

with col2:
    st.metric(
        "Prediksi Berhasil",
        st.session_state.prediction_successes
    )

with col3:
    st.metric(
        "Prediksi Gagal",
        st.session_state.prediction_errors
    )

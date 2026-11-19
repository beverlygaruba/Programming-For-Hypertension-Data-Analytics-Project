import pandas as pd
import streamlit as st



def export_hypertension_dataset_from_csv(data_set_file_path):
    try:
        dataset = pd.read_csv(data_set_file_path)
    except FileNotFoundError:
        print('File not found')
    else:
        return dataset



def preprocess_missing_data(hypertension_data):
    if 'Creatinine_mg_dL' in hypertension_data.columns:
        creatinine_values = hypertension_data['Creatinine_mg_dL']
        creatinine_median = creatinine_values.median()
        hypertension_data['Creatinine_mg_dL'] = creatinine_values.fillna(creatinine_median)

    if 'Fasting_Glucose_mg_dL' in hypertension_data.columns:
        glucose_values = hypertension_data['Fasting_Glucose_mg_dL']
        glucose_median = glucose_values.median()
        hypertension_data['Fasting_Glucose_mg_dL'] = glucose_values.fillna(glucose_median)

    if 'Alcohol_Consumption' in hypertension_data.columns:
        alcohol_values = hypertension_data['Alcohol_Consumption']
        hypertension_data['Alcohol_Consumption'] = alcohol_values.fillna("None")

    if 'waist_circumference_cm' in hypertension_data.columns:
        waist_values = hypertension_data['waist_circumference_cm']
        waist_median = waist_values.median()
        hypertension_data['waist_circumference_cm'] = waist_values.fillna(waist_median)

    if 'sleep_hours' in hypertension_data.columns:
        sleep_values = hypertension_data['sleep_hours']
        sleep_median = sleep_values.median()
        hypertension_data['sleep_hours'] = sleep_values.fillna(sleep_median)

    if 'creatinine_mg_dl' in hypertension_data.columns:
        creatinine_values = hypertension_data['creatinine_mg_dl']
        creatinine_median = creatinine_values.median()
        hypertension_data['creatinine_mg_dl'] = creatinine_values.fillna(creatinine_median)

    if 'fasting_glucose_mg_dl' in hypertension_data.columns:
        glucose_values = hypertension_data['fasting_glucose_mg_dl']
        glucose_median = glucose_values.median()
        hypertension_data['fasting_glucose_mg_dl'] = glucose_values.fillna(glucose_median)

    if 'cholesterol_mg_dl' in hypertension_data.columns:
        cholesterol_values = hypertension_data['cholesterol_mg_dl']
        cholesterol_median = cholesterol_values.median()
        hypertension_data['cholesterol_mg_dl'] = cholesterol_values.fillna(cholesterol_median)

    return hypertension_data

def drop_exact_duplicates_from_hypertension_data(hypertension_data):
    hypertension_data = hypertension_data.drop_duplicates()
    return hypertension_data


def engineer_new_feature_from_existing_data(hypertension_data):
    if 'Systolic_BP_mmHg' in hypertension_data.columns and 'Diastolic_BP_mmHg' in hypertension_data.columns:

        systolic_bp = hypertension_data['Systolic_BP_mmHg']
        diastolic_bp = hypertension_data['Diastolic_BP_mmHg']
        pulse_pressure = systolic_bp - diastolic_bp
        hypertension_data['Pulse_Pressure'] = pulse_pressure

        mean_arterial_pressure = diastolic_bp + (1 / 3) * pulse_pressure
        hypertension_data['Mean_Arterial_Pressure'] = mean_arterial_pressure

    return hypertension_data


def preprocess_hypertension_data(hypertension_data):
    hypertension_data = preprocess_missing_data(hypertension_data)
    hypertension_data = drop_exact_duplicates_from_hypertension_data(hypertension_data)
    hypertension_data = engineer_new_feature_from_existing_data(hypertension_data)

    return hypertension_data


def show_hypertension_data_overview_page():
    st.header("Understanding hypertension through the data")



def show_hypertension_and_age_correlation_page():
    st.header("How Age Relates to Hypertension")


def build_and_display_hypertension_data_page(hypertension_data):
    st.title("Understanding Hypertension")
    st.caption("An educational tool")

    sections = st.navigation([
        st.Page(show_hypertension_data_overview_page, title="Data overview"),
        st.Page(show_hypertension_and_age_correlation_page, title="How Age Relates to Hypertension"),
    ])
    sections.run()



if __name__ == '__main__':
    print("My hypertension dataset analysis and visualization ")
    file_path = "hypertension_dataset_5000.csv"
    raw_hypertension_data = export_hypertension_dataset_from_csv(file_path)
    preprocessed_hypertension_data = preprocess_hypertension_data(raw_hypertension_data.copy())
    print(raw_hypertension_data.info)
    print(preprocessed_hypertension_data.info)
    build_and_display_hypertension_data_page(preprocessed_hypertension_data)


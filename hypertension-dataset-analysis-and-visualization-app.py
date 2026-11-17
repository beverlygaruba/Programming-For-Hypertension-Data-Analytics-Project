import pandas as pd


def export_hypertension_dataset_from_csv(data_set_file_path):
    try:
        dataset = pd.read_csv(data_set_file_path)
    except FileNotFoundError:
        print('File not found')
    else:
        return dataset



def preprocess_hypertension_data(hypertension_data):
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


if __name__ == '__main__':
    print("My hypertension dataset analysis and visualization ")
    file_path = "hypertension_dataset_5000.csv"
    raw_hypertension_data = export_hypertension_dataset_from_csv(file_path)
    preprocessed_hypertension_data = preprocess_hypertension_data(raw_hypertension_data.copy())
    print(raw_hypertension_data.info)
    print(preprocessed_hypertension_data.info)


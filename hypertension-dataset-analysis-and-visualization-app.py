import pandas as pd
import streamlit as st
import plotly.express as px


BP_COLORS = { "Normal": "#2E9E6B","Elevated": "#F2C14E","Stage 1 Hypertension": "#F28C38","Stage 2 Hypertension": "#D64545",}
AGE_LABELS = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
BMI_LABELS = ["Underweight", "Normal", "Overweight", "Obese"]
HTN_COLORS = {"Yes": "#E45756", "No": "#2E86AB"}
FEATURE_CATEGORY_ORDER = {"Age_Group": AGE_LABELS,  "BMI_Class": BMI_LABELS,"Gender": ["Female", "Male"],"Salt_Intake": ["Low", "Normal", "High", "Very High", "Unknown"],
    "Physical_Activity": ["Sedentary", "Light", "Moderate", "Active"],"Alcohol_Consumption": ["Unknown", "Occasional", "Moderate", "Heavy"],
    "Smoking_Status": ["Never", "Former", "Current"],"Stress_Level": ["Low", "Moderate", "High", "Very High", "Unknown"],
    "Family_History_HTN": ["No", "Yes"], "BP_Category": list(BP_COLORS),}
LABELS = {
    "Waist_Circumference_cm": "Waist circumference (cm)", "Sleep_Hours": "Sleep (hours)", "Creatinine_mg_dL": "Creatinine (mg/dL)","Fasting_Glucose_mg_dL": "Fasting glucose (mg/dL)",
    "Cholesterol_mg_dL": "Cholesterol (mg/dL)", "Systolic_BP_mmHg": "Systolic BP (mmHg)", "Diastolic_BP_mmHg": "Diastolic BP (mmHg)", "Family_History_HTN": "Family history of hypertension",
}

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
        hypertension_data['Alcohol_Consumption'] = alcohol_values.fillna("Unknown")

    if 'Salt_Intake' in hypertension_data.columns:
        alcohol_values = hypertension_data['Salt_Intake']
        hypertension_data['Salt_Intake'] = alcohol_values.fillna("Unknown")

    if 'Stress_Level' in hypertension_data.columns:
        alcohol_values = hypertension_data['Stress_Level']
        hypertension_data['Stress_Level'] = alcohol_values.fillna("Unknown")

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

    hypertension_data["Age_Group"] = pd.cut(hypertension_data["Age"], bins=[0, 30, 40, 50, 60, 70, 80, 200],
                                                right=False, labels=AGE_LABELS).astype(str)
    hypertension_data["BMI_Class"] = pd.cut(hypertension_data["BMI"], bins=[0, 18.5, 25, 30, 200], right=False,
                                                labels=BMI_LABELS).astype(str)
    hypertension_data["Has_Hypertension"] = (hypertension_data["Hypertension"] == "Yes").astype(int)

    return hypertension_data


def preprocess_hypertension_data(hypertension_data):
    hypertension_data = preprocess_missing_data(hypertension_data)
    hypertension_data = drop_exact_duplicates_from_hypertension_data(hypertension_data)
    hypertension_data = engineer_new_feature_from_existing_data(hypertension_data)

    return hypertension_data

def load_and_preprocess_hypertension_data():
    file_path = "hypertension_dataset_5000.csv"
    raw_hypertension_data = export_hypertension_dataset_from_csv(file_path)
    preprocessed_hypertension_data = preprocess_hypertension_data(raw_hypertension_data.copy())

    return raw_hypertension_data, preprocessed_hypertension_data


def show_chart_row(chart1, chart2):
    col1, col2 = st.columns(2)
    with col1:
        chart1()
    with col2:
        chart2()

def resolve_column_name(name):
    return LABELS.get(name, name.replace("_", " "))


def show_hypertension_data_overview_page():
    raw_hypertension_data, preprocessed_hypertension_data = load_and_preprocess_hypertension_data()

    st.write("Hypertension is often called the silent killer because it can develop over time without noticeable symptoms. "
             "It occurs when the force of blood pushing against the walls of your arteries remains consistently too high, "
             "putting extra strain on your heart and blood vessels. It usually causes no symptoms, yet over time it raises "
            "the risk of stroke, heart attack, heart failure and kidney disease.\n\n"
            "Blood Pressure (BP) =  **Systolic Pressure / Diastolic Pressure** ")
    st.caption("")

    st.dataframe(pd.DataFrame({
        "Category": ["Normal", "Elevated", "Stage 1 hypertension", "Stage 2 hypertension"],
        "Systolic (mmHg)": ["below 120", "120 - 129", "130 - 139", "140 or higher"],
        "Diastolic (mmHg)": ["and below 80", "and below 80", "or 80 - 89", "or 90 or higher"],
    }), hide_index=True)
    st.caption("")

    st.subheader("Understanding hypertension through  data")
    st.write("Total number of patients = ",  f"{len(preprocessed_hypertension_data):,}")



    show_bar_chart(preprocessed_hypertension_data, "Salt_Intake", horizontal=True)
    show_hypertension_split(preprocessed_hypertension_data, "Salt_Intake")

    show_bar_chart(preprocessed_hypertension_data, "Physical_Activity")
    show_hypertension_split(preprocessed_hypertension_data, "Physical_Activity")


    show_bar_chart(preprocessed_hypertension_data, "Alcohol_Consumption", horizontal=True)
    show_hypertension_split(preprocessed_hypertension_data, "Alcohol_Consumption")


    show_bar_chart(preprocessed_hypertension_data, "Stress_Level")
    show_hypertension_split(preprocessed_hypertension_data, "Stress_Level")
    show_pie_chart(preprocessed_hypertension_data, "Family_History_HTN")

    show_chart_row(
        lambda: show_bar_chart(preprocessed_hypertension_data, "Age_Group"),
        lambda: show_pie_chart(preprocessed_hypertension_data, "Gender")
    )

    st.subheader("Blood pressure")
    show_chart_row(
        lambda: chart_share_with_hypertension(preprocessed_hypertension_data),
        lambda: chart_patients_by_bp_category(preprocessed_hypertension_data)
    )

def show_hypertension_split(df, column):
    table = pd.crosstab(df[column], df["Hypertension"], normalize="index") * 100
    table = table.reindex(FEATURE_CATEGORY_ORDER[column])

    fig = px.bar(table, x=table.index, y=["Yes", "No"], text_auto=".1f",
                 color_discrete_map=HTN_COLORS,
                 title=f"Hypertension by {resolve_column_name(column)}",
                 labels={"x": resolve_column_name(column), "value": "Percentage of patients",
                         "variable": "Hypertension"})
    fig.update_layout(height=400, yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

def show_bar_chart(hypertension_data, column, horizontal=False):
    counts = hypertension_data[column].value_counts().reindex(
        FEATURE_CATEGORY_ORDER[column], fill_value=0
    )

    chart = px.bar(
        x=counts.values if horizontal else counts.index,
        y=counts.index if horizontal else counts.values,
        orientation="h" if horizontal else "v",
        text_auto=True,
        title=f"Patients by {resolve_column_name(column)}",
        labels={
            "x": "Patients" if horizontal else resolve_column_name(column),
            "y": resolve_column_name(column) if horizontal else "Patients"
        }
    )

    chart.update_layout(height=400)
    st.plotly_chart(chart, use_container_width=True)


def show_pie_chart(hypertension_data, column):
    counts = hypertension_data[column].value_counts().reindex(
        FEATURE_CATEGORY_ORDER[column], fill_value=0
    )
    chart = px.pie(
        values=counts.values,
        names=counts.index,
        title=f"Patients by {resolve_column_name(column)}",
        hole=0.4
    )
    chart.update_layout(height=380)
    st.plotly_chart(chart, use_container_width=True)



def chart_share_with_hypertension(df):
    share = df["Hypertension"].map({"No": "No hypertension", "Yes": "Hypertension"})
    share = share.value_counts().reset_index()
    share.columns = ["Status", "Patients"]
    fig = px.pie(share, names="Status", values="Patients", hole=0.5, color="Status",
                 color_discrete_map={"Hypertension": HTN_COLORS["Yes"],
                                     "No hypertension": HTN_COLORS["No"]},
                 title="Patients with hypertension")
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)


def chart_patients_by_bp_category(df):
    counts = df["BP_Category"].value_counts().reindex(FEATURE_CATEGORY_ORDER["BP_Category"], fill_value=0)
    counts = counts.reset_index()
    counts.columns = ["BP_Category", "Patients"]
    fig = px.bar(counts, x="BP_Category", y="Patients", color="BP_Category", text_auto=True,
                 color_discrete_map=BP_COLORS, title="Patients by blood pressure category",
                 labels={"BP_Category": ""})
    fig.update_layout(showlegend=False)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)



def show_hypertension_and_age_correlation_page():
    st.header("How Age Relates to Hypertension")


def build_and_display_hypertension_data_page():
    st.title("Understanding Hypertension")
    st.caption("")

    sections = st.navigation([
        st.Page(show_hypertension_data_overview_page, title="Data overview"),
        st.Page(show_hypertension_and_age_correlation_page, title="How Age Relates to Hypertension"),
    ])
    sections.run()



if __name__ == '__main__':
    build_and_display_hypertension_data_page()


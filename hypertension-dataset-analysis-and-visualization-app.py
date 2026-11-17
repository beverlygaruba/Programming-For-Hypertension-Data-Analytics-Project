import pandas as pd


def export_hypertension_dataset_from_csv(data_set_file_path):
    try:
        dataset = pd.read_csv(data_set_file_path)
    except FileNotFoundError:
        print('File not found')
    else:
        return dataset

if __name__ == '__main__':
    print("My hypertension dataset analysis and visualization ")
    file_path = "hypertension_dataset_5000.csv"
    hypertension_data = export_hypertension_dataset_from_csv(file_path)
    print(hypertension_data.info)


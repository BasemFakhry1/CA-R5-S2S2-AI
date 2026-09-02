import pandas as pd


def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except Exception as e:
        print(f"Error: Cannot read the file. {e}")
        return None


def Drop_unnecessary_features(df, cols_to_drop):
    df = df.drop(cols_to_drop, axis=1)
    return df


def Check_data_type(df):
    dtypes = df.dtypes
    n_unique = df.nunique()

    report = pd.DataFrame({
        "Dtype": dtypes,
        "Num_Unique": n_unique
    }).T

    return report
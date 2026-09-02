from preprocessing import Read_data_file
from preprocessing import Drop_unnecessary_features
from preprocessing import Check_data_type

from Config.config import cols_to_drop


file_path = "src/python/Session-10/assignments/Preprocessing/Titanic_Project/train.csv"

df = Read_data_file(file_path)

if df is not None:

    print("Original Data:")
    print(df.head())

    df = Drop_unnecessary_features(df, cols_to_drop)

    print("\nData after dropping unnecessary features:")
    print(df.head())

    print("\nData Type Report:")
    print(Check_data_type(df))
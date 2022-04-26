import pandas as pd
import numpy as np

# Function Area
def check_NaN(dataframe):
    for col in dataframe.columns:
        sum_NaN = sum(dataframe[col].isna())
        print(f'{col}에는 NaN 값이 총 {sum_NaN}개 있습니다')

# Main Area
raw_data = {'1열': [1, 2, np.NaN, 4],
            '2열': [10, np.NaN, np.NaN, 40],
            '3열': [9, 3, 300, 400]}
dataframe = pd.DataFrame(raw_data)

check_NaN(dataframe)

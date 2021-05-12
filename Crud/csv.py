import pandas as pd


def read_excel():
    loc = "user_list.xlsx"

    data_frame = pd.read_excel(loc)
    return data_frame.values

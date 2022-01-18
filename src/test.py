import numpy as np
import pandas as pd

df = pd.read_excel("test.xlsx")


def get_white_line():
    temp = df[df['لنگش جدید'] == "*"]
    temp = temp[~temp['2'].isna() | ~temp['3'].isna()]

    def white_line_count(temp_df):
        two = temp_df["2"].values
        three = temp_df["3"].values
        values = np.unique(np.concatenate([two, three]))
        values = values[~np.isnan(values)]
        return values.shape[0]

    white_line = temp.groupby(["شماره دام", "روز"]).apply(white_line_count)

    print(white_line.sum())


def get_kaf_som():
    temp = df[df['لنگش جدید'] == "*"]
    temp = temp[~temp['4'].isna()]

    def kaf_som_count(temp_df):
        four = np.unique(temp_df["4"].values)
        return four.shape[0]

    kaf_som = temp.groupby(["شماره دام", "روز"]).apply(kaf_som_count)
    print(kaf_som.sum())


if __name__ == '__main__':
    get_kaf_som()
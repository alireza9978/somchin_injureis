import numpy as np
import pandas as pd

df = pd.read_excel("test.xlsx")


def get_felemon():
    temp = df[df['لنگش جدید'] == "*"]
    temp = temp[~temp['0'].isna()]
    felemon = temp[["شماره دام", "روز", "0"]].groupby(["شماره دام", "روز"]).nunique()
    return felemon.sum()[0]


def get_dramatit():
    temp = df[df['لنگش جدید'] == "*"]
    temp = temp[~temp['10'].isna()]
    dramatit = temp[["شماره دام", "روز", "10"]].groupby(["شماره دام", "روز"]).nunique()
    return dramatit.sum()[0]


def get_kaf_som():
    temp = df[df['لنگش جدید'] == "*"]
    temp = temp[~temp['4'].isna()]
    kaf_som = temp[["شماره دام", "روز", "4"]].groupby(["شماره دام", "روز"]).nunique()
    return kaf_som.sum()[2]


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

    # print(white_line.sum())
    return white_line.sum()


def get_panje():
    pass


def get_pashne():
    pass


def get_tarak():
    pass


def get_nine():
    pass


def get_visit():
    pass


def get_new_limp():
    pass


def get_sad():
    pass


def get_dry():
    pass


def get_delay():
    pass


def get_group():
    pass


def get_long():
    pass


def get_som_chini():
    pass


def get_high_score():
    pass


def get_talise():
    pass


def get_erjaii():
    pass


def get_takhte():
    pass


if __name__ == '__main__':
    if get_felemon() != 8:
        print("wrong felemon")
    if get_dramatit() != 28:
        print("wrong dramatit")
    if get_kaf_som() != 101:
        print("wrong kaf som")
    if get_white_line() != 12:
        print("wrong white line")
    if get_panje() != 17:
        print("wrong panje")
    if get_pashne() != 37:
        print("wrong pashne")
    if get_tarak() != 1:
        print("wrong tarak")
    if get_nine() != 9:
        print("wrong nine")
    if get_visit() != 80:
        print("wrong visit")
    if get_new_limp() != 141:
        print("wrong langesh jadid")
    if get_sad() != 74:
        print("wrong sad roze")
    if get_dry() != 130:
        print("wrong dry")
    if get_delay() != 60:
        print("wrong delay")
    if get_group() != 0:
        print("wrong group")
    if get_long() != 3:
        print("wrong long")
    if get_som_chini() != 983:
        print("wrong som chini")
    if get_high_score() != 626:
        print("wrong high score")
    if get_talise() != 1:
        print("wrong talise")
    if get_erjaii() != 51:
        print("wrong erjaii")
    if get_takhte() != 159:
        print("wrong takhte")

import numpy as np
import pandas as pd

df = pd.read_excel("test.xlsx")
areas = [f"{i}" for i in range(13)]
new_limp_column = 'لنگش جدید'
cow_number_column = "شماره دام"
day_column = "روز"
month_column = "ماه"
year_column = "سال"


def get_felemon():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['0'].isna()]
    felemon = temp[[cow_number_column, day_column, month_column, year_column, "0"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return felemon.sum()[0]


def get_dramatit():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['10'].isna()]
    dramatit = temp[[cow_number_column, day_column, month_column, year_column, "10"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return dramatit.sum()[0]


def get_kaf_som():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['4'].isna()]
    kaf_som = temp[[cow_number_column, day_column, month_column, year_column, "4"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return kaf_som.sum()[0]


def get_white_line():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['2'].isna() | ~temp['3'].isna() | ~temp['4'].isna()]

    def white_line_count(temp_df):
        two = temp_df["2"].values
        three = temp_df["3"].values
        values = np.unique(np.concatenate([two, three]))
        values = values[~np.isnan(values)]
        if values.shape[0] != 0:
            four = temp_df["4"].values
            four = four[~np.isnan(four)]
            if four.shape[0] != 0:
                return values.shape[0] - np.intersect1d(four, values).shape[0]
            else:
                return values.shape[0]
        else:
            return 0

    white_line = temp[[cow_number_column, day_column, month_column, year_column, "2", "3", "4"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(white_line_count)

    return white_line.sum()


def get_panje():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['1'].isna() | ~temp['5'].isna() | ~temp['4'].isna()]

    def white_line_count(temp_df):
        one = temp_df["1"].values
        five = temp_df["5"].values
        values = np.unique(np.concatenate([one, five]))
        values = values[~np.isnan(values)]
        if values.shape[0] != 0:
            four = temp_df["4"].values
            four = four[~np.isnan(four)]
            if four.shape[0] != 0:
                return values.shape[0] - np.intersect1d(four, values).shape[0]
            else:
                return values.shape[0]
        else:
            return 0

    panje = temp[[cow_number_column, day_column, month_column, year_column, "1", "5", "4"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(white_line_count)
    result = panje.sum()

    return result


def get_pashne():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['6'].isna()]
    pashne = temp[[cow_number_column, day_column, month_column, year_column, "6"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return pashne.sum()[0]


def get_tarak():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['7'].isna() | ~temp['8'].isna() | ~temp['11'].isna() | ~temp['12'].isna()]

    def inner_tarak(temp_df):
        seven = temp_df["7"].values
        eight = temp_df["8"].values
        eleven = temp_df["11"].values
        twelve = temp_df["12"].values
        values = np.unique(np.concatenate([seven, eight, eleven, twelve]))
        values = values[~np.isnan(values)]
        return values.shape[0]

    tarak = temp[[cow_number_column, day_column, month_column, year_column, "7", "8", "11", "12"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(inner_tarak)
    return tarak.sum()


def get_nine():
    temp = df[df[new_limp_column] == "*"]
    temp = temp[~temp['9'].isna()]
    kaf_som = temp[[cow_number_column, day_column, month_column, year_column, "9"]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return kaf_som.sum()[0]


def get_visit():
    temp = df[df['بازدید لنگش'] == "*"]
    visit_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return visit_count.sum()[0]


def get_new_limp():
    temp = df[df[new_limp_column] == "*"]
    limp_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return limp_count.sum()[0]


def get_sad():
    temp = df[df["100 روزه"] == "*"]
    sad_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return sad_count.sum()[0]


def get_dry():
    temp = df[df["خشکی"] == "*"]
    dry_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return dry_count.sum()[0]


def get_delay():
    temp = df[df["عقب مانده تولید مثلی"] == "*"]
    delay_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return delay_count.sum()[0]


def get_group():
    temp = df[df['سم چینی گروهی'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_long():
    temp = df[df['سم بلند'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_som_chini():
    temp = df[df['سم چینی'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_high_score():
    temp = df[df['اسکور بالا'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_talise():
    temp = df[df['تلیسه'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_erjaii():
    temp = df[df['ارجاعی'] == "*"]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_takhte():
    temp = df[df['تخته گذاری'] == "*"]

    def inner_takhte(temp_df):
        fingers = np.unique(temp_df[areas].values)
        fingers = fingers[~np.isnan(fingers)]
        return fingers.shape[0]

    group_count = temp[[cow_number_column, day_column, month_column, year_column] + areas].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(
        inner_takhte)
    return group_count.sum()


def get_recorde_avg():
    record_count = df[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return record_count.mean()[0]


names = """فلگمون بین انگشتی
درماتیت انگشتی
زخم کف سم
زخم خط سفید
زخم پنجه
زخم پاشنه
ترک دیواره
ناحیه 9
میانگین عملیات در روز
بازدید
لنگش جدید
صد‌روزه
خشکی
عقب‌مانده تولید مثلی
سم‌چینی گروهی
سم بلند
سم‌چینی
اسکوربالا
تلیسه
ارجاعی
تخته گذاری
"""
values = [get_felemon(),
          get_dramatit(),
          get_kaf_som(),
          get_white_line(),
          get_panje(),
          get_pashne(),
          get_tarak(),
          get_nine(),
          round(get_recorde_avg(), 4),
          get_visit(),
          get_new_limp(),
          get_sad(),
          get_dry(),
          get_delay(),
          get_group(),
          get_long(),
          get_som_chini(),
          get_high_score(),
          get_talise(),
          get_erjaii(),
          get_takhte()]

final_df = pd.DataFrame(columns=["name", "count"])
names = names.split("\n")
for key, value in zip(names, values):
    final_df = final_df.append(pd.Series([key, value], index=["name", "count"]), ignore_index=True)

final_df.to_excel("report_user_date.xlsx", index=False)

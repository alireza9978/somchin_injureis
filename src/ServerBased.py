import numpy as np
import pandas as pd

df = pd.read_excel("lesion_injury_report.xlsx")
areas = [f"{i}" for i in range(13)]
new_limp_column = 'reference_cause_new_limp'
leg_area_number = "leg_area_number"
finger_number = "finger_number"
cow_number_column = "cow_id"
day_column = "day"
month_column = "month"
year_column = "year"


def get_felemon():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number] == 0]
    felemon = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return felemon.sum()[0]


def get_dramatit():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number] == 10]
    dramatit = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return dramatit.sum()[0]


def get_kaf_som():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number] == 4]
    kaf_som = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return kaf_som.sum()[0]


def get_white_line():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number].isin([2, 3, 4])]

    def white_line_count(temp_df):
        two = temp_df.loc[temp_df[leg_area_number] == 2, finger_number].values
        three = temp_df.loc[temp_df[leg_area_number] == 3, finger_number].values
        values = np.unique(np.concatenate([two, three]))
        values = values[~np.isnan(values)]
        if values.shape[0] != 0:
            four = temp_df.loc[temp_df[leg_area_number] == 4, finger_number].values
            four = four[~np.isnan(four)]
            if four.shape[0] != 0:
                return values.shape[0] - np.intersect1d(four, values).shape[0]
            else:
                return values.shape[0]
        else:
            return 0

    white_line = temp[
        [cow_number_column, day_column, month_column, year_column, leg_area_number, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(white_line_count)

    return white_line.sum()


def get_panje():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number].isin([1, 5, 4])]

    def white_line_count(temp_df):
        one = temp_df.loc[temp_df[leg_area_number] == 1, finger_number].values
        five = temp_df.loc[temp_df[leg_area_number] == 5, finger_number].values
        values = np.unique(np.concatenate([one, five]))
        values = values[~np.isnan(values)]
        if values.shape[0] != 0:
            four = temp_df.loc[temp_df[leg_area_number] == 4, finger_number].values
            four = four[~np.isnan(four)]
            if four.shape[0] != 0:
                return values.shape[0] - np.intersect1d(four, values).shape[0]
            else:
                return values.shape[0]
        else:
            return 0

    panje = temp[[cow_number_column, day_column, month_column, year_column, leg_area_number, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(white_line_count)
    result = panje.sum()

    return result


def get_pashne():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number] == 6]

    pashne = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return pashne.sum()[0]


def get_tarak():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number].isin([7, 8, 11, 12])]

    def inner_tarak(temp_df):
        seven = temp_df.loc[temp_df[leg_area_number] == 7, finger_number].values
        eight = temp_df.loc[temp_df[leg_area_number] == 5, finger_number].values
        eleven = temp_df.loc[temp_df[leg_area_number] == 11, finger_number].values
        twelve = temp_df.loc[temp_df[leg_area_number] == 12, finger_number].values
        values = np.unique(np.concatenate([seven, eight, eleven, twelve]))
        values = values[~np.isnan(values)]
        return values.shape[0]

    tarak = temp[[cow_number_column, day_column, month_column, year_column, leg_area_number, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(inner_tarak)
    return tarak.sum()


def get_nine():
    temp = df[df[new_limp_column]]
    temp = temp[temp[leg_area_number] == 9]

    kaf_som = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).nunique()
    return kaf_som.sum()[0]


def get_visit():
    temp = df[df['reference_cause_limp_visit'] == 1]
    visit_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return visit_count.sum()[0]


def get_new_limp():
    temp = df[df[new_limp_column]]
    limp_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return limp_count.sum()[0]


def get_sad():
    temp = df[df["reference_cause_hundred_days"] == 1]
    sad_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return sad_count.sum()[0]


def get_dry():
    temp = df[df["reference_cause_dryness"] == 1]
    dry_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return dry_count.sum()[0]


def get_delay():
    temp = df[df["reference_cause_lagged"] == 1]
    delay_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return delay_count.sum()[0]


def get_group():
    temp = df[df['reference_cause_group_hoof_trim'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_long():
    temp = df[df['reference_cause_long_hoof'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_som_chini():
    temp = df[df['other_info_hoof_trim'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_high_score():
    temp = df[df['reference_cause_high_score'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_talise():
    temp = df[df['reference_cause_heifer'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_erjaii():
    temp = df[df['reference_cause_referential'] == 1]
    group_count = temp[[cow_number_column, day_column, month_column, year_column]].groupby(
        [day_column, month_column, year_column]).nunique()
    return group_count.sum()[0]


def get_takhte():
    temp = df[df['other_info_boarding'] == 1]

    def inner_takhte(temp_df):
        fingers = np.unique(temp_df[finger_number].values)
        fingers = fingers[~np.isnan(fingers)]
        return fingers.shape[0]

    group_count = temp[[cow_number_column, day_column, month_column, year_column, finger_number]].groupby(
        [cow_number_column, day_column, month_column, year_column]).apply(inner_takhte)
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
export_values = [get_felemon(),
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
for key, value in zip(names, export_values):
    final_df = final_df.append(pd.Series([key, value], index=["name", "count"]), ignore_index=True)

final_df.to_excel("report_user_date.xlsx", index=False)

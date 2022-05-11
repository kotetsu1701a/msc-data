import math

# ユリウス日から年月日を求める
# 天文計算入門　63頁 (16.6)より
def getdaytime(julian):
    # 各月の日数
    # 月に対応するために配列の先頭には０を代入
    T = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    a = int(julian + 68569.5)
    b = int(a / 36524.25)
    c = a - int(36524.25 * b + 0.75)
    e = int((c + 1) / 365.25025)
    f = c - int(365.25 * e) + 31
    g = int(f / 30.59)
    day = f - int(30.59 * g) + (julian + 0.5) - int(julian + 0.5)  # 日
    h = int(g / 11)
    month = g - 12 * h + 2  # 月
    year = 100 * (b - 49) + e + h  # 年

    # うるう年の判定
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        T[2] = 29

    # ユリウス日から年月日を求めるのでdの値がその月の日数を
    # 大きく超えることはなく、せいぜい＋1日程度だと思われる
    # 12月32日になったときの処理
    if month == 12:
        if day > T[month]:
            year += 1
            month = (month + 1) - 12
            day = 1
    else:
        # 12月以外の月における処理
        if day > T[month]:
            month += 1
            day = 1

    T[2] = 28

    return year, month, day


# ユリウス日を求める
def getjulian(year, month, day, hour, minute, second):
    if month < 3:
        month += 12.0
        year -= 1.0

    julian = int(year * 365.25) + int(year / 400.0) - int(year / 100.0) + int(30.59 * (month - 2)) + day + 1721088.5

    julian += hour / 24.0 + minute / 1440.0 + second / 86400.0
    julian -= 0.375

    return julian


# メイン
year = 2022
month = 5
day = 4
hour = 15
minute = 24
second = 37

julian = getjulian(year, month, day, hour, minute, second)

year, month, day = getdaytime(julian)

f = day - math.floor(day)

# 小数点以下７桁に丸める
f = math.floor(f * math.pow(10, 7)) / math.pow(10, 7)
print(f)

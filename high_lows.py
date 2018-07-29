import csv

from datetime import datetime
from matplotlib import pyplot as plt

#从文件中获取日期、最高气温和最低气温
# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs,lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(row[1])
            lows.append(low)

#根据数据绘制图形
flg = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)

#设置图形的格式
# plt.title("Daliy high temperatures, July 2014", fontsize=24)
plt.title("Daliy high and low temperatures, - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
flg.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
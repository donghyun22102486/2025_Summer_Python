import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fs
import platform

if platform.system() == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif platform.system() == "Darwin":
    plt.rc("font", famity="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False


tips = sns.load_dataset("tips")
# print(tips.head())

sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("요일별 평균 식사 금액")

sns.boxplot(data=tips, x="day", y="total_bill", palette="Set2")
plt.title("요일별 식사 금액 분포")
plt.xlabel("요일", fontsize=12)
plt.ylabel("식사 총 금액", fontsize=12)
plt.grid(True, axis="y", linestyle="--")

sns.set_style("darkgrid")
sns.set_palette("pastel")
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("식사 금액 vs 팁 금액 회귀선")
plt.show()


iris = sns.load_dataset("iris")
print(iris.head())


flights = sns.load_dataset("flights")
# print(data.head())
monthly = flights.pivot(index="month", columns="year", values="passengers")


sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.title("월별 항공 탑승객 수")
plt.show()

pivot_data = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(pivot_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title("연도-월별 항광 탑승객 수")
plt.show()

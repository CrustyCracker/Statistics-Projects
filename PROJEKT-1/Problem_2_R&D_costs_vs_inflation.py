import numpy
import pandas as pd
import os
from matplotlib import pyplot as plt

TASK_2_PATH = os.path.join(os.getcwd(), "data", "task2", "cleaned")
IMG_PATH = os.path.join(os.getcwd(), "img", "task_2")

PER_CAPITA_PATH = os.path.join(TASK_2_PATH, "R&D_per_capita.csv")
PKB_PATH = os.path.join(TASK_2_PATH, "R&D_PKB.csv")
SECTORS_PATH = os.path.join(TASK_2_PATH, "R&D_sectors.csv")
INFLATION_PATH = os.path.join(TASK_2_PATH, "inflacja_lata.csv")

INFLATION_VALUES = pd.read_csv(INFLATION_PATH)["wartosc"].tolist()
INFLATION_VALUES = [float(elem) - 100 for elem in INFLATION_VALUES]


def save_path(name):
    return os.path.join(IMG_PATH, name)


# R&B per capita vs inflation

per_capita = pd.read_csv(PER_CAPITA_PATH, delimiter=';')
years = per_capita["year"].tolist()
values = per_capita["value"].tolist()
plt.plot(years, values)
plt.title("Nakłady na R&B w latach 1999-2022")
plt.xlabel("Rok")
plt.ylabel("w [zł] na mieszkańca")
plt.savefig(save_path("nakłady_per_capita"))
plt.show()

values_inc = [1] + [new/last for new, last in zip(values[1:], values)]
values_inc = [elem * 100 - 100 for elem in values_inc]
temp = values_inc
plt.plot(years, values_inc, label="R&D")
plt.plot(years, INFLATION_VALUES, label="inflacja")
plt.title("Wzrost nakładów na R&D oraz inflacja w latach 1999-2022")
plt.xlabel("Rok")
plt.ylabel("w [%]")
plt.legend()
plt.savefig(save_path("per_capita_vs_inflacja"))
plt.show()

# R&D in relation to PKB vs inflation

pkb = pd.read_csv(PKB_PATH, delimiter=';')
years = pkb["year"].tolist()
values = pkb["value"].tolist()
negate_increase = [values[0]/elem for elem in values]
print(negate_increase)
plt.plot(years, values)
plt.title("Nakłady na rozwój i działalnośc badawczą w latach 1999-2022")
plt.xlabel("Rok")
plt.ylabel("w [%] w relacji do PKB")
plt.savefig(save_path("nakłady_PKB"))
plt.show()

values_inc = [1] + [new/last for new, last in zip(values[1:], values)]
values_inc = [elem * 100 - 100 for elem in values_inc]
plt.plot(years, values_inc)
plt.title("Wzrost nakładów na R&D w latach 1999-2022")
plt.xlabel("Rok")
plt.ylabel("w [%]")
plt.savefig(save_path("PKB_vs_inflacja"))
plt.show()

print(numpy.corrcoef(values_inc, temp))

# negate increase
inflation_comp = []
comp = 1
for inflation in INFLATION_VALUES:
    inflation_comp.append(comp)
    comp *= (1 + inflation/100)
values = per_capita["value"].tolist()
negated = [value * neg for neg, value in zip(negate_increase, values)]
predicted = [values[0] * comp for comp in inflation_comp]
plt.plot(years, negated, label="Faktyczny")
plt.plot(years, predicted, label="Przewidywany")
plt.legend()
plt.savefig(save_path("faktyczne_porownanie"))
plt.show()


# per sectors
sectors = ["Sektor przedsiębiorstw (BES)", "Sektor rządowy (GOV)", "Sektor szkolnictwa wyższego (HES)", "Sektor prywatnych instytucji niekomercyjnych (PNP)"]
pkb = pd.read_csv(SECTORS_PATH, delimiter=';')
years = ["2020", "2021", "2022"]
for sector in sectors:
    values = pkb.where(pkb["sector"] == sector).dropna()["value"].tolist()
    plt.plot(years, values, label=sector)
plt.title("Wydatki na R&D w różnych sektorach")
plt.xlabel("Rok")
plt.ylabel("W [zł]")
plt.legend()
plt.savefig(save_path("sectors"))
plt.show()


for sector in sectors:
    values = pkb.where(pkb["sector"] == sector).dropna()["value"].tolist()
    values = [1] + [new/last for new, last in zip(values[1:], values)]
    values = [elem * 100 - 100 for elem in values]
    plt.plot(years, values, label=sector)
inflation = INFLATION_VALUES[-3:]
plt.plot(years, inflation, label="inflation")
plt.title("Wzrost wydatków na R&D w różnych sektorach")
plt.xlabel("Rok")
plt.ylabel("W [%]")
plt.legend()
plt.savefig(save_path("sectors_vs_inflation"))
plt.show()



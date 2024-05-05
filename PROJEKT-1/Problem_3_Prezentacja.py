import os
import pandas as pd
from matplotlib import pyplot as plt


TASK_3_PATH = os.path.join(os.getcwd(), "data", "task_3", "cleaned")
IMG_PATH = os.path.join(os.getcwd(), "img", "task_3")

DEBT_PATH = os.path.join(TASK_3_PATH, "Debt.csv")
INCOME_PATH = os.path.join(TASK_3_PATH, "Income.csv")
INFLATION_PATH = os.path.join(TASK_3_PATH, "inflacja_lata.csv")
PKB_PATH = os.path.join(TASK_3_PATH, "PKB.csv")

def save_path(name):
    return os.path.join(IMG_PATH, name)


# debt vs income

debt_data = pd.read_csv(DEBT_PATH, delimiter=";")
years = debt_data["year"].tolist()
debt_values = debt_data["value"].tolist()
income_value = pd.read_csv(INCOME_PATH, delimiter=";")["value"].tolist()
plt.plot(years, debt_values, label="Dług Publiczny")
plt.plot(years, income_value, label="Dochód Państwa")
plt.title("Dług i Dochód Państwa")
plt.xlabel("Lata")
plt.ylabel("W [zł]")
plt.legend()
plt.savefig(save_path("inflacja_vs_dług"))
plt.show()

ratio = [deb/inc for deb, inc in zip(debt_values, income_value)]
plt.plot(years, ratio, label="Stosunek Długu do Dochodu")
plt.title("Stosunek Długu do Dochodu")
plt.xlabel("Lata")
plt.ylabel("W %")
# plt.legend()
plt.savefig(save_path("ratio"))
plt.show()

# Pkb
pkb_value = pd.read_csv(PKB_PATH, delimiter=";")["value"].tolist()
pkb_ration = [debt/pkb for debt, pkb in zip(debt_values, pkb_value)]
plt.plot(years, pkb_ration, label="Stosunek do PKB")
plt.title("Stosunek do PKB")
plt.xlabel("Lata")
plt.ylabel("W %")
# plt.legend()
plt.savefig(save_path("PKB_ratio"))
plt.show()

import os

RAW_PATH = os.path.join(os.getcwd(), "data", "task2", "raw")
CLEAN_PATH = os.path.join(os.getcwd(), "data", "task2", "cleaned")

PER_CAPITA_PATH = "R&D_per_capita.csv"
PKB_PATH = "R&D_PKB.csv"
SECTORS_PATH = "R&D_sectors.csv"
FILES = ["R&D_per_capita.csv", "R&D_PKB.csv", "R&D_sectors.csv"]

PATH = PKB_PATH
BLOCK = True  # to prevent random data loss

if BLOCK:
    exit()

for file in FILES:
    path = os.path.join(RAW_PATH, file)
    with open(path, "r") as h:
        data = h.readlines()
        if data[0][3:5] != "id":
            continue

    mask = [set() for _ in data[1].split(";")]
    for line in data[1:]:
        items = line.split(";")
        for set_, item in zip(mask, items):
            set_.add(item)

    real_mask = []
    for set_ in mask:
        if len(set_) == 1:
            real_mask.append(False)
        else:
            real_mask.append(True)

    path = os.path.join(CLEAN_PATH, file)
    cleaned_data = []
    for line in data[1:]:
        c_line = []
        for mask_, item in zip(real_mask, line.split(";")):
            if mask_:
                c_line.append(item)
        cleaned_data.append(";".join(c_line) + "\n")
    with open(path, "w") as h:
        h.writelines(cleaned_data)




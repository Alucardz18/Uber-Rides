import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# import dataset
dataset = pd.read_csv("UberDataset.csv")
dataset.head()

print(dataset.shape)
dataset.info()

# data processing
dataset["PURPOSE"].fillna(0, inplace=True)
dataset["START_DATE"] = pd.to_datetime(dataset["START_DATE"], errors="coerce") # object to datetime
dataset["END_DATE"] = pd.to_datetime(dataset["END_DATE"], errors="coerce") # object to datetime

# split datetime into date & time column
dataset["date"] = pd.DatetimeIndex(dataset["START_DATE"]).date
dataset["time"] = pd.DatetimeIndex(dataset["START_DATE"]).hour
# change time into day and night
dataset["day-night"] = pd.cut(x = dataset["time"],
                              bins = [0, 10, 15, 19, 24],
                              labels = ["Morning", "Afternoon", "Evening", "Night"])

# dropping null & duplicate values
dataset.dropna(inplace = True)
dataset.drop_duplicates(inplace = True)


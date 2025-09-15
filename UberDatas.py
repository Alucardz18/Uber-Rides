import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder



# import dataset
dataset = pd.read_csv("UberDataset.csv")
dataset.head()

#print(dataset.shape)
#dataset.info()

# data processing
dataset["PURPOSE"] = dataset["PURPOSE"].fillna("empty") # null values to 'empty'
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

# data visualization

#count unique values
obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
unique_values = {}
for col in object_cols:
    unique_values[col] = dataset[col].unique().size
#print(unique_values)

# creating visuals
plt.figure(figsize = (12,12))
plt.suptitle("Uber Ride Visualizations", fontsize=16)
# CATEGORY bar graph
plt.subplot(3,2,1)
sns.countplot(data=dataset, y = "CATEGORY", hue = "CATEGORY")
plt.title("Count of Rides by Category")
plt.xticks(rotation = 90)

# PURPOSE bar gragh
plt.subplot(3,2,2)
sns.countplot(data=dataset, y = "PURPOSE", hue="PURPOSE")
plt.title("Count of Rides by Purpose")
plt.xticks(rotation = 90)

# date-night bar gragh
plt.subplot(3,2,3)
plt.xticks(rotation = 90)
sns.countplot(data = dataset, y = "day-night",hue = "day-night")
plt.title("Count of Rides by Day - Night")

# comparing the purpose by the category
plt.subplot(3,2,4)
sns.countplot(data = dataset, x = "PURPOSE", hue = "CATEGORY")
plt.xticks(rotation = 90)
plt.title("Purpose VS Categories")

# display
plt.tight_layout()
plt.show()

object_cols = ["CATEGORY", "PURPOSE"]
# Set up a one-hot encoder that turns categories into numbers,
# and prevents errors from new/unseen values.
OH_encoder = OneHotEncoder(sparse_output = False, handle_unknown = "ignore")

# One-hot encode the object (categorical) columns and store in a new DataFrame
OH_cols = pd.DataFrame(OH_encoder.fit_transform(dataset[object_cols]))

# Keep the original row indices
OH_cols.index = dataset.index

# Assign column names to the encoded columns
OH_cols.columns = OH_encoder.get_feature_names_out()

# Drop the original categorical columns from the dataset
df_final = dataset.drop(object_cols, axis=1)

# Concatenate the dataset with the new one-hot encoded columns
dataset = pd.concat([df_final, OH_cols], axis=1)

# using heatmap find the correlation btwn the columns
numeric_dataset = dataset.select_dtypes(include = ["number"])
plt.figure(figsize=(10, 8))
plt.title("Correlation Heatmap of Numeric Features", fontsize=14)
sns.heatmap(numeric_dataset.corr(),
            cmap = "YlOrRd",
            fmt = ".2f",
            linewidths = .5,
            annot = True
            )

# display
plt.show()





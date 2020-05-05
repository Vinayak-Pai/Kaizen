import pandas as pd


reviews = pd.read_csv("/home/vipai/repos/some_code/Kaizen/datascience_ML_learning/dataquest_learning/pandas_tutorial/ign.csv")

print("head>>", reviews.head())
print("tail>>", reviews.tail())

print("shape>>", reviews.shape)

print(".........................Pandas.........................")
print("iloc>>", reviews.iloc[0:5, :])

print("loc>>", reviews.loc[0:5, :])

print("index>>", reviews.index)

some_reviews = reviews.iloc[10:20,]
print(some_reviews.head())

print(reviews.loc[2:5,["title", "score", "release_year"]])
print("\n")
print("............................Pandas Series...............................")
print(reviews[["score", "release_year"]])

print(type(reviews["score"]))

print("\n create a Series object manually")

s1 = pd.Series([1,2])
s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"])
print(s2)

print("\n ......................Creating A DataFrame in Pandas.............................")

print(pd.DataFrame([s1,s2]))

print("\n", pd.DataFrame(
    [
    [1,2],
    ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    columns=["column1", "column2"]
))

print("\n", pd.DataFrame(
    [
    [1,2],
    ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
))


print("\n", pd.DataFrame(
    {
    "column1": [1, "Boris Yeltsin"],
    "column2": [2, "Mikhail Gorbachev"]
    }
))


print("\n -----------------Pandas DataFrame Methods-------------------------")

print("mean", reviews["score"].mean())
print(reviews.mean())  # column wise
print("\n", reviews.mean(axis=1))  # row wise

print("corr", reviews.corr())

print("max", reviews["score"].max())
print("std", reviews["score"].std())
# more info : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html



print("\n ------------DataFrame Math with Pandas------------------------")
print(reviews["score"] / 2)

print("\n ------------DataFrame boolean index with Pandas------------------------")
print(reviews["score"] >7)


print("\n ------------------multiple conditions for filtering----------------------")

xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[(reviews["score"] > 7) & (reviews["platform"] == "Xbox One")]
print(filtered_reviews['score'].head())


print("\n --------------pandas plotting---------------")

a=reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")
import matplotlib.pyplot as plt
plt.show()

# more info : https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

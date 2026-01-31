import pandas as pd

data = {"A": [1, 2, 2, 1],
        "B": [3.1, 4.2, 1.5, 6.3],
        "C": [800, 150, 400, 210]
        }

df = pd.DataFrame(data) # create a data frame with the existing data
df["D"] = df["A"]+df["B"]+df["C"]
# i am not too sure what is meant by a new column "derived from existing columns", so i made the column "D" equal to the added values of A, B and C

print(df)
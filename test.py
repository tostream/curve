import pandas as pd
dataframe = pd.read_csv('content/sanofi.csv')
data = dataframe.values
y = data[:, 1].astype(float)
x = data[:, 0].astype(float)
print(y
      )
print(x)
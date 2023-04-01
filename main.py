import pandas as pd
from .Curve import *

pd.options.display.float_format = '{:,.4f}'.format

def result_rank(df: pd.DataFrame) -> pd.DataFrame:
  df['Rank'] = df['r_squared'].rank(ascending=False).astype(int)
  return df[['r_squared', 'Rank']].reset_index()

def split_popt(df: pd.DataFrame) -> pd.DataFrame:
  df= pd.DataFrame(df.popt.tolist(), index= df.index).reset_index()
  df.fillna('', inplace=True)
  return df

def merge_result(result_df: pd.DataFrame, popt_df: pd.DataFrame) -> pd.DataFrame:
  df = pd.merge(result_df, popt_df, how='inner', on ='index')
  df.rename(columns={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}, inplace=True)
  return df

def main(mode="w", header=True):
  dataframe = pd.read_csv(input_file)
  data = dataframe.values
  x = data[:, 0].astype(float)

    # Test curves
  curve_test_functions = [linear_curve, \
                          quad_curve, \
                          cubic_curve,\
                          quar_curve, \
                          quin_curve,\
                          PL4_curve, \
                          PL5_curve, \
                          gaussian_curve,\
                          power_curve, \
                          exponential_curve, \
                          exponential_half_curve
                          ]
  results = {}

  for function in curve_test_functions:
    results[function.__name__] = test_curve(x, y, function=function)

  results_df = pd.DataFrame.from_dict(results, orient='index', columns=['r_squared','popt'])
  
  results_ = result_rank(results_df)
  
  #where does i come from?
  results_['y'] = i 

  popt_df = split_popt(results_df[['popt']])

  table_i= merge_result(results_, popt_df)
  # # final.append(table_i)
  table_i.to_csv('result.csv', mode=mode, header=header)


final=[]
# final=pd.DataFrame()
for i in range(1,3):
  y = data[:, i].astype(float)
  if i==1:
    final.append(main())
  else:
    final.append(main(mode='a', header=False))


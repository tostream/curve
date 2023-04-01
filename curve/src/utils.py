
import numpy as np
from scipy.optimize import curve_fit #pip install scipy

#test function - R requared.
def r_square(x, y, popt, function=linear_curve):
  #To get R_squared
  residuals = y- function(x, *popt)
  ss_res = sum(residuals**2)
  ss_tot = sum((y-np.mean(y))**2)
  r_squared = 1 - (ss_res / ss_tot)
  return r_squared

#test function - Popt 
def test_curve(x, y, function=linear_curve):
  # curve fit
  popt, _ = curve_fit(function, x, y, maxfev=5000)
  r_squared = r_square(x, y, popt, function=function)  
  return r_squared, popt


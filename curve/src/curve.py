
import numpy as np

# # define the quadutic function
def quad_curve(x, a, b, c):
  return a * x**2 + b *x + c

def cubic_curve(x, a, b, c, d):
  return a * x**3 + b *x**2 + c* x + d

def quar_curve(x, a, b, c, d, e):
  return a * x**4 + b *x**3 + c* x**2 + d* x + e 

def quin_curve(x, a, b, c, d, e, f):
  return a * x**5 + b *x**4 + c* x**3 + d* x**2 + e* x + f

# # # def the symmeterical curve function
def PL4_curve(x, a, b, c, d):
  return d + (a - d) / (1 + np.power(x/c, b)) 

def PL5_curve(x, a, b, c, d, e):
  return d + (a - d) / np.power(1 + np.power(x/c, b), e)  


# # # def the bell curve function
def gaussian_curve(x, a, b, c):
  return a * np.exp(-np.power(x - b, 2) / (2 * np.power(c, 2)))

# # # def the power curve function
def power_curve(x, a, b):
  return a * np.power(x, b)

# # def the basic exp curve
def exponential_curve(x, a, b, c):
  return a + b * np.exp(-c*x)

# # def the exp 1/2 curve
def exponential_half_curve(x, a, b, c):
  return a + b / np.power(2 ,x/c)

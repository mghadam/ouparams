import numpy as np
def find(x):
  """
  Input:
	- x: the process dataset in numpy array format
  Output:
	- mu, sigma, theta
	Ornstein–Uhlenbeck process with long-term mean mu, volatility sigma, and mean reversion speed theta.
  """
  s_x = np.sum(x[:-1])
  s_y = np.sum(x[1:])
  s_xx = np.sum(x[:-1]**2)
  s_yy = np.sum(x[1:]**2)
  s_xy = np.sum(x[:-1] * x[1:])
  n = len(x)-1
  delta = 1

  mu = ((s_y*s_xx)-(s_x*s_xy))/(n*(s_xx-s_xy)-((s_x**2)-s_x*s_y)) # Mean

  theta = -(1/delta)*np.log((s_xy-mu*s_x-mu*s_y+n*mu**2)/(s_xx-2*mu*s_x+n*mu**2)) # Rate

  alpha = np.exp(-theta*delta)
  sigma_h = np.sqrt((1/n)*(s_yy-(2*alpha*s_xy)+((alpha**2)*s_xx)-(2*mu*(1-alpha)*(s_y-alpha*s_x))+(n*(mu**2)*(1-alpha)**2)))

  sigma = np.sqrt((sigma_h**2)*(2*theta/(1-alpha**2))) #Volatility

  return mu, sigma, theta

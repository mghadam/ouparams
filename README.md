# ouparams
A python module to Find Process Parameters for Ornstein-Uhlenbeck Processes
```
Input:
	- x the process dataset in numpy array format
Output:
	- mu, sigma, theta
	  Ornstein–Uhlenbeck process with long-term mean mu, volatility sigma, and mean reversion speed theta.
```

# Installation
Clone the github repository and install it with `pip install .`

or

```
pip install git+https://github.com/mghadam/ouparams.git
```

# Usage
```
# A sample OU process in numpy array format
import numpy
ds = numpy.array([0.8, 0.58606434, 0.49098481, 0.49343492, 0.54575029,0.51207641, 0.50084814, 0.52559959, 0.53000366, 0.53668143])

# Estimating the OU parameters
from ouparams import ouparams
mu, sigma, theta = ouparams.find(ds)
# 0.5171166243459767, 0.038885729337555484, 1.5906939803229536

```
The calculation matches with Mathematica's [FindProcessParameters](https://reference.wolfram.com/language/ref/FindProcessParameters.html) for [OrnsteinUhlenbeckProcess](https://reference.wolfram.com/language/ref/OrnsteinUhlenbeckProcess.html)
```
ds = {0.8, 0.58606434, 0.49098481, 0.49343492, 0.54575029, 0.51207641,
    0.50084814, 0.52559959, 0.53000366, 0.53668143};
FindProcessParameters[ds, 
 OrnsteinUhlenbeckProcess[\[Mu], \[Sigma], \[Theta]]]
 {\[Mu] -> 0.517117, \[Sigma] -> 0.0388857, \[Theta] -> 1.59069}
```

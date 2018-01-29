from __future__ import division
import numpy as np
def test_div():
	assert 2/8==0.25

def test_numpy():
	x=np.array([2])
	y=np.array([8])
	assert x[0]/y[0]==0.25
	



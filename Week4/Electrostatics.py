import numpy as np

def pointPotential(X,Y,q,posx,posy):
	'''Expects q in coulombs, and points in meters.
	Gives Vxy when given origin point (x,y) and location (posx, posy)'''
	Vxy=(8.89e9)*q/((X-posx)**2.+(Y-posy)**2.)**(1/2)
	return Vxy

def dipolePotential(X,Y,q,posx,angle):
	"""Set Vxy with equation below to check total potential in the x axis at posx.
	Expects q in coulombs and points in meters."""
	k=8.9e9
	Vxy = k*q/((X-posx*np.cos(angle))**2.+Y**2.)**(1/2) + k*q/((X+posx*np.cos(-1*angle))**2.+Y**2.)**(1/2)
	return Vxy

import numpy as np

def pointPotential(X,Y,q,posx,posy):
	'''Expects q in coulombs, and points in meters.
	Gives Vxy when given origin point (x,y) and location (posx, posy)'''
	Vxy=(8.89e9)*q/((X-posx)**2.+(Y-posy)**2.)**(1/2)
	return Vxy

def dipolePotential(x,y,q,posx,angle):
	"""Set Vxy with equation below to check total potential in the x axis at posx.
	Expects q in coulombs and points in meters."""
	k=8.9e9
	Vxy = k*q/((X-posx*cos(angle))**2.+Y**2.)**(1/2) + k*q/((X+posx*cos(-1*angle))**2.+Y**2.)**(1/2)
	return Vxy

def pointField(x,y,q,Xq,Yz):
	k = 8.89e9
	"""takes arrays(x,y), charge(q), and position, (Xq,Yq) and returns a tuple of electric field components"""
	Ex=((k*q)*(x-Xq))/(((x-Xq)**2)+((y-Yq)**2))**(1/2.)
	Ey=((k*q)*(y-Yq))/(((x-Xq)**2)+((y-Yq)**2))**(1/2.)
	return Ex
	return Ey

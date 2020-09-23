H = 1
#Hours spent walking
W = 115
#Weight in kilos
L = 10
#Weight of Load
V = 1
#Speed in m/s
n = 1
#Terrain factor, paved roads being 1, gravel roads being 1.2
G = 1
#Gradient of roads, averaged throughout walk
M = (1.5*W) + (2.0*(W+L))*((L/W)**2) + (n*(W+L)) * ((1.5*V**2)+(0.35*V)*G)
#M is the metabolic rate, aka, KCal per Hour
A = M*H
#Amount of calories burned on the walk
Speak = ("With the current numbers you will burn " + str(A) + " KCal per Hour walking!")
print (Speak)

#Lbs =
##Kilos to be converted to lbs
#KPH =
##Your speed in Kilometers per hour
#MPH =
##Your speed in Miles per hour
#WeighLbs-K = Lbs / 2.2
#Kph-m/s = 0.277778 * KPH
#Mph-m/s = 0.44704 * MPH

#print (WeightLbs-K)
#print (Kph-m/s)
#print (Mph-m/s)



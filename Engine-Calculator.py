#Kilogram Thrust = = kN*101.9716005
#TWR = Kgt/Wm
#G = Constant of Gravity
#Wm = Wet Mass
#Dm = Dry Mass
#Dv = Δv
#Isp = Specific Impulse
#Δv= (Isp*G)*ln(Wm/Dm)x'
import math 
M0 = float(input("Wet Mass of the Rocket in Tons: "))
M1 = float(input("Mass of the Rocket at the staging event in Tons: "))
o = float(input("How much DeltaV do you want this stage to have: "))
M0 = M0*1000 #Convert to Kg
M1 = M1*1000 #Convert to Kg
#Name, Isp, Thrust in Kn
def sL(M0, M1, o):
  #List of Sea Level Engine Stats
  sLEngines = [("Spider", 260, 1.79, 0.02), ("Twitch", 275, 15, 0.08),("Thud", 275, 108.20, 0.9), ("Puff", 120, 9.60, 0.09), ("Ant", 80, 0.51, 0.02), ("Spark", 265, 16.56, 0.13), ("Terrier",85, 14.78, 0.50), ("Reliant",265,205.16, 1.25), ("Swivel", 250,167.97, 1.5), ("Vector", 295, 936.51, 4), ("Dart", 290, 153.53, 1), ("Nerv", 185, 13.88, 3), ("Poodle", 90, 64.29, 1.75), ("Skipper", 280, 568.75, 3), ("Mainsail", 285, 1379.03, 6), ("Twin Boar", 280, 1866.67, 10.5), ("Rhino", 205, 1205.88, 9), ("Mammoth",295, 3746.03, 15), ("Rapier", 275, 162.30, 2)]
  sLDv = []
  TWRsL = []
  q = 1
  #Looking for ISP, Name, and Thrust, and Engine Weight in the list
  for i in sLEngines: 
    x = i[0]
    y = i[1]
    z = i[2]
    aa = i[3] * 1000
    Kgt = z*101.9716005 #Converts Kilonewtons of thrust to Kilograms
    twr = Kgt/M0 
    while twr < 1.2: #Should figure out how many engines needed to get a 1.2 TWR
      q = int(1.2/twr)+1 #Ints will round down until 0.99999999999 (11 9s)
      twr = twr*q #applying the change to TWR
    dV = ((y*9.807)*math.log(((M0+(q*aa)))/(M1+(q*aa)), math.e))
    #dV = ISP*Gravitational Constant * nl(Wet Mass+Engine Weight/Dry Mass + Engine Weight)
    sLDv.append((q, x, "DeltaV: ", dV, "TWR: ", twr))
  print("Possible Engines: ")
  GoodSL = []
  for i in sLDv: #Searches  from the new list
    a = i[0] #Engine Amount
    b = i[1] #Name
    c = i[3] #dV
    d = i[5] #TWR
    if a <= 6 and c >= o and 1.2 <=d <= 1.8:
      GoodSL.append(("Engine Name: ", b, "Engine Count: ", a, "DeltaV: ", c, "TWR: ", d)) #New List of Actual possible engines
  print(GoodSL)
  print(" ")#Space
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")#Space
  print(sLDv)#This is only for testing purposes and will be removed in the end
  return(GoodSL) #Returning it just so I can use it later
sL(M0, M1, o) #Calling Function

#Kgt = kN*101.9716005
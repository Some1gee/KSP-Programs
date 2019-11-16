#Kilogram Thrust = = kN*101.9716005
#TWR = Kgt/Wm
#G = Constant of GravitISP1
#Wm = Wet Mass
#Dm = DrISP1 Mass
#Dv = Δv
#Isp = Specific Impulse
#Δv= (Isp*G)*ln(Wm/Dm)Name1'
import math 
M0 = float(input("Wet Mass of the Rocket in Tons: "))
M1 = float(input("Mass of the Rocket at the staging event in Tons: "))
dVreq = float(input("How much DeltaV do you want this stage to have: "))
constOfGrav = str(input("Name of Celestial Body in which you are in: (Kerbol, Moho, Eve, Gilly, Kerbin, Mun, Minmus, Duna, Ike, Dres, Jool, Laythe, Vall, Tylo, Bop, Pol, Eeloo) "))
vac = 0
M01 = M0*1000 #Convert to Kg
M11 = M1*1000 #Convert to Kg
#Name, Isp, Thrust in Kn
def engineCalc(M0, M1, dVreq, M01, M11, constOfGrav, vac):
  #List of Sea Level Engine Stats
  if vac == False:
    sLEngines = [("Spider", 260, 1.79, 0.02), ("Twitch", 275, 15, 0.08),("Thud", 275, 108.20, 0.9), ("Puff", 120, 9.60, 0.09), ("Ant", 80, 0.51, 0.02), ("Spark", 265, 16.56, 0.13), ("Terrier",85, 14.78, 0.50), ("Reliant",265,205.16, 1.25), ("Swivel", 250,167.97, 1.5), ("Vector", 295, 936.51, 4), ("Dart", 290, 153.53, 1), ("Nerv", 185, 13.88, 3), ("Poodle", 90, 64.29, 1.75), ("Skipper", 280, 568.75, 3), ("Mainsail", 285, 1379.03, 6), ("Twin Boar", 280, 1866.67, 10.5), ("Rhino", 205, 1205.88, 9), ("Mammoth",295, 3746.03, 15), ("Rapier", 275, 162.295, 2), ("Mastadon", 290, 1283.63, 5), ("Cheetah", 150, 52.82, 1), ("Bobcat", 290, 374.19, 2), ("Skiff", 265, 240.91, 1.6), ("Wolfhound", 70, 69.08, 3.3), ("Kodiak", 285, 247, 1.25), ("Cub", 280, 28.9, 0.18)]
    sLDv = []
    TWRsL = []
    engineCount = 1
    #Looking for ISP, Name, and Thrust, and Engine Weight in the list
    for i in sLEngines: 
      Name1 = i[0]
      ISP1 = i[1]
      ThrustkN1 = i[2]
      WeightT = i[3]
      WeightkG = i[3] * 1000
      twr = ThrustkN1/((M0+(WeightT))*constOfGrav)#Original TWR Calc
      engineCount = int((1.35/twr)+1) #ints will round down until 0.99999999999 (11 9s)
      twr = round((ThrustkN1*engineCount)/((M0+(WeightT*engineCount))*constOfGrav), 2)#Second TWR Calc
      dV = round(((ISP1*constOfGrav)*math.log(((M01+(engineCount*WeightkG)))/(M11+(engineCount*WeightkG)), math.e)))
      #dV = ISP*Gravitational Constant * ln(Wet Mass+Engine Weight/Dry Mass + Engine Weight)
      sLDv.append((engineCount, Name1, "DeltaV: ", dV, "TWR: ", twr))
    print("Possible Engines: ")
    GoodSL = []
    for i in sLDv: #Searches  from the new list
      engAmount = i[0] #Engine Amount
      engName = i[1] #Name
      dV = int(i[3]) #dV
      twrF = round(i[5], 1) #TWR
      if engAmount <= 6 and dV >= dVreq and 1.2 <= twrF:
        GoodSL.append(("Engine Name: ", engName, "Engine Count: ", engAmount, "DeltaV: ", dV, "TWR: ", twrF)) #New List of Actual possible engines
    print(GoodSL)
    print(" ")#Space
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")#Space
    print(sLDv)#This is only for testing purposes and will be removed in the end
    return(GoodSL) #Returning it just so I can use it later
  elif vac == True:
    print("Vacuum")
#Going through Variable Gravity to find which one
if constOfGrav == "Kerbol":
  constOfGrav = 17.1
  vac = True
elif constOfGrav == "Moho":
  constOfGrav = 2.7
  vac = True
elif constOfGrav == "Eve":
  constOfGrav = 16.7
  vac = False
elif constOfGrav == "Gilly":
  constOfGrav = 0.049
  vac = True
elif constOfGrav == "Kerbin":
  constOfGrav = 9.81
  vac = False
elif constOfGrav == "Mun":
  constOfGrav = 1.63
  vac = True
elif constOfGrav == "Minmus":
  constOfGrav = 0.491
  vac = True
elif constOfGrav == "Duna":
  constOfGrav = 2.94
  vac = False
elif constOfGrav == "Ike":
  constOfGrav = 1.1
  vac = True
elif constOfGrav == "Dres":
  constOfGrav = 1.13
  vac = True
elif constOfGrav == "Tylo":
  constOfGrav = 7.85
  vac = True
elif constOfGrav == "Vall":
  constOfGrav = 2.31
  vac = True
elif constOfGrav == "Bop":
  constOfGrav = 0.589
  vac = True
elif constOfGrav == "Pol":
  constOfGrav = 0.373
  vac = True
elif constOfGrav == "Eeloo":
  constOfGrav = 1.69
  vac = True
elif constOfGrav == "Jool" or "Laythe":
  constOfGrav = 7.85
  vac = False
else:
  print("Try Again")
  constOfGrav = str(input("Name of Celestial Body in which you are in: (Kerbol, Moho, Eve, Gilly, Kerbin, Mun, Minmus, Duna, Ike, Dres, Jool, Laythe, Vall, Tylo, Bop, Pol, Eeloo) "))
engineCalc(M0, M1, dVreq, M01, M11, constOfGrav, vac) #calling function
#Kgt = kN*101.9716005
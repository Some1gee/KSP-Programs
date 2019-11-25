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
maxEngineCount = int(input("Maximum acceptable number of engines: "))
reqVecRange = float(input("What is the Minimum Required Vector Range (0 and above): "))
radialAsk = str(input("Are radial engines acceptable? Answer with 'True', 'False', or 'Only': "))
sizeAsk = float(input("Maximum Possible Engine Size (m):"))
srbAsk = str(input("Are SRBs acceptable? Answer with 'True', 'False', or 'Only': "))
M01 = M0*1000 #Convert to Kg
M11 = M1*1000 #Convert to Kg 
#Name, Isp, Thrust in Kn
def engineCalc(M0, M1, dVreq, M01, M11, constOfGrav, vac, maxEngineCount, reqVecRange, radialAsk, sizeAsk):
  #List of Sea Level Engine Stats
  if vac == False:
    sLEngines = [("Spider", 260, 1.79, 0.02, 10, 0, 0, 0), ("Twitch", 275, 15, 0.08, 8, 0, 0, 0),("Thud", 275, 108.20, 0.9, 8, 0, 0, 0), ("Puff", 120, 9.60, 0.09, 6, 0, 0, 0), ("Ant", 80, 0.51, 0.02, 0, 1, 0, 0), ("Spark", 265, 16.56, 0.13, 3, 1, 0.6, 0), ("Terrier",85, 14.78, 0.50, 4, 1, 1.25, 0), ("Reliant",265,205.16, 1.25, 0, 1, 1.25, 0), ("Swivel", 250,167.97, 1.5, 3, 1, 1.25, 0), ("Vector", 295, 936.51, 4, 10.5, 1, 1.25, 0), ("Dart", 290, 153.53, 1, 0, 0, 1.25, 0), ("Nerv", 185, 13.88, 3, 0, 1, 1.25, 0), ("Poodle", 90, 64.29, 1.75, 4.5, 1, 2.5, 0), ("Skipper", 280, 568.75, 3, 2, 1, 2.5, 0), ("Mainsail", 285, 1379.03, 6, 2, 1, 2.5, 0), ("Twin Boar", 280, 1866.67, 10.5, 1.5, 1, 2.5, 0), ("Rhino", 205, 1205.88, 9, 4, 1, 3.75, 0), ("Mammoth",295, 3746.03, 15, 2, 1, 3.75, 0), ("Rapier", 275, 162.295, 2, 3, 1, 1.25, 0), ("Mastadon", 290, 1283.63, 5, 5, 1, 2.5, 0), ("Cheetah", 150, 52.82, 1, 4, 1, 1.25, 0), ("Bobcat", 290, 374.19, 2, 5, 1, 1.875, 0), ("Skiff", 265, 240.91, 1.6, 2, 1, 2.5, 0), ("Wolfhound", 70, 69.08, 3.3, 3, 1, 1.875, 0), ("Kodiak", 285, 247, 1.25, 0, 1, 1.25, 0), ("Cub", 280, 28.9, 0.18, 22.5, 0, 0, 0), ("Sepratron", 118, 13.79, 0.0125, 0, 0, 0, 1), ("Kickback", 195, 593.86, 4.5, 1, 0, 1.25, 1), ("Thumper", 175, 250, 1.5, 1, 0, 1.25, 1), ("Hammer", 170, 197.9, 0.75, 1, 0, 1.25, 1), ("Flea", 140, 162.91, 0.45, 1, 0, 1.25, 1)]
    #Name, ISP, Thrust in kN, Weight in Tons, Vectoring Range, Radial Mounted (0 = True), Size, SRB (0 = No)
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
      vectorRange1 = i[4]
      radialTF = i[5]
      size1 = i[6]
      twr = ThrustkN1/((M0+(WeightT))*constOfGrav)#Original TWR Calc
      engineCount = int((1.35/twr)+1) #ints will round down until 0.99999999999 (11 9s)
      twr = round((ThrustkN1*engineCount)/((M0+(WeightT*engineCount))*constOfGrav), 2)#Second TWR Calc
      dV = round(((ISP1*constOfGrav)*math.log(((M01+(engineCount*WeightkG)))/(M11+(engineCount*WeightkG)), math.e)))
      #dV = ISP*Gravitational Constant * ln(Wet Mass+Engine Weight/Dry Mass + Engine Weight)
      sLDv.append((engineCount, Name1, "DeltaV: ", dV, "TWR: ", twr, "Vector Range: ", vectorRange1, "Radial True/False:", radialTF, "Size (m):", size1))
      #Add it to Sea level Delta V List (Name was created before it's final purpose was)
    print("Possible Engines: ")
    GoodSL = []
    for i in sLDv: #Searches  from the new list
      engAmount = i[0] #Engine Amount
      engName = i[1] #Name
      dV = int(i[3]) #dV
      twrF = round(i[5], 1) #TWR
      vectorRange2 = i[7]
      radialTF2 = i[9]
      size2 = i[11]
      if radialTF2 == 0 and radialAsk == "Only": #Changing radialTF2 from the opposite of Binary to Boolean
        radialTF2 = "Only"
      elif radialTF2 == 1 and radialAsk == "Only": #Engine is not Radial and Radial Ask is Only Radial
        radialTF2 = "False"
      elif radialTF2 == 0 and radialAsk == "True": #Engine is radial and Radial Ask is Everything
        radialTF2 = "True"
      elif radialTF2 == 1 and radialAsk == "True": #Engine is not radial and Radial Ask is Everything
        radialTF2 = "True"
      elif radialTF2 == 0 and radialAsk == "False": #Engine is radial and Radial Ask is Not Radial
        radialTF2 = "No"
      else: #Engine is not radial and Radial Ask is not radial
        radialTF2 = "False"
      if engAmount <= maxEngineCount and dV >= dVreq and 1.2 <= twrF and vectorRange2 >= reqVecRange and radialTF2 == radialAsk and size2 <= sizeAsk: 
        GoodSL.append(("Engine Name: ", engName, "Engine Count: ", engAmount, "DeltaV: ", dV, "TWR: ", twrF, "Vector Range: ", vectorRange2)) #New List of Actual possible engines
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
else:#This currently doesn't work
  print("Try Again")
  constOfGrav = str(input("Name of Celestial Body in which you are in: (Kerbol, Moho, Eve, Gilly, Kerbin, Mun, Minmus, Duna, Ike, Dres, Jool, Laythe, Vall, Tylo, Bop, Pol, Eeloo) "))
engineCalc(M0, M1, dVreq, M01, M11, constOfGrav, vac, maxEngineCount, reqVecRange, radialAsk, sizeAsk) #calling function
#Kgt = kN*101.9716005
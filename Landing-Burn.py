import krpc
import math

conn = krpc.connect(name='Landing Burn')

vessel = conn.space_center.active_vessel
space_center = conn.space_center

altitude = conn.add_stream(getattr, vessel.flight(), "mean_altitude")

gravConst = float(vessel.orbit.body.surface_gravity)

while int(altitude()) > 0:
twr = round((float(vessel.available_thrust)*0.001)/((float(vessel.mass)*0.001)*gravConst), 2)
print(twr)

ExhaustVelocity = vessel.specific_impulse*gravConst

DeltaVelocity = (ExhaustVelocity)*math.log(vessel.mass/vessel.dry_mass)

DeltaTime = ((vessel.mass*ExhaustVelocity)/vessel.available_thrust)*(1-math.e**(-DeltaVelocity/ExhaustVelocity))

acceleration = (vessel.mass/vessel.available_thrust)*DeltaTime

finalVelocity = (int(vessel.speed)+int(acceleration))

finalAltitude = 0

equation = ((twr/gravConst)**2)-(2((vessel.speed**2)-(finalVelocity**2))/(4*(gravConst)*(altitude-finalAltitude)))*(twr/gravConst)-(1+(((2*(vessel.speed))*2)-((2*(finalVelocity))*2))/((4*gravConst)*(altitude-finalAltitude)))
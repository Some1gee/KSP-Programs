import krpc
import math

conn = krpc.connect(name='Landing Burn')

vessel = conn.space_center.active_vessel
space_center = conn.space_center

srf_frame = vessel.orbit.body.reference_frame

altitude = conn.add_stream(getattr, vessel.flight(), "mean_altitude")

gravConst = float(vessel.orbit.body.surface_gravity)

twr = round((float(vessel.available_thrust)*0.001)/((float(vessel.mass)*0.001)*gravConst), 2)
print(twr)

ExhaustVelocity = vessel.specific_impulse*gravConst

DeltaVelocity = (ExhaustVelocity)*math.log(vessel.mass/vessel.dry_mass)

finalVelocity = 0

finalAltitude = 0

speed = vessel.flight(srf_frame).speed

accelerationDueToThrust = (vessel.mass*gravConst)-vessel.available_thrust

thrustNeeded = (accelerationDueToThrust/gravConst)-vessel.mass                  

a = 1**2

#ax^2 + bx + c = 0
print(vessel.flight(srf_frame).speed)
a = 1
b = -1*(2((vessel.flight(srf_frame).speed**2)-(finalVelocity**2))/(4*(gravConst)*(altitude-finalAltitude)))
c = -1*(1+((2*((vessel.flight(srf_frame).speed**2)-(finalVelocity**2))))/((4*gravConst)*(altitude-finalAltitude)))
x = accelerationDueToThrust/gravConst
#(-b +- sqrt(b^2 - 4ac))/2a
root1 = ((-1*b) + math.sqrt((b**2)-(4*a*c)))/(2*a)
root2 = ((-1*b) - math.sqrt((b**2)-(4*a*c)))/(2*a)

drag = vessel.flight(srf_frame).drag()
DRAG = math.sqrt(drag[0]**2+drag[1]**2+drag[2]**2)


if root1 > 0:
    accelerationDueToThrust = root1
else:
    accelerationDueToThrust = root2

desiredThrust = accelerationDueToThrust*gravConst*vessel.mass*drag

if desiredThrust >= vessel.available_thrust:
    vessel.control.throttle = 1


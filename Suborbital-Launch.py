import krpc
import time

conn = krpc.connect(name='Sub-orbital flight')

vessel = conn.space_center.active_vessel

	
#GNC
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

print("GNC is GO")
time.sleep(5)
print(vessel.name + " is GO for Launch")
vessel.control.activate_next_stage()

#Empty
fuel_amount = conn.get_call(vessel.resources.amount, 'SolidFuel')
altitude = conn.add_stream(getattr, vessel.flight(), "mean_altitude")
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(fuel_amount), 
    conn.krpc.Expression.constant_float(0.1)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print("We have SRB flame out at " + str(int(altitude())) + " meters!")

#Capsule Seperation
expr_altitude = conn.get_call(getattr, vessel.flight(), "mean_altitude")
expr = conn.krpc.Expression.greater_than(
    conn.krpc.Expression.call(expr_altitude),
    conn.krpc.Expression.constant_double(64000)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print("We are go for SRB Jettison")
vessel.control.activate_next_stage()
print("SRB Jettison Confirmed")

#Vacuum
expr = conn.krpc.Expression.greater_than_or_equal(
    conn.krpc.Expression.call(expr_altitude),
    conn.krpc.Expression.constant_double(70001)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()

#Reentry
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(expr_altitude),
    conn.krpc.Expression.constant_double(70000)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print("Reentry has begun. Reorienting capsule for descent.")
vessel.auto_pilot.disengage()
vessel.auto_pilot.sas = True
time.sleep(1)
vessel.auto_pilot.sas_mode = conn.space_center.SASMode.retrograde
time.sleep(1)
print("Reorientation complete, Capsule is ready for descent.")

#Parachute Landing
speed = conn.get_call(getattr, vessel.flight(), "speed")
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(expr_altitude),
    conn.krpc.Expression.constant_double(5000)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
expr = conn.krpc.Expression.less_than(
    conn.krpc.Expression.call(speed),
    conn.krpc.Expression.constant_double(300)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print("Parachute Deployment")
vessel.control.activate_next_stage()
print("The Parachute has deployed")

expr = conn.krpc.Expression.equal(
    conn.krpc.Expression.call(expr_altitude),
    conn.krpc.Expression.constant_double(1000)
)
event = conn.krpc.add_event(expr)
with event.condition:
    event.wait()
print("Parachutes have caught")

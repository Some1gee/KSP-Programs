import krpc
conn = krpc.connect()
vessel = conn.space_center.active_vessel
print(vessel.name)
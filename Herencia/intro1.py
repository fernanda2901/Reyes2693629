class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

v=Vehicle()
lv=LandVehicle()
tv=TrackedVehicle()

for cls1 in [v,lv,tv]:
      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
          print(isinstance(cls1,cls2), end="\t")
      print()


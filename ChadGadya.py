defChadGadyaMaker(n):
  t="""Then came the Holy One Blessed be He and slew the the Angel of Death, that killed the butcher, that slaughtered the ox, that drank the water, that quenched the fire, that burnt the stick, that beat the dog, that bit the cat, that ate the goat, 
  That Father bought for two zuzim, Chad gadya. Chad gadya. """.split(",")
  t2=[x.lstrip(" ") for x in t][::-1]
  return("Then came the {},{}".format(t2[n+1].split(" ")[-1],','.join(t2[:n+1][::-1])))
ChadGadyaMaker(int(input("Enter your verse as a number from 1-10: ")))

# Simulated Mobile Network - Columbia MD
## Network Polygon
# top-right (Elicott City):             39.267732266577795, -76.79912666240163
# bottom-right (Columbia Pike):         39.202143545427270, -76.85878560274975
# bottom-left (Patient First Columbia): 39.209267634946656, -76.88718021114587
# top-left (Centennial Park North):     39.250097318923764, -76.85233935397152

from network import *
import random 

DEBUG=1

print("#### Creating Mobile Network #################")
net = mobileNetwork("MyNetwork")
if DEBUG > 4:
    print(net) # display class

# Zone 1
if DEBUG:
    print ("# Adding APs @ Zone 1")
# Macy's Columbia Town Center
net.addAP("ap010", latitude=39.217213628090825, 
            longitude=-76.85957073101905, zone="zone1", maxUsers=5, coverageSqKm=2.5)
# MOD Pizza
net.addAP("ap011", latitude=39.21407569438349,
          longitude=-76.86522479467084, zone="zone1", maxUsers=5, coverageSqKm=2.5)
# Sheraton Columbia Town Center
net.addAP("ap011", latitude=39.21250780710554, 
            longitude=-76.86321079953738, zone="zone1", maxUsers=8, coverageSqKm=2)
# Merriweather Post Pavilion
net.addAP("ap012", latitude=39.209543247787224, 
            longitude=-76.86141043494047, zone="zone1", maxUsers=10, coverageSqKm=1.5)
# Columbia Lake Front Stage - Lake Kittamaquindi
net.addAP("ap013", latitude=39.21495423182717, 
            longitude=-76.85575246041245, zone="zone1", maxUsers=5, coverageSqKm=2.5)
# Wilde Lake
net.addAP("ap014", latitude=39.22422842026038,
            longitude=-76.86052789553318, zone="zone1", maxUsers=5, coverageSqKm=2.5)
# Starbucks - Lynx Lane
net.addAP("ap015", latitude=39.221111731250815,
          longitude=-76.87511250598043, zone="zone1", maxUsers=5, coverageSqKm=2.5)
# Bryan Woods Elemetary School
net.addAP("ap016", latitude=39.22116730331977,
          longitude=-76.86680352716961, zone="zone1", maxUsers=5, coverageSqKm=2.5)

# Zone 2
if DEBUG:
    print ("# Adding APs @ Zone 2")
# Howard Communty College
net.addAP("ap020", latitude=39.213779016539505, 
            longitude=-76.87799058089493, zone="zone2", maxUsers=10, coverageSqKm=2.5)
# Howard County General Hospital
net.addAP("ap021", latitude=39.214873069305725, 
            longitude=-76.88622758163278, zone="zone2", maxUsers=15, coverageSqKm=1)
# Columbia Athletic Club
net.addAP("ap021", latitude=39.222690089422265,
          longitude=-76.88635843141691, zone="zone2", maxUsers=10, coverageSqKm=2.5)

# Zone 3
if DEBUG:
    print ("# Adding APs @ Zone 3")
# Centennial Lake
net.addAP("ap030", latitude=39.24084419501035,
          longitude=-76.86047409502802, zone="zone3", maxUsers=5, coverageSqKm=2.5)
# Cedar Park Pavilion
net.addAP("ap031", latitude=39.232823189437674,
          longitude=-76.88315261512867, zone="zone3", maxUsers=5, coverageSqKm=2.5)
# Dorsey Hall Professional Park
net.addAP("ap032", latitude=39.24450897507948,
          longitude=-76.83602312634758, zone="zone3", maxUsers=5, coverageSqKm=2.5)
# Elicott City Fire Dept Station 2
net.addAP("ap032", latitude=39.25531630846513,
          longitude=-76.82027384604649, zone="zone3", maxUsers=5, coverageSqKm=2.5)
# Circuit Court for Howard County MD
net.addAP("ap032", latitude=39.237182632628766,
          longitude=-76.82819139355466, zone="zone3", maxUsers=5, coverageSqKm=2.5)
# Howard County Animal Control & Adoption
net.addAP("ap033", latitude=39.21680694339477,
          longitude=-76.80895125045787, zone="zone3", maxUsers=5, coverageSqKm=2.5)


## UEs

net.addUser('ue001', serviceQuality=round(random.uniform(1, 5), 2))
net.addUser('ue003', serviceQuality=round(random.uniform(1, 5), 2))
net.addUser('ue004', serviceQuality=round(random.uniform(1, 5), 2))
net.addUser('ue005', serviceQuality=round(random.uniform(1, 5), 2))

net.Users["ue003"].addAP("ap001")
net.Users["ue003"].addAP("ap002",status="primary")

net.Users["ue004"].addAP("ap001",status="primary")

net.Users["ue005"].addAP("ap001")
net.Users["ue005"].addAP("ap001")

if DEBUG > 2:
    print("#### All network #############################")
    print(net.getAll())

if DEBUG:
    print("#### All APs in Network ######################")
    print(net.getAllAPs())

if DEBUG:
    print("#### All UEs in Network ######################")
    print(net.getAllUsers())

print("#### DONE ####################################")

#
# END OF FILE
#
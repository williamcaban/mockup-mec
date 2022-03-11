#
class mecZones():
    def __init__(self,
            zoneID="zone0",
            numAPs=0,
            numAPsUnserviceable=0):
        self.zoneID=zoneID
        self.numAPs=numAPs 
        self.numAPsUnserviceable=numAPsUnserviceable
        self.APs=[] # list of APs in the zone

    def numUsers():
        """
        return num of users actives in the zone (sum of APs users)
        """
        pass


class mecAP():
    _site={}
    _activeUsers=[]
    _standbyUsers=[]
    def __init__():
        _site={
            "apId":"ap000",
            "latitude": 0.000,
            "longitude": 0.000,
            "maxUsers": 10
        }
    def addUser(user, isActive):
        pass
    def removeUser(user)
        pass


class mecUsers():
    _UE = {}
    def __init__():
        _UE = {
            "userId":"ue000",
            "latitude": 0.000,
            "longitude": 0.000,
            "activeAP": "ap000",
            "standbyAP" : ["ap000","ap001"]
            "serviceQuality": "",
            "bandwidthMbps": 10.5,
        }
    

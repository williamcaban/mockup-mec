#
import random 

# Class representing an Access Point or Cell Site
class mecAP():
    def __init__(self,
                 apId="ap000",
                 latitude=0.000,
                 longitude=0.000,
                 zone="zone0",
                 maxUsers=10,
                 coverageSqKm=2.5):
        # site info
        self.apId = apId
        self.latitude = latitude
        self.longitude = longitude
        self.zone = zone

        # constraints for simulations
        self.maxUsers = maxUsers  # qty UEs supported by AP
        self.coverageSqKm = coverageSqKm # square kilometer coverage for AP
        self.regUsers = {} # registered users {"userId":True}
        self.serviceScore = {}  # AP to App service score (1-5) eg. {"appName":4.5}

    def __repr__(self):
        return str(vars(self))

    def addUser(self, userId, isActive=True):
        """
        return errorCode,errorMsg
        """
        errorCode=0
        errorMsg=""
        if len(self.regUsers) <= self.maxUsers:
            self.regUsers[userId] = isActive
            errorMsg="Successfully added"
        else:
            errorCode=1
            errorMsg="Error: Max user limit reached"
        return errorCode,errorMsg

    def removeUser(self, userId):
        try:
            self.regUsers.pop(userId)
        except KeyError:
            pass

    def getServiceScore(self, destApp):
        """
        return Application Service Score
        """
        try:
            appScore = self.serviceScore[destApp]
        except KeyError:
            # App is not registered. Create and assign appScore
            appScore = round(random.uniform(1, 5), 2)
            self.serviceScore[destApp] = appScore
        return appScore


# Class representing a UE or MEC User
class mecUser():
    def __init__(self,
                 userId="ue000",
                 latitude=0.00,
                 longitude=0.00,
                 bandwidthMbps=10.5,
                 serviceQuality=1):
        self.userId = userId
        self.latitude = latitude
        self.longitude = longitude
        # registration
        self.UPF = ""
        self.primaryAP = ""
        self.APs = {}
        # constraints for simulations
        self.bandwidthMpbs = bandwidthMbps
        self.serviceQuality = serviceQuality

    def __repr__(self):
        return str(vars(self))

    def addAP(self, nameAP, status="active"):
        self.APs[nameAP] = status
        if status == "primary":
            self.primaryAP = nameAP

    def removeAP(self, nameAP):
        try:
            del self.APs[nameAP]
            # if disconnected AP is primary, re-assign a primary
            if self.primaryAP == nameAP:
                if len(self.APs) > 0:
                    self.primaryAP = list(self.APs.keys())[0]
                else:
                    self.primaryAP = ""
        except KeyError:
            pass

    def getAPs(self):
        return self.APs.keys()


# Class representing a simulated mobile network
class mobileNetwork():
    """
    Simulate mobile network deployment
    """
    def __init__(self,
            networkName="Simulated Mobile Network"):
        self.networkName = networkName
        self.APs={}      # {'apId':<mecAP object'}
        self.Users = {}  # {'userId':<mecUser object'}
    
    def __repr__(self):
        return "<class> mobileNetwork "+self.networkName

    def getAPsinZone(self, zoneName):
        """
        return a list of APs on a particular zone
        """
        tmp=[]
        for ap in self.APs.keys():
            if self.APs[ap].zone == zoneName:
                tmp.append(ap)
        return tmp

    def getUserVisibleAPs(self, userId):
        """
        return a list of APs visible by the UE userId
        """
        tmp = []
        try:
            ue=self.Users[userId]
            tmp.extend(ue.APss.keys()) # append all APs visible by mecUser
        except:
            # userId not found
            pass
        return tmp
    
    def addAP(self,
              apId="ap000",
              latitude=0.000,
              longitude=0.000,
              zone="zone0",
              maxUsers=10, 
              coverageSqKm=2.5):
        """
        Create a mecAP instance and add it to the list
        """
        errorCode=0
        try:
            # validate if exist
            self.APs[apId]
            errorCode=1
        except:
            self.APs[apId]=mecAP(apId,latitude,longitude,zone,maxUsers,coverageSqKm) 
        return errorCode

    def removeAP(self,apId="ap000"):
        try:
            del self.APs[apId]
            for ue in self.Users.keys():
                ue.removeAP(apId)
        except KeyError:
            pass

    def addUser(self,
                userId="ue000",
                latitude=0.00,
                longitude=0.00,
                bandwidthMbps=10.5,
                serviceQuality=1):
        """
        Create a mecUser instance and add it to the list
        """
        errorCode = 0
        errorMsg=""
        try:
            # validate if exist
            self.Users[userId]
            errorCode = 1
            errorMsg="Error: User ID already exist"
        except:
            self.Users[userId] = mecUser(userId,latitude,longitude,bandwidthMbps,serviceQuality)
            errorMsg="User successfully created"
  
        return errorCode,errorMsg

    def removeUser(self,userId):
        try:
            del self.Users[userId]
            for ap in self.APs.keys():
                ap.removeUser(userId)
        except KeyError:
            pass

    def getAll(self):
        return vars(self)

    def getAllAPs(self):
        """
        return disctionary with all variables of the class
        """
        tmp={}
        for ap in self.APs.keys():
            tmp[ap]=self.APs[ap]
        return tmp

    def getAllUsers(self):
        """
        return disctionary with all variables of the class
        """
        tmp={}
        for ue in self.Users.keys():
            tmp[ue]=self.Users[ue]
        return tmp

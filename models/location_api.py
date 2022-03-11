#
# Location API Models
#
from marshmallow import Schema, fields

class MecTimeStamp(Schema):
    nanoSeconds = fields.Integer(required=True)
    seconds = fields.Integer(required=True)


class MecLocationDistance(Schema):
    # /queries/distance
    requester = fields.String(description="Entity that is requesting the information")
    address = fields.List(fields.URL(description="address of users (eg. sip URI)", required=True))
    latitude = fields.Float(description="Latitude geo position")
    longitude = fields.Float(description="Longitude geo position")


class MecLocationTerminalDistance(Schema):
    """
    A type containing information about the distance from a terminal to a location
    or between two terminals, in addition the accuracy and a timestamp of the
    information are provided.
    """
    # accuracy of provided distance
    accuracy = fields.Float(
        description="Accuracy of the provided distance in meters")
    distance = fields.Float(required=True) # distance in meters
    timestamp = fields.Nested(MecTimeStamp)


class MecLocationProblemDetails(Schema):
    detail   = fields.String()
    instance = fields.URL()
    status   = fields.Int()
    title    = fields.String()
    type     = fields.URL()


class MecLocationVelocity(Schema):
    bearing = fields.Float(description="Bearing, expressed in the range 0 to 360 degree", required=True)
    horizontalSpeed = fields.Float(description="Horizontal speed, expressed in km/h", required=True)
    # only if velocityType = 3 or 4
    uncertainty = fields.Float(description="Present only if 'velocityType' equals 3 or 4")
    velocityTypeDescription="""
    1 = HORIZONTAL
    2 = HORIZONTAL_VERTICAL
    3 = HORIZONTAL_UNCERT
    4 = HORIZONTAL_VERTICAL_UNCERT
    """
    velocityType = fields.Integer(description=velocityTypeDescription, required=True)
    verticalSpeed = fields.Float(
        description="Vertical speed, expressed in km/h. Present only if 'velocityType' equals 2 or 4")
    verticalUncertainty = fields.Float(description="Vertical uncertainty. Present if 'velocityType' equals 4")


class MecLocationInfo(Schema):
    accuracy          = fields.Float(description="Horizontal accuracy")
    accuracyAltitude  = fields.Float(description="Altitude accuracy")
    accuracySemiMinor = fields.Float(description="Horizontal accuracy semi-major")
    altitude          = fields.Float(description="Location altitude relative to the WGS84 ellipsoid surface")
    confidence        = fields.Float(description="Percentage by which the position of a target entity is known (only shapes 1,4 or 6)")
    includedAngle     = fields.Float(description="for shape = 6")
    innerRadius       = fields.Float(description="for shape = 6")
    latitude          = fields.Float(description="-90 to 90 degrees. Only > 1 if shape = 7", required=True)
    longitude         = fields.Float(description="longitued -180 to 180. Only > 1 if shape = 7", required=True)
    shapeDescription="""
    1 = ELLIPSOID_ARC
    2 = ELLIPSOID_POINT
    3 = ELLIPSOID_POINT_ALTITUDE
    4 = ELLIPSOID_POINT_ALTITUDE_UNCERT_ELLIPSOID
    5 = ELLIPSOID_POINT_UNCERT_CIRCLE
    6 = ELLIPSOID_POINT_UNCERT_ELLIPSE
    7 = POLYGON
    """
    shape             = fields.Integer(description=shapeDescription, required=True) 
    timestamp         = fields.Nested(MecTimeStamp)
    uncertaintyRadius = fields.Float(description="Present only if 'shape' equals 6")
    velocity = fields.Nested(MecLocationVelocity) # Target entity’s velocity


class MecLocationUsers(Schema):
    zoneId = fields.List(fields.String())
    accessPointId = fields.String()
    address = fields.URL()


class MecLocationUserInfo(Schema):
    accessPointId = fields.String()
    address = fields.URL(required=True)
    ancillaryInfo = fields.String()
    contextLocationInfo = fields.String()
    locationInfo = fields.Nested(MecLocationInfo)
    resourceURL = fields.URL(required=True)
    timestamp = fields.Nested(MecTimeStamp, required=True)
    zoneId = fields.String(description="Identifier of zone", required=True)


class MecLocationUserList(Schema):
    resourceURL = fields.URL(required=True)
    user = fields.List(fields.Nested(MecLocationUserInfo))


class MecLocationZone(Schema):
    pass


class MecLocationZoneInfo(Schema):
    """
    A class containing zone information
    """
    numberOfAccessPoints = fields.Integer(description="The number of access points within the zone", required=True)
    numberOfUnserviceableAccessPoints = fields.Integer(description="Number of inoperable access points within the zone", required=True)
    numberOfUsers = fields.Integer(
        description="The number of users currently on the access point", required=True)
    resourceURL = fields.URL(description="Self referring URL", required=True)
    zoneId = fields.String(description="Identifier of zone", required=True)


class MecLocationZoneList(Schema):
    """
    A class containing a list of zones
    """
    resourceURL = fields.URL(description="Self referring URL", required=True)
    zone = fields.List(fields.Nested(MecLocationZoneInfo))

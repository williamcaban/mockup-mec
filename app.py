#!/usr/bin/python3

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields
from flask import Flask, jsonify, make_response, redirect, url_for, render_template, send_from_directory
import time

# Import MEC Models definitions
from models.location_api import *

# Create an APISpec
spec = APISpec(
    title="Mockup MEC",
    version="1.0.0",
    openapi_version="3.0.1",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ]
)

app = Flask(__name__, template_folder="./resources/templates", static_folder="./resources/static")

@app.route("/")
def mainIndex():
    return "Mockup MEC API"


@app.route("/api/swagger.json")
def swaggerSpec():
    return jsonify(spec.to_dict())


@app.route("/api/swagger")
@app.route("/api/swagger/<path:path>")
def swaggerDocs(path=None):
    if not path or path == "index.html":
        return render_template("index.html", base_url="/api/swagger")
    else:
        return send_from_directory("./resources/static", path)


def getMecTimeStamp():
    t_sec, t_ns = str(time.time()).split(".")
    return {"nanoSeconds":int(t_ns),"seconds":int(t_sec)}


@app.route("/queries/distance")
def queriesDistance():
    """
    ---
    get:
      tags:
      - 'MEC Location API'
      summary: 'UE Distance Lookup of a specific UE'
      description: 'UE Distance Lookup between terminals or a terminal and a location'
      operationId: distanceGET
      parameters:
        - in: query
          schema: MecLocationDistance
      responses:
        200:
          description: 'Successful response to a distance request'
          content:
            application/json:
              schema: MecLocationTerminalDistance
    """
    # dummy_data = {
    #     "requester" : "dummg",
    #     "address" : "url://localhost",
    #     "latitude" : 1.234,
    #     "longitude" : 1.234,
    #     "status" : 200
    # }
    dummy_data = {
        "accuracy": 1,
        "distance": 3,
        "timestamp": getMecTimeStamp()
    }
    return MecLocationTerminalDistance().dump(dummy_data)


@app.route("/queries/users")
def queriesUsers():
    """
    ---
    get:
      tags:
      - 'MEC Location API'
      summary: 'UE Location Lookup of a specific UE or group of UEs'
      description: 'UE Location Lookup of a specific UE or group of UEs'
      parameters:
        - in: query
          schema: MecLocationUsers
      responses:
        '200':
          description: 'Successful response to users request'
          content:
            application/json:
              schema: MecLocationUserList     
    """
    dummy_data = {
        "resourceURL":"uri://localhost/queries/users?...",
        "user":[{
            "accessPointId":"ap1234",
            "address":"mec://localhost/mec/ue/1234",
            "resourceURL": "mec://localhost/mec/ue/1234",
            "timestamp": getMecTimeStamp(),
            "zoneId":"zone240",
            "contextLocationInfo": "mobile device",
            "locationInfo": {
                "accuracy":1,
                "shape":1,
                "latitude": 1.234,
                "longitude": 2.3134,
                "timestamp": getMecTimeStamp(),
            }

        }]
    }
    return MecLocationUserList().dump(dummy_data)


@app.route("/queries/zones")
def queriesZones():
    """
    ---
    get:
      tags:
      - 'MEC Location API'
      summary: 'Zones information Lookup'
      description: 'Used to get a list of identifiers for zones authorized for use by the application.'
      responses:
        '200':
          description: 'Successful response to zones request'
          content:
            application/json:
              schema: MecLocationZoneList
    """
    dummy_data={
        "resourceURL":"uri://localhost/...",
        "zone":[
            {
                "numberOfAccessPoints": 5,
                "numberOfUnserviceableAccessPoints": 1,
                "numberOfUsers": 779,
                "resourceURL":"uri://localhost/mec/zone/35",
                "zoneId":"zone35"
            }
        ]

    }
    return MecLocationZoneList().dump(dummy_data)






# Define schemas
spec.components.schema("MecTimeStamp",
                       schema=MecTimeStamp)
spec.components.schema("MecLocationDistance",
                        schema=MecLocationDistance)
spec.components.schema("MecLocationTerminalDistance",
                       schema=MecLocationTerminalDistance)
spec.components.schema("MecLocationProblemDetails",
                       schema=MecLocationProblemDetails)
spec.components.schema("MecLocationVelocity", schema=MecLocationVelocity)
spec.components.schema("MecLocationInfo", schema=MecLocationInfo)
spec.components.schema("MecLocationUsers", schema=MecLocationUsers)
spec.components.schema("MecLocationUserInfo", schema=MecLocationUserInfo)
spec.components.schema("MecLocationUserList", schema=MecLocationUserList)
spec.components.schema("MecLocationZone", schema=MecLocationZone)
spec.components.schema("MecLocationZoneList", schema=MecLocationZoneList)
# spec.components.schema("MecLocationZoneInfo", schema=MecLocationZoneInfo)


with app.test_request_context():
    spec.path(view=queriesDistance)
    spec.path(view=queriesUsers)
    spec.path(view=queriesZones)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
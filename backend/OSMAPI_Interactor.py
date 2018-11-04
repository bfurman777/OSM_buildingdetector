# based on https://pypi.org/project/osmapi/ and http://osmapi.metaodi.ch/#header-classes
import osmapi

# I made an account for us to all use
api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org", username="OSM_buildingdetector", password="fakepassword123")

# add meaningful comments pls :)
# Code works instantaneously in random areas but in residential/populated areas I'm not sure what's going on
api.ChangesetCreate({u"comment": u"Testing Way Create Non-Residential"})

# make Nodes based on longitude and latitude
Node1 = api.NodeCreate({"lon": 1, "lat": 1, "tag": {"Corner": "1"}})
Node2 = api.NodeCreate({"lon": 1, "lat": 1.01, "tag": {"Corner": "2"}})
Node3 = api.NodeCreate({"lon": 1.01, "lat": 1.01, "tag": {"Corner": "3"}})
Node4 = api.NodeCreate({"lon": 1.01, "lat": 1, "tag": {"Corner": "4"}})

node_list = [Node1["id"], Node2["id"], Node3["id"], Node4["id"]]

# if you want to see the id's of the Nodes you made uncomment this part
# for node in node_list:
#     print(node)

# create the way using the nodes
way = api.WayCreate({"nd": node_list, "tag": {}})

# see data on the way you just made
print(api.WayGet(str(way["id"])))

# to close the set of changes
# also exists a flush command to force upload to OSM server; not sure if it's necessary or how it differs
# from api.ChangesetClose()
api.ChangesetClose()
# api.flush()

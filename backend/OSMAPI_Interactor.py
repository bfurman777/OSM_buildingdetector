# based on https://pypi.org/project/osmapi/ and http://osmapi.metaodi.ch/#header-classes
# not a built-in library in PyCharm
import osmapi

# I made an account for us to all use
api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org", username="OSM_buildingdetector", password="fakepassword123")

# add meaningful comments pls :)
api.ChangesetCreate({u"comment": u"Testing Way Create on Building"})

# make Nodes based on longitude and latitude
# add relevant tags
Node1 = api.NodeCreate({"lat": 41.788348, "lon": -88.129079, "tag": {"Corner": "1"}})
Node2 = api.NodeCreate({"lat": 41.788453, "lon": -88.129079, "tag": {"Corner": "2"}})
Node3 = api.NodeCreate({"lat": 41.788445, "lon": -88.129262, "tag": {"Corner": "3"}})
Node4 = api.NodeCreate({"lat": 41.788338, "lon": -88.129211, "tag": {"Corner": "4"}})

# need the id of the Node specifically
node_list = [Node1["id"], Node2["id"], Node3["id"], Node4["id"]]

# if you want to see the id's of the Nodes you made uncomment this part
# for node in node_list:
#     print(node)

# create the way (area) using the nodes
# add relevant tag
way = api.WayCreate({"nd": node_list, "tag": {}})

# see data on the way you just made
print(api.WayGet(str(way["id"])))

# to close the set of changes
api.ChangesetClose()

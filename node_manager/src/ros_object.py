class ROSObject:

  def __init__(self, world, json):
    self.world = world
    self.properties = json
    self.nodes = []  


  def update_properties(self):
    for node in self.nodes:
      node.set_param('properties', self.properties)
    


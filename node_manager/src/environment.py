from node import Node

class Environment:

  def __init__(self, world):

    self.world = world
    self.namespace = '%s/%s' % (world.id, 'env')
    self.node = Node(obj=self, name='env', node_type='env')
    self.node.set_param('world_id', self.world.id)
    

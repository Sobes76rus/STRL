from node import Node
from config import config
from node_manager import srv


class RNode(Node):

  def __init__(self, **args):
    Node.__init__(self, **args)

    self.tick_count = config['robots']['rate']['r']
    self.tick = 0


  def run(self):
    world = self.obj.world
    if self.tick * world.tick_count >= world.tick * self.tick_count: return

    self.tick += 1
    print world.tick, world.time, self.tick, self.tick_count

    env = world.env.node
    reac = self.get_srv('get_data', srv.RNode)()
    prop = env.get_srv('execute', srv.EnvExecute)(reac.reaction, self.obj.properties['name'])
    print prop

    if self.tick == self.tick_count: self.tick = 0

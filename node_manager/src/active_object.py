from ros_object import ROSObject
from os.path import join, isfile
from config import config
import converter
from node import Node
from r_node import RNode


class ActiveObject(ROSObject):

  def __init__(self, world, json):
    ROSObject.__init__(self, world=world, json=json)
    self.__robot = ActiveObject.by_name(json['name'])
    self.namespace = '%s/%s' % (world.id, json['name'])

    for node_name in config['robots']['launch']:
      robo_path = join(config['root'], config['robots']['root'])
      src_path = join(robo_path, self.__robot.get('src'))

      file_name = node_name + '.py'
      file_path = join(self.__robot.get('src'), file_name)

      klass = Node
      if node_name == 'r': klass = RNode

      if isfile(join(src_path, file_name)):
        node = klass(obj=self, name=node_name, node_type='runner')
        node.set_param('module', file_path)
        self.nodes.append(node)

    self.update_properties()


  @staticmethod
  def by_name(name):
    xml = converter.load(join(config['root'], 
      config['robots']['root'], config['robots']['config']))
    for robot in xml['robot']:
      if robot.get('name') == name: return robot

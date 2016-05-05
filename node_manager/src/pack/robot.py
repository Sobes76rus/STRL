import converter
from config import config
from os.path import *
from node import Node


class Robot:

  def __init__(self, world, ident, json):
    name = json['name']
    robot = Robot.by_name(name)

    self.__world = world
    self.__ident = ident
    self.__robot = robot
    self.__nodes = []

    for file_name in config['robots']['launch']:
      self.add_node(file_name)
      file_path = join(robot.get('src'), file_name+'.py')


  def add_node(self, node_name):
    robo_path = join(config['root'], config['robots']['root'])
    src_path = join(robo_path, self.__robot.get('src'))

    file_name = node_name + '.py'
    file_path = join(self.__robot.get('src'), file_name)

    if isfile(join(src_path, file_name)):
      self.__nodes.append(
        Node(
          robot=self, rate=config['robots']['rate'][node_name], name=node_name, 
          namespace='%s/%s'%(self.__world.get_id(), self.__ident), 
          params=[('module', file_path)]
        )
      )


  @staticmethod
  def by_name(name):
    xml = converter.loadObjectFromFile(join(config['root'],
      config['robots']['root'], config['robots']['config']))
    for robot in xml['robot']: 
      if robot.get('name') == name: return robot


  def get_nodes(self): return self.__nodes
  def get_maxrate(self): 
    rate = 0
    for node in self.__nodes:
      rate = max(rate, node.get_maxrate())
    return rate


  def interview(self, rate):
    for node in self.__nodes:
      node.interview(rate)

from roslaunch.scriptapi import ROSLaunch
from robot import Robot
from env_node import EnvNode


class World:

  def __init__(self, ident, json):

    self.__ident = ident
    self.__robots = []
    self.__launch = ROSLaunch()

    for robot in json['robot']: self.add_robot(robot)
    self.__env_node = EnvNode(name='env', namespace=ident)

    self.__maxrate = self.get_maxrate()
    self.__rate = 0
    self.__tick = 0

    self.start()

  
  def start(self): 
    self.__launch.start()
    self.__launch.launch(self.__env_node)
    for robot in self.__robots: 
      for node in robot.get_nodes():
        self.__launch.launch(node)

  def stop(self): self.__launch.stop()


  def add_robot(self, json): self.__robots.append(Robot(world=self, ident=len(self.__robots), json=json))


  def get_id(self): return self.__ident
  def get_tick(self): return self.__tick
  def get_maxrate(self): 
    rate = 0
    for robot in self.__robots:
      rate = max(rate, robot.get_maxrate())
    return rate


  def interview(self): 
    self.__rate += 1
    rate = 1.0 * self.__rate / self.__maxrate

    for robot in self.__robots: 
      robot.interview(rate)

    if self.__rate == self.__maxrate:
      self.__rate = 0
      self.__tick += 1

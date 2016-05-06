from roslaunch.scriptapi import ROSLaunch
from threading import Thread
from ros_object import ROSObject
from active_object import ActiveObject
from environment import Environment
import bridge, time


class World:

  def __init__(self, ID):
    json = bridge.request_world(ID)

    self.__destroy = False
    self.__launch = ROSLaunch()
    self.objects = []

    self.tick_count = 0
    self.tick = 0
    self.time = 0

    self.__init_by_json(json)
    self.__start()

    thread = Thread(target=self.loop)
    thread.start()


  def __init_by_json(self, json):
    self.id = json['id']
    for obj in json['objects']:
      self.__init_object(obj)

    self.env = Environment(world=self)


  def __init_object(self, json):
    if json['active']: 
      obj = ActiveObject(json=json, world=self)
      for n in obj.nodes: self.tick_count = max(self.tick_count, n.tick_count)
      self.objects.append(obj)
    else:
      self.objects.append(NodeObject(json=json, world=self))
    

  def __start(self):
    self.__launch.start()
    for obj in self.objects:
      for node in obj.nodes:
        self.__launch.launch(node)
    self.__launch.launch(self.env.node)

  def __stop(self): self.__launch.stop()


  def run(self):
    self.tick += 1

    for obj in self.objects:
      if obj.properties['active']:
        for node in obj.nodes: node.run()

    if self.tick == self.tick_count:
      self.tick = 0
      self.time += 1

    time.sleep(0.1)


  def loop(self):
    while not self.__destroy: self.run()
    self.__stop()


  def destroy(self): self.__destroy = True

import roslaunch.core
from config import config
import rospy, math
from node_manager.srv import *


class Node(roslaunch.core.Node):

  def __init__(self, robot, rate, 
      name, namespace, args=None, params=None):

    roslaunch.core.Node.__init__(self, 
        package=config['robots']['root'], 
        node_type=config['robots']['runner'],
        name=name, namespace=namespace, args=args)

    self.__robot = robot
    self.__maxrate = rate
    self.__rate = 0
    self.__x = 200

    params = params or []
    self.add_params(params)


  def add_param(self, key, val):
    self.args = self.args + ' _%s:=%s' % (key, val)

  def add_params(self, params):
    for (key, val) in params: self.add_param(key, val)

  
  def get_maxrate(self): return self.__maxrate

  
  def interview(self, rate):
    val = math.floor(self.__maxrate * rate + 1e-3)
    if val <= self.__rate: return
    self.__rate += 1

    print self.__rate, val, self.namespace, self.name 
    servicename = '%s%s'%(self.namespace, 'ready')
    rospy.wait_for_service(servicename)
    ready = rospy.ServiceProxy(servicename, Num)

    servicename = '/1/compute'
    rospy.wait_for_service(servicename)
    compute = rospy.ServiceProxy(servicename, Req)
    read = ready()
    res = compute(self.__x, read.Num)
    rospy.loginfo(res)
    self.__x = res.x
    

    if self.__rate == self.__maxrate:
      self.__rate = 0

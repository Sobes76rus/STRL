from config import config
import roslaunch.core
import rospy

class EnvNode(roslaunch.core.Node):

  def __init__(self, 
      name, namespace, args=None, params=None):

    roslaunch.core.Node.__init__(self,
        package=config['robots']['root'],
        node_type='env.py',
        name=name, namespace=namespace,
        args=args)

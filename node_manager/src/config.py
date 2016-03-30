config ={
  'config': {
    'name': 'NodeManager',
    'start': 'nodeManager_Start',
    'stop': 'nodeManager_Stop',
    'rate': 2
  },

  'root': 'src',
  'robots': {
    'root': 'robots',
    'config': 'config.xml',
    'launch': ['r', 's', 't'],
    'rate': {
      'r': 100,
      's': 25,
      't': 3
    }
  }
}



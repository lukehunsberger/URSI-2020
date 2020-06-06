# =====================================
#  FILE:    stn.py
#  AUTHOR:  ursi-2020
#  DATE:    june 2020
# =====================================
#  hi there

class STN:
    """
    ---------------------------
    Implement Simple Temporal Network.
    ---------------------------
    Attributes/Fields:
      n = number of time-points
      succs = list whose ith element is dictionary of successors of tp i
      tpToIndex = dictionary with key = name of time-point, value = index
      indexToTP = list whose ith element is the time-point name
    ---------------
    Methods:
      __init__
      addTP
      addEdgeIndices
      addEdgeNames
    """
  def __init__(self):
      """Initializes STN object"""
      self.n = 0
      self.succs = []
      self.tpToIndex = {}
      self.indexToTP = []

  def addTP(self,name):
      """ 
      ------------------------------------
        INPUTS:  self
                 name, a string
        OUTPUT:  none
        SIDE EFFECT:  Adds NAME as a time-point
      -------------------------------------
      """
      self.indexToTP.append(name)
      self.succs.append({})
      self.tpToIndex[name] = self.n
      self.n += 1
      
  def addEdgeIndices(self,x,delta,y):
      """ Inserts edge into STN """
      self.succs[x][y] = delta

  def addEdgeNames(self,x,delta,y):
      self.succs[self.tpToIndex[x]][self.tpToIndex[y]] = delta


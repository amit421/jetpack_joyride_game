from person import Player
from colorama import init,Fore
import numpy as np
import time

obj_list=[]

class Background:

  def __init__(self):
    self.__length=40
    self.__breadth=1000
    self.__matrix=[]
    self.__speed=0.09
    # self.__matrix=np.ndarray(shape=(self.__length,self.__breadth),dtype=int)
    # self.__matrix=[[" "]*self.__breadth]*self.__length

  def create_board(self):  
    for i in range(self.__length):
      self.new = []
      for j in range(self.__breadth):
        self.new.append(" ")
      self.__matrix.append(self.new)

  def sky_ground(self):  
    for i in range(self.__length):
      for j in range(self.__breadth):
        if i==5 or i==39:
          self.__matrix[i][j]= Fore.YELLOW+ 'x'+ '\x1b[0m'
        else:
          self.__matrix[i][j]=" "
    
  def listed(self,lis):
    global obj_list
    obj_list=lis

  def get_breadth_value(self):
    return self.__breadth

  def get_length_value(self):
    return self.__length

  def give_hor_obstacle(self,ycoo):
    global obj_list
    obj=0
    flag=0
    for i in obj_list:
      for j in range(i.get_size()):
        if i.get_ycoo()+j==ycoo:
          flag=1
          break
      if flag==1:
        obj=i
        break
    return obj

  def give_ver_obstacle(self,ycoo):
    global obj_list
    obj=0
    flag=0
    for i in obj_list:
      if i.get_ycoo()==ycoo:
        flag=1
      if flag==1:
        obj=i
        break
    return obj

  def give_ang_obstacle(self,ycoo):
    global obj_list
    obj=0
    flag=0
    for i in obj_list:
      for j in range(i.get_size()):
        if i.get_ycoo()+j==ycoo:
          flag=1
          break
      if flag==1:
        obj=i
        break
    return obj
  
  def inc_grid_speed(self,x):
    self.__speed+=x

  def dec_speed_val(self,x):
    self.__speed-=x

  def get_speed_value(self):
    return self.__speed

  def get_matrix_value(self,x,y):
    return self.__matrix[x][y]
  
  def set_matrix_value(self,x,y,z):
    self.__matrix[x][y]=z
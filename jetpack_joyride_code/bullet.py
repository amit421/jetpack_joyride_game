from colorama import init,Fore

class Bullet:
  def __init__(self,xcoo,ycoo,asc):
    self.__xcoo=xcoo
    self.__ycoo=ycoo
    self.__asc=asc

  def construct(self,grid):
    grid.set_matrix_value(self.__xcoo,self.__ycoo,self.__asc)

  def movebullet(self,grid,k):
    flag=0
    self.disappear(grid)
    
    for i in range(1,4,1):
      # if self.__ycoo<1497 and grid._matrix[self.__xcoo][self.__ycoo+i]==124:
      
      if self.__ycoo< k-3 and grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==Fore.LIGHTYELLOW_EX +'+'+ '\x1b[0m':
        flag=1
        break

      # elif grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==48:
      #   flag=1
      #   break
      # if self.__ycoo>grid.get_breadth_value()-1:
      #   flag=1
      #   break

      if self.__ycoo>=k:
        flag=1
        break

      elif self.__ycoo< k-3 and grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==Fore.BLACK + '|' + '\x1b[0m':
        ret=grid.give_hor_obstacle(self.__ycoo+i)
        ret.hor_erase(grid)
        flag=1
        break
      # elif self.__ycoo< 1497 and grid._matrix[self.__xcoo][self.__ycoo+i]==61:
      elif self.__ycoo< k-3 and grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==Fore.BLACK + '=' + '\x1b[0m':
        ret=grid.give_ver_obstacle(self.__ycoo+i)
        ret.ver_erase(grid)
        flag=1
        break
      # elif self.__ycoo< 1497 and grid._matrix[self.__xcoo][self.__ycoo+i]==47:
      elif self.__ycoo< k-3 and grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==Fore.BLACK + '/' + '\x1b[0m':
        ret=grid.give_ang_obstacle(self.__ycoo+i)
        ret.ang_erase(grid)
        flag=1
        break

      elif self.__ycoo< k-3 and grid.get_matrix_value(self.__xcoo,self.__ycoo+i)==Fore.LIGHTYELLOW_EX + '$' + '\x1b[0m':
        ret=grid.give_hor_obstacle(self.__ycoo+i)
        siz=ret.get_size()
        self.__ycoo+=siz
        flag=0
        break

      
    
    # if flag==0 and self.__ycoo< 1497 and self.__ycoo< k:
    if flag==0 and self.__ycoo< k-3:
      self.__ycoo+=3
      self.reappear(grid)

    else:
      return 7

  def disappear(self,grid):
    grid.set_matrix_value(self.__xcoo,self.__ycoo," ")

  def reappear(self,grid):
    grid.set_matrix_value(self.__xcoo,self.__ycoo,self.__asc)
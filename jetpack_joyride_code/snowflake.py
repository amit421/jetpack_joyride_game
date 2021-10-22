from colorama import init,Fore

class Snowflake:
  def __init__(self,xcoo,ycoo):
    self.__xcoo=xcoo
    self.__ycoo=ycoo
    self.__lis=[]

  def construct(self,grid):
    with open('boss/snowflake','r') as f:
      for line in f:
        self.__lis.append(line.strip('\n'))

    for i in range(3):
      for j in range(3):
        vol=Fore.LIGHTYELLOW_EX + self.__lis[i][j] + '\x1b[0m'
        grid.set_matrix_value(self.__xcoo+i,self.__ycoo+j,vol)

  def move(self,grid,c):
    flag=0
    self.disappear(grid)
    for k in range(1,4,1):
      for i in range(0,3,1):
        for j in range(0,3,1):
          if (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)==Fore.LIGHTMAGENTA_EX+'>'+'\x1b[0m') or (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)==" "):
            flag=0
            break

          if (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)=='O') or (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)=='\\') or (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)=='\\') or (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)=='|') or (self.__ycoo>=c and grid.get_matrix_value(self.__xcoo+i,(self.__ycoo+j)-k)=='/'):
            return 3
            

        # if self.__ycoo>c and grid._matrix[self.__xcoo+i][self.__ycoo-j]!=32:
        #   flag=1
        #   break

    if flag==0 and self.__ycoo>=c:
      self.__ycoo-=3
      self.reappear(grid)
    else:
      return 7



  def disappear(self,grid):
    for i in range(3):
      for j in range(3):
        grid.set_matrix_value(self.__xcoo+i,self.__ycoo+j," ")

  def reappear(self,grid):
    for i in range(3):
      for j in range(3):
        vol=Fore.LIGHTYELLOW_EX + self.__lis[i][j] + '\x1b[0m'
        grid.set_matrix_value(self.__xcoo+i,self.__ycoo+j,vol)
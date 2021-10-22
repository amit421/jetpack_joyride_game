
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from bullet import Bullet
from snowflake import Snowflake
from colorama import init, Fore
import signal
import time

bullet_obj=[]
snow_obj=[]

class Person:
  def __init__(self,xcoo,ycoo):
    self._xcoo=xcoo
    self._ycoo=ycoo
    self._lives=3


class Player(Person):
  def __init__(self,matrix,matrix2,xcoo,ycoo):
    super().__init__(xcoo,ycoo)
    self.__matrix=matrix
    self.__matrix2=matrix2
    self.__shield=0
    self.__obhit=0
    self.__score=0
    self.__shield_check=0
    self.__shield_of=1
    self.__enp=0
    self.__t_in=0
    self.__t_en=0
    self.__ini_val=1
    self.__real_val=1
    self.__creat_check=0


  def move(self,k,c,grid):
    global bullet_obj
    def alarmhandler(signum,frame):
      raise AlarmException
    def user_input(timeout=grid.get_speed_value()-0.01):
      signal.signal(signal.SIGALRM, alarmhandler)
      signal.setitimer(signal.ITIMER_REAL, timeout)
      
      try:
        text = getChar()()
        signal.alarm(0)
        return text
      except AlarmException:
        pass
      signal.signal(signal.SIGALRM, signal.SIG_IGN)
      return 's'

    char = user_input()

    if char == 'd' and self._ycoo<k:
      self.disappear_mando(grid)
      self._ycoo+=3
      if self._xcoo<36:
        self._xcoo+=self.__real_val
      if self._xcoo>36:
        self._xcoo=36
      self.reappear_mando(grid,1,c)

    elif char == 'a' and self._ycoo>c:
      self.disappear_mando(grid)
      self._ycoo-=3
      if self._xcoo<36:
        self._xcoo+=self.__real_val 
      if self._xcoo>36:
        self._xcoo=36  
      self.reappear_mando(grid,2,c)
      
    elif char == 'q':
      quit()

    elif char == 'w' and self._xcoo>7:
      self.disappear_mando(grid)
      self.__real_val=self.__ini_val
      self._xcoo-=3
      if self._xcoo<=7:
        self._xcoo=6
      self.reappear_mando(grid,3,c)

    elif char == 's':
      #  and self._xcoo<36-self.__real_val:
      self.disappear_mando(grid)
      self._xcoo+=self.__real_val
      self.__real_val+=1
      if self._xcoo>36:
        self._xcoo=36
      self.reappear_mando(grid,4,c)

    elif char == 'p' and self.__enp==0:
      self.__enp=1
      # grid.__speed-=0.05
      grid.dec_speed_val(0.05)
      self.disappear_mando(grid)
      if self._xcoo<36:
        self._xcoo+=self.__real_val
      if self._xcoo>36:
        self._xcoo=36
      self.reappear_mando(grid,8,c)
      return 7

    elif char == chr(32) and self.__shield_check==1:
      self.__shield=1
      self.disappear_mando(grid)
      self.reappear_mando(grid,6,c)
      self.__shield_check=0
      self.__t_in=int(time.time())
      return char
    
    elif char == 'b' :
      b1=Bullet(self._xcoo+1,self._ycoo+3,Fore.LIGHTMAGENTA_EX + '>' + '\x1b[0m')
      bullet_obj.append(b1)
      b1.construct(grid)
      self.disappear_mando(grid)
      if self._xcoo<36:
        self._xcoo+=self.__real_val
      if self._xcoo>36:
        self._xcoo=36
      self.reappear_mando(grid,8,c) 

    # else:
    #   self.disappear_mando(grid)
    #   if self._xcoo<36:
    #     self._xcoo+=1
    #   self.reappear_mando(grid,8,c)




  def construct(self,grid):
    for i in range(self._xcoo, self._xcoo+3):
      for j in range(self._ycoo, self._ycoo+3):
        # grid.__matrix[i][j]=self.__matrix[i-self._xcoo][j-self._ycoo]
        val=self.__matrix[i-self._xcoo][j-self._ycoo]
        grid.set_matrix_value(i,j,val)

  def disappear_mando(self, grid):
    for i in range(self._xcoo, self._xcoo+3):
      for j in range(self._ycoo, self._ycoo+3):
        # grid.__matrix[i][j] = 32
        grid.set_matrix_value(i,j," ")
    

  def reappear_mando(self, grid, code, c):
    count=0
    for i in range(self._xcoo, self._xcoo+3):
      for j in range(self._ycoo, self._ycoo+3):
        if grid.get_matrix_value(i,j)== Fore.BLACK +'|' + '\x1b[0m' or grid.get_matrix_value(i,j)==Fore.BLACK +'='+ '\x1b[0m' or grid.get_matrix_value(i,j)==Fore.BLACK +'/'+ '\x1b[0m':
          # or grid.get_matrix_value(i,j)==Fore.LIGHTYELLOW_EX +'+'+ '\x1b[0m'
          count+=1
        if grid.get_matrix_value(i,j)==Fore.LIGHTYELLOW_EX +'$'+ '\x1b[0m':
          self.__score+=1


    if count==0 or self.__shield==1:

      # i can also add going through the beam capability without breaking the beam just by making different cases for each of the inputs by increasing the count directly by +3 in that direction
      if count==0 and code==9:
        for i in range(self._xcoo, self._xcoo+3):
          for j in range(self._ycoo, self._ycoo+3):

            # grid.__matrix[i][j]=self.__matrix[i-self._xcoo][j-self._ycoo]
            vol=self.__matrix[i-self._xcoo][j-self._ycoo]
            grid.set_matrix_value(i,j,vol)
      
      if count==0 and code==9 and self.__shield==1:
        for i in range(self._xcoo, self._xcoo+3):
          for j in range(self._ycoo, self._ycoo+3):
            vol=self.__matrix2[i-self._xcoo][j-self._ycoo]
            grid.set_matrix_value(i,j,vol)

      if self.__shield==1: 
        for i in range(self._xcoo, self._xcoo+3):
          for j in range(self._ycoo, self._ycoo+3):
            vol=self.__matrix2[i-self._xcoo][j-self._ycoo]
            grid.set_matrix_value(i,j,vol)
      else:    
        for i in range(self._xcoo, self._xcoo+3):
          for j in range(self._ycoo, self._ycoo+3):
            vol=self.__matrix[i-self._xcoo][j-self._ycoo]
            grid.set_matrix_value(i,j,vol)

    elif count>0 and code == 1 and self.__shield==0:
      self.__shield=1
      self.__t_in=int(time.time())
      self.__obhit=1
      self._lives-=1
      # self._ycoo-=2
      # if self._xcoo <= 36:
      #   self._xcoo-=1
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)

    elif count>0 and code ==2 and self.__shield==0:
      self.__obhit=1
      self.__shield=1
      self.__t_in=int(time.time())
      self._lives-=1
      # self._ycoo+=3
      # if self._xcoo<=36:
      #   self._xcoo-=1
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)

    elif count>0 and code==3 and self.__shield==0:
      self.__obhit=1
      self.__shield=1
      self.__t_in=int(time.time())
      self._lives-=1
      # self._xcoo+=2
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)

    elif count>0 and code==4 and self.__shield==0:
      self.__obhit=1
      self.__shield=1
      self.__t_in=int(time.time())
      self._lives-=1
      # self._xcoo-=1
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)

    elif count>0 and code==5 and self.__shield==0:
      self.__obhit=1
      self.__shield=1
      self.__t_in=int(time.time())
      self._lives-=1
      # self._ycoo-=1
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)

  def shot(self,grid,k):
    global bullet_obj
    for o in bullet_obj:
      check=o.movebullet(grid,k)
      if check==7:
        bullet_obj.remove(o)

  def get_real_val(self):
    return self.__real_val

  def set_enp_value(self,x):
    self.__enp=0

  def get_enp_value(self):
    return self.__enp

  def get_shield_value(self):
    return self.__shield
  
  def get_obhit_value(self):
    return self.__obhit

  def get_shield_of_value(self):
    return self.__shield_of

  def set_shield_of_value(self,x):
    self.__shield_of=x

  def get_t_in_value(self):
    return self.__t_in
  
  def set_t_en_value(self,x):
    self.__t_en=x

  def get_creat_check_val(self):
    return self.__creat_check
  
  def set_creat_check_value(self,x):
    self.__creat_check=x

  def set_shield_check_value(self,x):
    self.__shield_check=x
  
  def get_t_en_value(self):
    return self.__t_en

  def set_shield_value(self,x):
    self.__shield=x

  def set_obhit_value(self,x):
    self.__obhit=x

  def get_lives_value(self):
    return self._lives

  def get_score_value(self):
    return self.__score

  def inc_ycoo_val(self,x):
    self._ycoo+=x

  def dec_ycoo_val(self,x):
    self._ycoo-=x

  def dec_xcoo_val(self,x):
    self._xcoo-=x
  
  def inc_xcoo_val(self,x):
    self._xcoo+=x

  def deduct_lives(self,k,c,grid):
    if self.__shield==1:
      pass
    elif self.__shield==0:
      self._lives-=1
      self._ycoo=c+2
      self._xcoo=36
      for i in range(self._xcoo, self._xcoo+3):
        for j in range(self._ycoo, self._ycoo+3):
          vol=self.__matrix[i-self._xcoo][j-self._ycoo]
          grid.set_matrix_value(i,j,vol)


class Enemy(Person):
  def __init__(self,xcoo,ycoo):
    super().__init__(xcoo,ycoo)
    self.__lis=[]
    self._lives=3

  def construct_dragon(self,grid):
    with open('boss/boss', 'r') as f:
      for line in f:
        self.__lis.append(line.strip('\n'))
    
    for i in range(23):
      for j in range(52):
        # grid.__matrix[self._xcoo+i][self._ycoo+j]=ord(self.__lis[i][j])
        vol=Fore.RED + self.__lis[i][j] + '\x1b[0m'
        grid.set_matrix_value(self._xcoo+i,self._ycoo+j,vol)

  def move_dragon(self,grid,p1,c,k):
    global snow_obj

    if grid.get_matrix_value(self._xcoo+9,self._ycoo+13)==Fore.LIGHTMAGENTA_EX +'>'+ '\x1b[0m' or grid.get_matrix_value(self._xcoo+10,self._ycoo+12)==Fore.LIGHTMAGENTA_EX +'>'+ '\x1b[0m' or grid.get_matrix_value(self._xcoo+11,self._ycoo+9)==Fore.LIGHTMAGENTA_EX +'>'+ '\x1b[0m':
    # if grid.get_matrix_value(self._xcoo+9][self._ycoo+13]==62 or grid.__matrix[self._xcoo+10][self._ycoo+12]==62 or grid.__matrix[self._xcoo+11][self._ycoo+9]==62:
      self._lives-=1

    flag=0

    self.disappear_dragon(grid)

    for i in range(6,39,1):
      for j in range(c,k-52,1):
        if grid.get_matrix_value(i,j)=='O':
          # if i<self._xcoo+18 and self._xcoo-1>5:
          if i<self._xcoo+18 and (self._xcoo+18)-1>5:
            self._xcoo-=1
          elif i>self._xcoo+18 and (self._xcoo+18)+1<39:
            self._xcoo+=1
          elif i==self._xcoo+18:
            s1=Snowflake(self._xcoo+18,self._ycoo-8)
            snow_obj.append(s1)
            s1.construct(grid)
          flag=1
          break

      if flag==1:
        break

    self.reappear_dragon(grid)
      
    for o in snow_obj:
      ret=o.move(grid,c)
      if ret==7:
        snow_obj.remove(o)
      if ret==3:
        return 7
    # if self._xcoo+18==p1._xcoo:
    #   s1=Snowflake(self._xcoo+18,self._ycoo-8)
    #   snow_obj.append(s1)
    #   s1.construct(grid)

  def disappear_dragon(self,grid):
    # if self._xcoo+23<39:
    for i in range(23):
      for j in range(52):
        if self._xcoo+i>5 and self._xcoo+i<39:
          grid.set_matrix_value(self._xcoo+i,self._ycoo+j," ")  

  def reappear_dragon(self,grid):
    # if self._xcoo+23<39:
    for i in range(23):
      for j in range(52):
        if self._xcoo+i>5 and self._xcoo+i<39:
          vol=Fore.RED + self.__lis[i][j] + '\x1b[0m'
          grid.set_matrix_value(self._xcoo+i,self._ycoo+j,vol)

  def get_lives_value(self):
    return self._lives

  
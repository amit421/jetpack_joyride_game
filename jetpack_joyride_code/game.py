from background import Background
from obstacle import hor_obstacle
from obstacle import ver_obstacle
from obstacle import ang_obstacle
from obstacle import coins
from obstacle import magnet
from person import Player
from person import Enemy
from bullet import Bullet


from colorama import Fore
# init(autoreset=True)

import random
import time
import pyfiglet
  
# import time
# import sys
# import os

# def countd():

#   seconds = 59
#   minutes = 4
#   five_minutes = 0

#   os.system('clear')
#   os.system('setterm -cursor off')

#   while five_minutes != 300:
#     sys.stdout.write("\r%d:%02.f\t" % (minutes, seconds))
#     sys.stdout.flush()
#     seconds -= 1
#     if seconds == -1:
#       minutes -= 1
#       seconds = 59

#     five_minutes += 1
#     time.sleep(1)

# countd()

# os.system('setterm -cursor on')


obj_list=[]
# import os

# l, b = os.popen('stty size', 'r').read().split()
# # import readchar

# length=int(l)
# bb=int(b)
# breadth=bb-1
grid=Background()
grid.create_board()
grid.sky_ground()

# print(length)
# print(breadth)

# for i in range(grid.length):
#   for j in range(120):
#     print(chr(grid.matrix[i][j]),end="")
#   print()

h1=hor_obstacle(random.randint(6,20),random.randint(7,38),random.randint(7,20))
h2=hor_obstacle(random.randint(68,80),random.randint(7,38),random.randint(7,10))
h3=hor_obstacle(random.randint(157,170),random.randint(7,38),random.randint(8,20))
h4=hor_obstacle(random.randint(396,410),random.randint(7,38),random.randint(8,10))
h5=hor_obstacle(random.randint(536,550),random.randint(7,38),random.randint(7,10))
h6=hor_obstacle(random.randint(736,750),random.randint(7,38),random.randint(7,10))
h7=hor_obstacle(random.randint(795,810),random.randint(7,38),random.randint(5,20))

v1=ver_obstacle(random.randint(28,40),random.randint(7,18),random.randint(7,20))
v2=ver_obstacle(random.randint(136,150),random.randint(7,28),random.randint(8,10))
v3=ver_obstacle(random.randint(236,250),random.randint(7,18),random.randint(7,20))
v4=ver_obstacle(random.randint(556,570),random.randint(7,28),random.randint(8,10))
v5=ver_obstacle(random.randint(637,650),random.randint(7,18),random.randint(7,20))
v6=ver_obstacle(random.randint(716,730),random.randint(7,18),random.randint(8,20))
v7=ver_obstacle(random.randint(756,770),random.randint(7,28),random.randint(7,10))

a1=ang_obstacle(random.randint(87,110),random.randint(7,28),random.randint(8,10))
a2=ang_obstacle(random.randint(276,290),random.randint(7,18),random.randint(8,20))
a3=ang_obstacle(random.randint(297,310),random.randint(7,28),random.randint(7,10))
a4=ang_obstacle(random.randint(357,370),random.randint(7,28),random.randint(8,10))
a5=ang_obstacle(random.randint(456,470),random.randint(7,18),random.randint(13,20))
a6=ang_obstacle(random.randint(576,590),random.randint(7,28),random.randint(9,10))
a7=ang_obstacle(random.randint(777,790),random.randint(7,18),random.randint(8,20))

c1=coins(random.randint(47,60),random.randint(7,38),random.randint(8,10))
c2=coins(random.randint(177,190),random.randint(7,38),random.randint(4,10))
c3=coins(random.randint(216,230),random.randint(7,38),random.randint(6,20))
c4=coins(random.randint(317,330),random.randint(7,38),random.randint(4,10))
c5=coins(random.randint(376,390),random.randint(7,38),random.randint(8,20))
c6=coins(random.randint(416,430),random.randint(7,38),random.randint(4,20))
c7=coins(random.randint(476,490),random.randint(7,38),random.randint(3,10))
c8=coins(random.randint(497,510),random.randint(7,38),random.randint(7,10))
c9=coins(random.randint(596,610),random.randint(7,38),random.randint(4,10))
c10=coins(random.randint(656,670),random.randint(7,38),random.randint(4,20))
c11=coins(random.randint(676,690),random.randint(7,38),random.randint(10,10))
# c12=coins(random.randint(817,830),random.randint(7,38),random.randint(4,20))

m1=magnet(random.randint(117,130),random.randint(18,28),4)
m2=magnet(random.randint(196,210),random.randint(18,28),4)
m3=magnet(random.randint(256,270),random.randint(18,28),4)
m4=magnet(random.randint(337,350),random.randint(18,28),4)
m5=magnet(random.randint(436,450),random.randint(18,28),4)
m6=magnet(random.randint(515,530),random.randint(18,28),4)
m7=magnet(random.randint(617,630),random.randint(18,28),4)
m8=magnet(random.randint(696,710),random.randint(18,28),4)


obj_list.append(h1)
obj_list.append(h2)
obj_list.append(h3)
obj_list.append(h4)
obj_list.append(h5)
obj_list.append(h6)
obj_list.append(h7)
obj_list.append(v1)
obj_list.append(v2)
obj_list.append(v3)
obj_list.append(v4)
obj_list.append(v5)
obj_list.append(v6)
obj_list.append(v7)
obj_list.append(a1)
obj_list.append(a2)
obj_list.append(a3)
obj_list.append(a4)
obj_list.append(a5)
obj_list.append(a6)
obj_list.append(a7)
obj_list.append(c1)
obj_list.append(c2)
obj_list.append(c3)
obj_list.append(c4)
obj_list.append(c5)
obj_list.append(c6)
obj_list.append(c7)
obj_list.append(c8)
obj_list.append(c9)
obj_list.append(c10)
obj_list.append(c11)
# obj_list.append(c12)
obj_list.append(m1)
obj_list.append(m2)
obj_list.append(m3)
obj_list.append(m4)
obj_list.append(m5)
obj_list.append(m6)
obj_list.append(m7)
obj_list.append(m8)


grid.listed(obj_list)


# h_list=[]

# h_list.append(h1)
# h_list.append(h2)
# h_list.append(h3)
# h_list.append(h4)
# h_list.append(h5)
# h_list.append(h6)
# h_list.append(h7)

# v_list=[]

# v_list.append(v1)
# v_list.append(v2)
# v_list.append(v3)
# v_list.append(v4)
# v_list.append(v5)
# v_list.append(v6)
# v_list.append(v7)

# a_list=[]

# a_list.append(a1)
# a_list.append(a2)
# a_list.append(a3)
# a_list.append(a4)
# a_list.append(a5)
# a_list.append(a6)
# a_list.append(a7)

# c_obj=[]

# for i in range(15):
#   c_obj.append(Obstacle(random.randint(1,1300),random.randint(17,28),4))

# for o in c_obj:
#   o.magnet_construct(grid)


# list obj

# c_obj=[]

# for i in range(15):
#   c_obj.append(Obstacle(random.randint(1,1300),random.randint(7,38),random.randint(6,16)))

# for o in c_obj:
#   o.coins_construct(grid)

# h_obj=[]
# for i in range(15):
#   h_obj.append(Obstacle(random.randint(1,1300),random.randint(7,38),random.randint(6,15)))

# for o in h_obj:
#   o.hor_construct(grid)

# v_obj=[]
# for i in range(15):
#   if i%2==0:
#     v_obj.append(Obstacle(random.randint(1,1300),random.randint(7,28),random.randint(6,10)))
#   else:
#     v_obj.append(Obstacle(random.randint(1,1300),random.randint(7,18),random.randint(6,20)))

# for o in v_obj:
#   o.ver_construct(grid)

# a_obj=[]
# for i in range(15):
#   if i%2==0:
#     a_obj.append(Obstacle(random.randint(1,1300),random.randint(7,28),random.randint(6,10)))
#   else:
#     a_obj.append(Obstacle(random.randint(1,1300),random.randint(7,18),random.randint(6,20)))

# for o in a_obj:
#   o.ang_construct(grid)


h1.construct(grid)
h2.construct(grid)
h3.construct(grid)
h4.construct(grid)
h5.construct(grid)
h6.construct(grid)
h7.construct(grid)
v1.construct(grid)
v2.construct(grid)
v3.construct(grid)
v4.construct(grid)
v5.construct(grid)
v6.construct(grid)
v7.construct(grid)
a1.construct(grid)
a2.construct(grid)
a3.construct(grid)
a4.construct(grid)
a5.construct(grid)
a6.construct(grid)
a7.construct(grid)
c1.construct(grid)
c2.construct(grid)
c3.construct(grid)
c4.construct(grid)
c5.construct(grid)
c6.construct(grid)
c7.construct(grid)
c8.construct(grid)
c9.construct(grid)
c10.construct(grid)
c11.construct(grid)
# c12.construct(grid)
m1.construct(grid)
m2.construct(grid)
m3.construct(grid)
m4.construct(grid)
m5.construct(grid)
m6.construct(grid)
m7.construct(grid)
m8.construct(grid)


matrix=[[" ","O"," "],["[","|","\\"],["/"," ","\\"]]
matrix2=[["O","/","|"],["|","\\","|"],["/","\\","|"]]

p1=Player(matrix,matrix2,36,1)
Player.construct(p1,grid)

# dragon=Enemy(15,140)
dragon=Enemy(15,940)

dragon.construct_dragon(grid)

# cursor.hide()

k=183
do=0
print('\033c')
t0=int(time.time())
# p1.s_timer_in=int(time.time())
# p1.t_in=int(time.time())
while k < grid.get_breadth_value():
  print('\033[1;0H')
  if(p1.get_lives_value()==0):
    print('\033c')
    result = pyfiglet.figlet_format("GAME OVER                                            YOU LOSE !!")
    # pyfiglet.figlet_format("GAME OVER", font = "isometric1" ) 
    print(result)
    exit()

  # if(dragon._lives==0):
  if(dragon.get_lives_value()==0):
    print('\033c')
    result = pyfiglet.figlet_format("GAME OVER                                            YOU WON !!")
    # pyfiglet.figlet_format("GAME OVER", font = "isometric1" ) 
    print(result)
    exit()
  t1=int(time.time())-t0
  if(t1>200):
    print('\033c')
    result = pyfiglet.figlet_format("TIME UP                                              YOU LOST !!")
    # pyfiglet.figlet_format("GAME OVER", font = "isometric1" ) 
    print(result)
    exit()

# Fore.RED + "j" + '\x1b[0m'
  print(Fore.CYAN + "Player lives:- %d   Boss lives:- %d     Game Over in:- %3.d       "%(p1.get_lives_value(),dragon.get_lives_value(),201-t1) + '\x1b[0m' ,end=" ")

  # if p1._shield==1:
  if p1.get_shield_value()==1:
    vol=int(time.time())-p1.get_t_in_value()
    p1.set_t_en_value(vol)
    # if p1._obhit==0:
    if p1.get_obhit_value()==0:
      print(Fore.CYAN + "SHIELD :- ON     SCORE :- %3.d      %3.d - Time Remaining....... "%(p1.get_score_value(),int(11-p1.get_t_en_value())) + '\x1b[0m' ,end='\n')
    else:
      print(Fore.CYAN + "SHIELD :- ON     SCORE :- %3.d      %3.d - Time Remaining....... "%(p1.get_score_value(),int(6-p1.get_t_en_value())) + '\x1b[0m',end='\n')

  # elif p1._shield==0 and p1._shield_of==0:
  elif p1.get_shield_value()==0 and p1.get_shield_of_value()==0:
    val=int(time.time())-p1.get_t_in_value()
    p1.set_t_en_value(val)
    # if p1.creat_check==0:
    if p1.get_creat_check_val()==0:
      print(Fore.CYAN + "SHIELD :- OFF      SCORE :- %3.d     %3.d - Time to refill...... "%(p1.get_score_value(),int(66-p1.get_t_en_value())) + '\x1b[0m' ,end='\n')
    # elif p1.creat_check==1:
    elif p1.get_creat_check_val()==1:
      print(Fore.CYAN + "SHIELD :- OFF      SCORE :- %3.d     %3.d - Time to refill...... "%(p1.get_score_value(),int(71-p1.get_t_en_value())) + '\x1b[0m' ,end='\n')


  elif p1.get_shield_value()==0 and p1.get_shield_of_value()==1:
    # p1._shield_check=1
    p1.set_shield_check_value(1)
    print(Fore.CYAN + "SCORE :- %3.d  PRESS space to activate SHIELD..........."%(p1.get_score_value())+'\x1b[0m')

  
  if p1.get_t_en_value()>5 and p1.get_obhit_value()==1:
    # p1._shield=0
    # p1._obhit=0
    # p1._shield_of=0
    # p1.creat_check=0
    p1.set_shield_value(0)
    p1.set_obhit_value(0)
    p1.set_shield_of_value(0)
    p1.set_creat_check_value(0)
    

  
  if p1.get_t_en_value()>10 and p1.get_obhit_value()==0:
    # p1._shield=0
    # p1._shield_of=0
    # p1.creat_check=1
    p1.set_shield_value(0)
    p1.set_shield_of_value(0)
    p1.set_creat_check_value(1)
    

  if p1.get_t_en_value()>65 and p1.get_creat_check_val()==0:
    p1.set_shield_of_value(1)
    p1.set_creat_check_value(2)
    p1.set_t_en_value(0)

  # if p1.t_en>70 and p1.creat_check==1:
  if p1.get_t_en_value()>70 and p1.get_creat_check_val()==1:
    # p1._shield_check=1
    # p1._shield_of=1
    # p1.creat_check=2
    # p1.t_en=0
    p1.set_shield_of_value(1)
    p1.set_creat_check_value(2)
    p1.set_t_en_value(0)
    
  if p1.get_enp_value()==1:
    if do<150:
      do+=1
      # print("Booster Activated.....",end='')

    if do==150:
      grid.inc_grid_speed(0.05)
      # grid._speed+=0.05
      # can be reduced to 1 time by removing following two lines
      p1.set_enp_value(0)
      # p1._enp=0 
      do=0
      # do+=100


  i=1
  while i < grid.get_length_value():
    j=k-183
    while j < k:
      # if grid.get_matrix_value(i,j)==120:
      # print(Fore.YELLOW + chr(grid.get_matrix_value(i,j)) + '\x1b[0m',end='')
      # elif grid.get_matrix_value(i,j)==124:
      #   print(Fore.GREEN + chr(grid.get_matrix_value(i,j)) + '\x1b[0m',end='')
      # else:
      print(grid.get_matrix_value(i,j),end='')
      j+=1
    # print(" ",end="")
    # print()
    i+=1
  # print("\n")
  c=(k-183)
  tic=time.perf_counter()

  ti=p1.move(k-3,c,grid)

  toc=time.perf_counter()
  print("\n")
  # if c< 1499-183:
  if c< (grid.get_breadth_value()-1)-183:
    p1.disappear_mando(grid)
    # p1._ycoo+=1
    p1.inc_ycoo_val(1)
    # if p1._xcoo<36:
    #   p1._xcoo+=p1.get_real_val()
    # if p1._xcoo>36:
    #   p1._xcoo=36
    p1.reappear_mando(grid,5,c)
  
  p1.shot(grid,k)

  m1.capture(grid,p1,k,c)
  m2.capture(grid,p1,k,c)
  m3.capture(grid,p1,k,c)
  m4.capture(grid,p1,k,c)
  m5.capture(grid,p1,k,c)
  m6.capture(grid,p1,k,c)
  m7.capture(grid,p1,k,c)
  m8.capture(grid,p1,k,c)

  m1.construct(grid)
  m2.construct(grid)
  m3.construct(grid)
  m4.construct(grid)
  m5.construct(grid)
  m6.construct(grid)
  m7.construct(grid)
  m8.construct(grid)

  # i can use the following lines to give the effect that obstacles are not broken 

  # for o in h_list:
  #   o.hor_construct(grid)

  # for o in v_list:
  #   o.ver_construct(grid)

  # for o in a_list:
  #   o.ang_construct(grid)
  if c==(grid.get_breadth_value()-1)-183:
    ret=dragon.move_dragon(grid,p1,c,k)
    if ret==7:
      p1.deduct_lives(k,c,grid)

  if ti==7:
    time.sleep(0.09-(toc-tic))
  else:
    time.sleep(grid.get_speed_value()-(toc-tic))
  # if c< 1499-183:
  if c<(grid.get_breadth_value()-1)-183:
    k+=1
# i=1
#   while i < 40:
#     j=k-183
#     while j < k:
#       print(chr(grid._matrix[i][j]),end='')
#       j+=1
#     # print(" ",end="")
#     # print()
#     i+=1
#   # print("\n")
#   c=(k-183)
#   tic=time.perf_counter()

#   ti=p1.move(k-3,c,grid)

#   toc=time.perf_counter()
#   print("\n")
#   # if c< 1499-183:
#   if c< 1299-183:
#     p1.disappear_mando(grid)
#     p1._ycoo+=1
#     # if p1._xcoo<36:
#     #   p1._xcoo+=p1.get_real_val()
#     # if p1._xcoo>36:
#     #   p1._xcoo=36
#     p1.reappear_mando(grid,5,c)
  
#   p1.shot(grid,k)

#     m1.capture(grid,p1,k,c)

#     m1.construct(grid)

#   # i can use the following lines to give the effect that obstacles are not broken 

#   # for o in h_list:
#   #   o.hor_construct(grid)

#   # for o in v_list:
#   #   o.ver_construct(grid)

#   # for o in a_list:
#   #   o.ang_construct(grid)
#   if c==1499-183:
#     dragon.move_dragon(grid,p1,c,k)

#   if ti==7:
#     time.sleep(0.09-(toc-tic))
#   else:
#     time.sleep(grid._speed-(toc-tic))
#   # if c< 1499-183:
#   if c< 1499-183:
#     k+=1
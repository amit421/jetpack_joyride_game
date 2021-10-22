from colorama import init, Fore

class Obstacle:
  def __init__(self,y_coordinate,x_coordinate,size):
    self._size=size
    self._x_coordinate=x_coordinate
    self._y_coordinate=y_coordinate
    self._asc=" "

  def construct(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate,self._y_coordinate+j,self._asc)

  def hor_erase(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate,self._y_coordinate+j," ")

  def ver_erase(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate+j,self._y_coordinate," ")
  
  def ang_erase(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate+j,self._y_coordinate+j," ")
    
  def get_ycoo(self):
    return self._y_coordinate

  def get_size(self):
    return self._size


class hor_obstacle(Obstacle):
  def __init__(self,y_coordinate,x_coordinate,size):
    super().__init__(y_coordinate,x_coordinate,size)
    self._asc= Fore.BLACK + '|' + '\x1b[0m'

  def construct(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate,self._y_coordinate+j,self._asc)
    


class ver_obstacle(Obstacle):
  def __init__(self,y_coordinate,x_coordinate,size):
    super().__init__(y_coordinate,x_coordinate,size)
    self._asc= Fore.BLACK + '=' + '\x1b[0m'

  def construct(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate+j,self._y_coordinate,self._asc)



class ang_obstacle(Obstacle):
  def __init__(self,y_coordinate,x_coordinate,size):
    super().__init__(y_coordinate,x_coordinate,size)
    self._asc= Fore.BLACK + '/' + '\x1b[0m'
  
  def construct(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate+j,self._y_coordinate+j,self._asc)


class coins(Obstacle):
  def __init__(self,y_coordinate,x_coordinate,size):
    super().__init__(y_coordinate,x_coordinate,size)
    self._asc=Fore.LIGHTYELLOW_EX + '$' + '\x1b[0m'

  def construct(self,grid):
    for j in range(self._size):
      grid.set_matrix_value(self._x_coordinate,self._y_coordinate+j,self._asc)



class magnet(Obstacle):
  def __init__(self,y_coordinate,x_coordinate,size):
    super().__init__(y_coordinate,x_coordinate,size)
  
  def construct(self,grid):
    grid.set_matrix_value(self._x_coordinate,self._y_coordinate+0,Fore.RED + 'N' + '\x1b[0m')
    grid.set_matrix_value(self._x_coordinate,self._y_coordinate+1,Fore.WHITE +':' + '\x1b[0m')
    grid.set_matrix_value(self._x_coordinate,self._y_coordinate+2,Fore.WHITE + ':' + '\x1b[0m')
    grid.set_matrix_value(self._x_coordinate,self._y_coordinate+3,Fore.BLACK + 'S' + '\x1b[0m')


  def capture(self,grid,p1,k,c):
    for i in range(10):
      for j in range(10):
        if grid.get_matrix_value(self._x_coordinate+i,self._y_coordinate+j)=='O'  and self._y_coordinate>c+2 and self._y_coordinate<k:
          p1.disappear_mando(grid)

          # can be increased to increase the power of the magnet
          
          p1.dec_xcoo_val(2)
          p1.dec_ycoo_val(2)
          p1.reappear_mando(grid,9,c)

        if grid.get_matrix_value(self._x_coordinate-i,self._y_coordinate-j)=='O'  and self._y_coordinate>c+2 and self._y_coordinate<k:
          p1.disappear_mando(grid)
          p1.inc_xcoo_val(2)
          p1.inc_ycoo_val(2)
          p1.reappear_mando(grid,9,c)

        if grid.get_matrix_value(self._x_coordinate+i,self._y_coordinate-j)=='O'  and self._y_coordinate>c+2 and self._y_coordinate<k:
          p1.disappear_mando(grid)
          p1.dec_xcoo_val(2)
          p1.inc_ycoo_val(2)
          p1.reappear_mando(grid,9,c)

        if grid.get_matrix_value(self._x_coordinate-i,self._y_coordinate+j)=='O'  and self._y_coordinate>c+2 and self._y_coordinate<k:
          p1.disappear_mando(grid)
          p1.inc_xcoo_val(2)
          p1.dec_ycoo_val(2)
          p1.reappear_mando(grid,9,c)

  
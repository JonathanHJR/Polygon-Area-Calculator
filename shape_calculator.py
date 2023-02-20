class Rectangle:
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})" # string is inside quotations, actual python inside curly brackets
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self): 
    return self.width * self.height # try self.area = 
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self): 
    return (self.width ** 2 + self.height ** 2) ** .5
    
  def get_picture(self): 
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    string = (self.width * "*" + "\n") * self.height
    return string
    
  def get_amount_inside(self, shape): 
    return (self.width // shape.width) * (self.height // shape.height)  # better than int(self.get_area() / shape.get_area())

class Square(Rectangle): # Subclass will inherit all methods of class unless the method is overwritten

  def __init__(self, side): # eg 1
    self.width = side
    self.height = side

  def __str__(self): # eg 2
    return f"Square(side={self.width})"
  
  def set_side(self, side):
    self.width = side
    self.height = side
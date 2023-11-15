# from _typeshed import IdentityFunction


class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  

  def set_width(self, width):
    self.width = width
    return self.width

  def set_height(self, height):
    self.height = height
    return self.height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimerter = (2 * self.width) + (2 * self.height)
    return perimerter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for _ in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  def get_amount_inside(self, shape):
    sq = shape.width * shape.height
    rec = self.width * self.height
    return rec // sq
    
    
class Square(Rectangle):
  def __init__ (self, side):
    super().__init__(side, side)

  def __repr__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side
    return

  def set_width(self, side):
    return self.set_side(side)

  def set_height(self, side):
    return self.set_side(side)
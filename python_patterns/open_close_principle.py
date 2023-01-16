# open for extension, closed for modification
from Enum import enum

class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3

class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3
  
class Product:
  def __init__(self, name, color, size):
    self.name = name
    self.color = color
    self.size = size  

## example of bad class 'God' class
class ProductFilter:
  def FilterByColor(self, products, color):
    for p in products:
      if p.color == color: yield p
  
  def FilterBySize(self, products, size):
    for p in products:
      if p.size == size: yield p
  
  def FilterBySizeAndColor(self, products, size, color):
    for p in products:
      if p.color == color: yield p
    
## example of good class with usage of Specification

class Specification:
  def is_satisfied(self, item):
    pass
  
  def __and__(self, other):
    return AndSpecification(self, other)
  
class Filter:
  def filter(self, items, spec):
    pass
  
class AndSpecification(Specification):
  def __init__(self, *args):
    self.args = args
  
  def is_satisfied(self, item):
    return all(map(
    lambda spec: spec.is_satisfied(item), self.args
    ))
  
class ColorSpecification(Specification):
  def __init__(self, color):
    self.color = color
    
  def is_satisfied(self, item):
    return item.color == self.color

class SizeSpecification(Specification):
  def __init__(self, size):
    self.size = size
    
  def is_satisfied(self, size):
    return item.size == self.size
  
class FilterBySpec(Filter):
  def filter(self, items, spec):
    for item in items:
      if spec.is_satisfied(item):
        yield item
        
if __name__ == '__main__':
  apple = Product('Apple', Color.GREEN, Size.SMALL)
  tree = Product('Tree', Color.GREEN, Size.LARGE)
  house = Product('House', Color.BLUE, Size.LARGE)
  
products = [apple, tree, house]
# using naive class
pf = ProductFilter()
for p in pf.filter_by_color(products, Color.Green):
  print(f'{p.name} is green')

# using specification filter
bf = FilterBySpec()
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
  print(f'{p.name} is GREEN')

# using specification filter and combibing filters
blue = ColorSpecification(Color.BLUE)
large_blue = AndSpecification(large, blue)
for p in bf.filter(products, large_blue):
  print(f'{p.name} is large and blue')
  
# using specification filter and combibing filters and reassigned magic 'and' method
large_blue = large & blue
for p in bf.filter(products, large_blue):
  print(f'{p.name} is large and blue')

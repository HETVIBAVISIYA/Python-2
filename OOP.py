

# Blueprint
class dog:
  # attribute
  name="coco"
  weight=10

  # method
  def eating(self):
    print(f"{self.name} has {self.weight} and eat parleG")

# create a new instance is creating a new object
d1 = dog()
d1.name = "he2"
print(d1.name)
d1.eating()

d2 = dog()
print(d2.name)


class band:
  # __init__ is constructor. The constructor is the method which will be called when the instance is
  # created. __init__ method will be called automatically when the band instance is created. Purpose
  # of constructor is to providing mendetory attributes to the instance or object. So if I give the
  # arguments to the __init__ method then I have to give a value of the arguments to the constructor
  # when I create a instance. 

  number_of_gold_records = 0
  number_of_platinum_records = 0
  def __init__(self, bn, music_genre):
    self.band_name = bn
    self.music_genre = music_genre

  def describe_band(self):
    print(f"Band Name is {self.band_name} and Genre is {self.music_genre}")

  def __str__(self):
    return f"Band Name is {self.band_name} and Genre is {self.music_genre}"
    

  def is_active(self):
    return True
  
  def set_number_of_gold_record(self,number):
    self.number_of_gold_records = number

  def set_number_of_platinum_record(self,number):
    self.number_of_platinum_records = number

b1 = band("H&J Band","Pop Songs")
print(b1.band_name)
print(b1.music_genre)
b1.describe_band()
print(b1)
print(b1.is_active())

print()
print(b1.number_of_gold_records)
print(b1.number_of_platinum_records)
b1.set_number_of_gold_record(10)
b1.set_number_of_platinum_record(30)
print(b1.number_of_gold_records)
print(b1.number_of_platinum_records)


class coverBand(band):
  
  covered_band_and_performance = []
  def __init__(self, bn, music_genre):
    band.__init__(self,bn,music_genre)
    coverBand.covered_band_and_performance.append(self)

  def displayAll(self):
    print(f"Band Name is {self.band_name} and Genre is {self.music_genre}")

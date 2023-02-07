class Angle:
 def __init__(self, angle = 0) -> None:
     self.__angle = angle


 # метод __eq__ позволяет сравнивать объекты, используя оператор ==
 def __eq__(self, __o: object) -> bool:
   return self.__angle == __o.__angle

 @property
 def angle(self):
    return self.__angle

 @angle.setter
 def angle(self, angle):
    self.__angle = angle

if __name__ == "__main__":
  a1 = Angle(30)
  a2 = Angle(45)
  a3 = Angle(30)
  print(a1, a2, a3)
  print(f'a1 == a2 -> {a1 == a2}')
  print(f'a1 == a3 -> {a1 == a3}')
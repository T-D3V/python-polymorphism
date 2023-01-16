from abc import ABC, abstractmethod

class Spy:
  __damage:int = 3
  __hitpoints:int = 20
  def __init__(self, name:str) -> None:
    self.name = name
  
  @property
  def isDecommisioned(self) -> bool:
    return False if self.__hitpoints > 0 else True
  
  @property
  def damage(self) -> int:
    return self.__damage
  
  def getDamaged(self, damage:int) -> None:
    self.__hitpoints -= damage
  
  def damageOthers(self) -> int:
    return self.__damage
  
  def reduceDamage(self, reduction:int) -> None:
    self.__damage -= reduction
    if(self.__damage < 0):
      self.__damage = 0

class Scherge(ABC):
  _damge:int
  _hitpoints:int
  def __init__(self, name:str) -> None:
    self.__name:str = name
  
  @property
  def name(self) -> str:
    return self.__name
  
  @abstractmethod
  def attack(self, spy:Spy) -> None:
    if(self._hitpoints > 0):
      spy.getDamaged(self._damge)
      self._hitpoints -= spy.damageOthers()
  
class Hitter(Scherge):
  _damge = 1
  _hitpoints = 5
  
  def __init__(self, name:str) -> None:
    super().__init__(name)
  
  def attack(self, spy: Spy) -> None:
    while self._hitpoints > 0:
      super().attack(spy)
  
class Killer(Scherge):
  _damge = 10
  _hitpoints = 5
  
  def __init__(self, name:str) -> None:
    super().__init__(name)
    
  def attack(self, spy: Spy) -> None:
    super().attack(spy)
  
class Hacker(Scherge):
  _damge = 0
  _hitpoints = 2
  
  def __init__(self, name:str) -> None:
    super().__init__(name)
  
  def attack(self, spy: Spy) -> None:
    super().attack(spy)
    spy.reduceDamage(1)
  
class Enemy:
  __schergen:list[Scherge] = []
  def __init__(self, name:str) -> None:
    self.__rival:Spy
    self.__name:str = name
    
  @property
  def rival(self) -> Spy:
    return self.__rival
  
  @rival.setter
  def rival(self, rival:Spy) -> None:
    self.__rival = rival
  
  @property
  def name(self) -> str:
    return self.__name
  
  @property
  def Schergen(self) -> list[Scherge]:
    return self.__schergen
  
  def AddScherge(self, scherge:Scherge) -> None:
    self.__schergen.append(scherge)
    
  def FocusSchergenOnRival(self) -> None:
    while not self.__rival.isDecommisioned and any(scherge._hitpoints > 0 for scherge in self.__schergen):
      for scherge in self.__schergen:
        scherge.attack(self.__rival)
    
    if(self.__rival.isDecommisioned):
      print(self.__rival.name + " has been beaten")
    else:
      print(self.name + " did resign")
    
  


def main():
  blofeld:Enemy = Enemy("Blofeld")
  bond:Spy = Spy("James Bond")
  blofeld.rival = bond
  blofeld.AddScherge(Hitter("Beisser"))
  blofeld.AddScherge(Killer("Xenia"))
  blofeld.AddScherge(Hacker("Boris"))
  blofeld.FocusSchergenOnRival()

if __name__ == "__main__":
  main()
class Pet:
  
  def __init__(self):
    self.name = ""
    self.food = 5
    self.happiness = 5
    self.health = 5
    self.sleep_timer = 0

  def set_name(self, newName):
    self.name = newName

  def feed(self):
    self.food += 1

  def play(self):
    self.happiness += 1

  def energize(self):
    self.health += 1

  def sleep(self):
    self.sleep_timer += 1

  def update(self):
    self.food += 1
    self.happiness -= 1

import random

class Asskeeper:
  def __init__(self, filename):
    self.open(filename)

  def open(self, filename):
    f = open(filename, 'r')
    self.lines  = f.readlines()
    self.cur = 0
    f.close()

  def get(self):
    return self.lines[self.cur].strip()

  def get_proxies(self):
    proxies = { 'http' : self.get() }
    return proxies

  def count(self):
    return len(self.lines)

  def swap(self, next):
    if next < 0: next = self.count() - 1
    elif not next < self.count: next = 0
    self.cur = next
    return self

  def move(self, pos):
    self.swap(self.cur + pos)
    return self

  def random(self):
    self.swap(random.randint(0, self.count() - 1))
    return self

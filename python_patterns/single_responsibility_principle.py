# one class - one responsibility

class Journal
  def __init__(self):
    self.entries = {}
    self.count = 0
    
  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}:{self.text}')
  
  def remove_entry(self, pos):
    del self.entries[pos]
  
  def __str__(self):
    return '\n'.join(self.entries)
                        
    
 
class NotOnlyJournal
""" this class has an additional method that violates CRP """
  def __init__(self):
    self.entries = {}
    self.count = 0
    
  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}:{self.text}')
  
  def remove_entry(self, pos):
    del self.entries[pos]
  
  def __str__(self):
    return '\n'.join(self.entries)
  
  def save(self, filename):
    file = open(filename, 'w')
    file.write(str(self))
    file.close
   
  def load_from_web(self):
    pass
  
  
# saving methods should be organised in separate class for simpler maintenance in future

class EntriesManager:
  @staticmethod
  def save(journal, filename):
    file = open(filename, 'w')
    file.write(journal)
    file.close
    
  @staticmethod   
  def load_from_web():
    pass
  
    
                        

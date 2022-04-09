class EC2instances:
  def __init__(self, name, ami, type, dns):
      self.name = name
      self.ami = ami
      self.type = type
      self.dns = dns

  def get_name(self):
    return self.name
  def set_name(self, name):
    self.name = name

  def get_ami(self):
    return self.ami  
  def set_ami(self, ami):
    self.ami = ami  

  def get_type(self):
    return self.type
  def set_type(self, type):
    self.type = type

  def get_dns(self):
    return self.dns
  def set_dns(self, dns):
    self.dns = dns      
    
  def __str__ (self):
    return "Instancat e krijuara jane kto:\nEmri:" + str(self.name) +"\nAmi_ID: " + self.ami + "\nInstance_type" + self.type + "\nPrivate DNS:" + self.dns + "\n"   
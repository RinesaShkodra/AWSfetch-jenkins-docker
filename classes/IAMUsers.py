class IAMUsers:
  def __init__(self, name, arn):
    self.name = name
    self.arn = arn


  def get_username(self):
    return self.name
  def set_username(self, name):
    self.name = name

  def get_arn(self):
    return self.arn
  def set_arn(self,arn):
    self.arn = arn
     
  def __str__(self):
    return "Userat e AWS IAM jane:\nUsername:" + str(self.name) + "\nArn: "+ self.arn
 
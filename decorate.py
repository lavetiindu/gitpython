def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "Hello madhu"
print(myfunction())
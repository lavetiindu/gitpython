def my_function(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "indu", "lname": "laveti"}
my_function(**person)
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("indu123", age = 18, city = "vizag", hobby = "singing")
name_length = input('What is your name? ')

if len(name_length) < 3:
  print('Name length must be at least 3 characters')

elif len(name_length) > 50:
  print('Name can be maximum of 50 characters')

else:
  print('Name looks good')
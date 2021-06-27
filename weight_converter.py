weight = int(input('Weight:'))
unit = input('(L)bs or Kg: ')

if unit.upper() == 'L':
  converted_weight = weight * 0.45
  print(f'Weight is: {converted_weight} lbs')
else:
  converted_weight = weight / 0.45
  print(f'Weight is: {converted_weight} kg')

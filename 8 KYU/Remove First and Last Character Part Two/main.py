def array(string):
  new_array = string.split(',')
  try:
    new_array.remove(new_array[0])
    new_array.remove(new_array[-1])
    x = ', '.join(new_array)
    if x == '':
      return None
    else:
      return x.replace(',', '')
  except IndexError:
    return None

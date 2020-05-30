#This is a spin off of my first kata. You are given a list of character sequences as a comma separated string. Write a function which returns another string containing all the character sequences except the first and the last ones, separated by spaces. If the input string is empty, or the removal of the first and last items would cause the string to be empty, return a null value.

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

def remove_element(arr, element):
  """Removes the first occurrence of a specific element from an array.

  Args:
    arr: The input array.
    element: The element to remove.

  Returns:
    The modified array.
  """

  if element in arr:
    arr.remove(element)
  return arr

# Example usage:
my_array = [1, 2, 3, 2, 4]
my_array = remove_element(my_array, 2)
print(my_array)
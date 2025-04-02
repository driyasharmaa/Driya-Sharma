import math
def circumference(radius):
  """Calculate the circumference of a circle with its radius. """
  return 2 * math.pi * radius

# Example: 
r = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle is: {circumference(r):.2f}")
import sys

# Define a main() function that prints a listing.
def main():
  principal = 1000
  rate = 0.05
  numyears = 5
  year = 1
  while year <= numyears:
    principal = principal*(1+rate)
    print "%3d  %0.2f" % (year, principal)
    year +=1

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

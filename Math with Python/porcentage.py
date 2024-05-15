# Find out the percentage of numbers' given

a = int(input("PART:"))
b = int(input("WHOLE:"))

def percentage(part, whole):
  percentage = (float(part)*float(whole)) / 100
  return str(percentage) + "%"


print(percentage(a, b))
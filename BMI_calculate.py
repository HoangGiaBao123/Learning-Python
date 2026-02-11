def calculate(Height, Weight):
  result = Weight / pow(Height, 2)
  print(f'Your BMI is: {result}')

if __name__ == '__main__':
  height = float(input("Enter your height (m): "))
  weight = float(input("Enter your weight (kg): "))

calculate(height, weight)

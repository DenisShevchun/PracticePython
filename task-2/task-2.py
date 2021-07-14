import math

while True:
  print("\n-----------------HINT: You can type 'end' anytime to exit------------------\n")
  yourInput = input("Enter an integer number: ")

  if yourInput == "end":
    break
  elif not yourInput.isdigit():
    print("invalid number.")
    continue
  else:
    num_1 = int(yourInput.strip())
  
  operation = input("Enter an operation (+, -, *, /, %, cos, sin, tan, ctan, log, ln): ")
  if operation == "end":
      break
  elif operation == "cos":
    print (math.cos(num_1))
    continue
  elif operation == "sin":
    print (math.sin(num_1))
    continue
  elif operation == "tan":
    print (math.tan(num_1))
    continue
  elif operation == "ctan":
    print (math.cos(num_1)/math.sin(num_1))
    continue
  elif operation == "log":
    print (math.log(num_1))
    continue
  elif operation == "ln":
    print (math.log1p(num_1))
    continue
  
  anotherInput = input("Enter another number: ")
  if anotherInput == "end":
    break

  if not anotherInput.isdigit():
    print("invalid number.")
    continue
  else:
    num_2 = int(anotherInput.strip())

  if operation == "+":
    ans = num_1+num_2
  elif operation == "-":
    ans = num_1-num_2
  elif operation == "*":
    ans = num_1*num_2
  elif operation == "/":
    ans = num_1/num_2
  elif operation == "%":
    ans = num_1%num_2
  else:
    print("invalid operation.")
    continue

  print(num_1, operation, num_2, "=", ans)

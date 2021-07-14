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
  
  operation = input("Enter an operation (+, -, *, /): ")
  if operation == "end":
      break
  operation = operation.strip()
  
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
  else:
    print("invalid operation.")
    continue

  print(num_1, operation, num_2, "=", ans)

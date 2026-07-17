h = int(input("Enter a number: "))

if h > 1:
    for i in range(2, int(h**0.5)+1):
      if h % i == 0:
        print("This is not a prime number.")
        break
      else:
        print("This is a prime number.")
else:
    print("This is not a prime number.")
a = []
for i in range(10):
    num = input(f"Enter number{i+1}: ")
    a.append(num)
    
sum = 0
for i in range(0, len(a)):
  sum += i

print(f"Addition of 10 numbers is {sum}")

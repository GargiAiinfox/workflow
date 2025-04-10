'''v=int(input("enter the number: "))
ascii_value=65
for i in range(v):
    for j in range(i+1):
      a=chr(ascii_value)
      print(" ",a,end="")
    ascii_value += 1
    print("\n")'''

'''v=int(input("enter the number of rows : "))
ascii_value= 69
for i in range(v,0,-1):
    for j in range(i):
      a=chr(ascii_value)
      print(a, end= "")
    ascii_value -= 1
    print("\n")'''
    
n=int(input("enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
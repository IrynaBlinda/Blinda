print("Hello")
print()
name=input ("Як вас звати? \n")
print("Дуже приємно познайомитися", name)
year = int (input("В якому році Ви народилися? - "))
age=2020-year
answer=int(input("Увас був день народження? (1-Yes / 0-No)\n"))
if (answer!=0):
    print("Вам", age, "років")
else:
    print("Вам", age-1, "років")
print("До побачення!")    
    

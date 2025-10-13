try: 
    num1 = int(input("Number 1 = "))
    num2 = int(input("Number 2 = "))

    print(f"{num1} + {num2} = {num1 + num2}")

except ValueError:
    print("Error: Please input integer")
    
except Exception:
    print("Error: have some errors")
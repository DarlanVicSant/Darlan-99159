import os
os.system("cls")


vector = []

NUM_ELEMENTS = 5

print(f"Please enter {NUM_ELEMENTS} numbers.")

for i in range(NUM_ELEMENTS):
   
    while True:
        try:
     
            value = float(input(f"Enter number {i + 1}: "))
            break  
        except ValueError:
 
            print("Invalid input. Please enter a valid number.")

    if value < 0:
  
        vector.append(0)
    else:
 
        vector.append(value)


print("\n--- Final Vector Values ---")



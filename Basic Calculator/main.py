import time

def main():
    time.sleep(.5)
    print(f"\n{"-"*40}")
    time.sleep(.5)
    print("Welcome to Simple Calculator")
    repeat = True
    while True:
        try:
            if repeat:
                time.sleep(.5)
                print(f"\n{"*"*15} Let's Calculate {"*"*15}")
                time.sleep(1)
                x = int(input("Enter the First Number: "))
                y = int(input("Enter the Second Number: "))
                result = None
                while True:
                    ope = input("Choose an Operation (+, -,x, /): ")
                    if ope == "+":
                        result = x + y
                        break
                    elif ope == "-":
                        result = x - y
                        break
                    elif ope == "x":
                        result = x * y
                        break
                    elif ope == "/":
                        result = x / y
                        break
                    else:
                        print("\nError: Please enter an valid Operator")
                        continue
                time.sleep(2)
                print(f"\nThe result is: {result}")
                time.sleep(1)
                repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
                repeat = True if repeat == "yes" else False
            else:
                time.sleep(2)
                print("\nGoodbye")
                time.sleep(1)
                print(f"{"-"*40}\n")
                exit()
        except ValueError:
            time.sleep(1)
            print("\n Please Enter a Valid Number To perform Calculation !")
            repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            repeat = True if repeat == "yes" else False
        except ZeroDivisionError:
            time.sleep(1)
            print("Error: Division by zero is not allowed!")
            repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            repeat = True if repeat == "yes" else False

if __name__ == "__main__":
    main()
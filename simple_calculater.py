process1=input("pleas enter what you want?(plural,minus,multiplied by,distribution)").strip()
print("****************************************************************************")
if process1=="plural":
    first_number = int(input("please enter first number:"))
    second_number = int(input("please enter second number:"))
    result= first_number + second_number
    print("-------------------------------------------------")
    print(f"Result is:{first_number}+{second_number}={result}")
    print("-------------------------------------------------")

elif process1=="minus":
    first_number = int(input("please enter first number:"))
    second_number = int(input("please enter second number:"))
    result= first_number - second_number
    print("-------------------------------------------------")
    print(f"Result is:{first_number}-{second_number}={result}")
    print("-------------------------------------------------")

elif process1=="multiplied by":
    first_number = int(input("please enter first number:"))
    second_number = int(input("please enter second number:"))
    result= first_number * second_number
    print("-------------------------------------------------")
    print(f"Result is:{first_number}*{second_number}={result}")
    print("-------------------------------------------------")

elif process1 == "distribution":
    first_number = int(input("please enter first number:"))
    second_number = int(input("please enter second number:"))

    if second_number == 0:
        print("invalid number!!!")
    else:
        result = first_number / second_number
        print("-------------------------------------------------")
        print(f"Result is:{first_number}/{second_number}={result}")
        print("-------------------------------------------------")
else:
    print("just choose from the box!")
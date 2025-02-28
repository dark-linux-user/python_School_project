##############################################################
x = input("Put the Distance: ")
convert_from = input("Unit of length to convert from (kilometer, meter, decimeter, or santimitr): ").lower()
convert_to = input("Unit of length to convert to (kilometer, meter, decimeter, or santimitr): ").lower()
##############################################################
try:
    Distance = float(x)
except ValueError:
    print("Try again the Value is not a number")
    exit()

#############################################################
if convert_from == "santimitr" and convert_to == "santimitr":
    print(f"The length in santimitr is: {Distance}")

elif convert_from == "decimeter" and convert_to == "decimeter":
    print(f"The length in decimeter is: {Distance}")

elif convert_from == "meter" and convert_to == "meter":
    print(f"The length in meter is: {Distance}")



####################################################
elif convert_from == "kilometer" and convert_to == "kilometer":
    print(f"The length in kilometer is: {Distance}")

    
elif convert_from == "santimitr" and convert_to == "decimeter":
    print(f"{Distance / 10} dm")

elif convert_from == "santimitr" and convert_to == "meter":
    print(f"{Distance / 100} m")

elif convert_from == "santimitr" and convert_to == "kilometer":
    print(f"{Distance / 100000} km")

####################################################
elif convert_from == "decimeter" and convert_to == "santimitr":
    print(f"{Distance * 10} sm")

elif convert_from == "decimeter" and convert_to == "meter":
    print(f"{Distance / 10} m")

elif convert_from == "decimeter" and convert_to == "kilometer":
    print(f"{Distance / 10000} km")

#######################################################
elif convert_from == "meter" and convert_to == "santimitr":
    print(f"{Distance * 100} sm")

elif convert_from == "meter" and convert_to == "decimeter":
    print(f"{Distance * 10} dm")

elif convert_from == "meter" and convert_to == "kilometer":
    print(f"{Distance / 1000} km")
##################################################
elif convert_from == "kilometer" and convert_to == "santimitr":
    print(f"{Distance * 100000} sm")

elif convert_from == "kilometer" and convert_to == "decimeter":
    print(f"{Distance * 10000} dm")

elif convert_from == "kilometer" and convert_to == "meter":
    print(f"{Distance * 1000} m")

else:
    print("Try again")
################################################################
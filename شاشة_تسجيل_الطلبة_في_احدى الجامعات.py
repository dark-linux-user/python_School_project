print("""  
      
                                  "Student Registration Screen Project"

      

  Project Designer Name : Mohammad jobran                     The github account: https://github.com/Dark-hack
""")

first_name=input("Enter your first name : ").lower()




if len(first_name) =="":
    print("the university number is less than required!!")
    exit()



else:
    pass




last_name=input("Enter your last name : ").lower()



if last_name == "":
    print("the university number is less than required!!")
    exit()



else:
    pass




university_number=input("Enter your university number :").lower()

if len(university_number) != 10 :
    print("the university number is less than required!!")
    exit()



else:
    pass

student_email=input("Enter the student email : ").lower()


if len(student_email) =="":
    print("the university number is less than required!!")
    exit()



else:
    pass



hours=input("Enter the number of hours you want to register for the current semester : ")

if len(first_name) =="":
    print("the university number is less than required!!")
    exit()



try:
    hours = float(hours)
except ValueError:
    print("The number of hours is invalid!!")
    exit()




else:
    pass

type_of_study=input("Choose the type of study systematic, parallel, international : ").lower()


if type_of_study == "systematic":
    systematic=10
    sum_all=hours*systematic + 250

elif type_of_study == "parallel":
    parallel=20
    sum_all=hours*parallel + 250

elif type_of_study == "international":
    international=float(30)
    sum_all=hours*international + 250

else:
    print("Try again You have an error in the study type!!!")
    exit()



#عرض ملخص المعلومات السابقة 
print(f"""

First name : {first_name}

Last name : {last_name}

University number : {university_number}

Student email : {student_email}

Number of hours you want to register : {hours}

the type of study : {type_of_study}

Total money owed to the university : {sum_all}
""")

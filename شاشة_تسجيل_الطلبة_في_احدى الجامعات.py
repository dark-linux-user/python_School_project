print("""                            University student registration screen

Project Designer Name : Mohammad jobran                     My github account: https://github.com/dark-linux-user/
    

                My project in github : https://github.com/dark-linux-user/python_School_project
      

""")
# ادخال الاسم الاول وتحويله الى حرف صغير وتجاهل المسافات
first_name=input("""
################################                 
Enter your first name : """).lower().strip()


#تحقق اذا كان طول اسم المستخدة الاول صفر اذا كان كذالك اطبع انت لم تدخل الاسم واخرج من البرنامج
if len(first_name) == 0:
    print("You did not write the name!")
    exit()
# ادخال الاسم الاخير وتحويله الى حرف صغير وتجاهل المسافات
last_name=input("""
################################
Enter your last name : """).lower().strip()
#تحقق اذا طول الاسم الاخير يساوي صفر اذا هو كذلك اطبع انت لم تدخل الاسم الاخير واخرج من البرنامج والا لاتفعل شيء
if len(last_name) == 0:
    print("\nYou did not write the last name!!")
    exit()
#ادخال الرقم الجامعي وتجاهل المسافات 
university_number=input("""
###########################################                        
Enter the 10-digit university number : """).strip()
# محاولة التحويل المتغيير الى عدد صحيح ان لم يستطيع تحويله اطبع الموجود بين الاقواس واخرج من البرنامج
try:
    int(university_number)
except ValueError:
    print("University number is not a number")
    exit()
# تحقق اذا طول المتغيير لا يساوي الرقم 10 اطبع الموجود بين علامتان التنصيص واخرج من البرنامج  اذا لم يتحقق الشرط لا تفعل شيء
if len(university_number) != 10 :
    print("The university number is not made up of 10 digits!!")
    exit()
# ادخلا  ايميل المستخدم وتجاهل المسافات
student_email=input("""
##############################
Enter the student email : """).lower().strip()
#اذا طول المتغيير اكبر او يساوي 5 اطبع الموجود بين علامتان الاتنصيص ثم اخرج من البرنامج
if len(student_email) <= 5:
    print("The email is not correct!!")
    exit()
#ادخل عدد الساعات المراد دراستها في الفصل 
hours=input("""
###############################################################################
Enter the number of hours you want to register for the current semester : """)
#تحقق اذا طول متغيير الساعات يساوي صفر اطبع الموجود بين الاقواس ثم اخرج من البرنامج
if len(hours) == 0:
    print("You did not write the number of hours!!")
    exit()
#حاول تغيير متغيير الساعات الى عدد عشري ان لميستطع التحويل اطبع الموجود بين علامتان التنصيص ثم اخرج من البرنامج 
try:
    float(hours)
except ValueError:
    print("The number of hours is not a number!!")
    exit()
# اطلب من المستخدم  ادخال رقم نوع الدراسة  ثم تجاهل المسافات 
type_of_study=input("""
             
systematic==> 1
                    
parallel==> 2
                    
international==> 3
                    
Choose the type of study:""").strip()
#  تحقق اذا كان المتغيير يساوي1 اذا كذلك اعمل متغيير وخزن داخله القيمة 10 وقم وقم بعمل متغيير اخر وقم بجعل قيمته العدد العشري من الساعات ضربه بالمتغيير ويادة عليه الرقم  250 وقم بعمل متغيير اخر وضع قيمته نفس قيمة رقم الاختيار
if type_of_study == "1":
    systematic=10
    sum_all=float(hours)*systematic + 250
    study_type="systematic"
#تحقق اذا كان المتغيير يساوي2 اذا كذلك اعمل متغيير وخزن داخله القيم20 وقم وقم بعمل متغيير اخر وقم بجعل قيمته العدد العشري من الساعات ضربه بالمتغيير ويادة عليه الرقم 250 وقم بعمل متغيير اخر وضع قيمته نفس قيمة رقم الاختيار
elif type_of_study == "2":
    parallel=20
    sum_all=float(hours)*parallel + 250
    study_type="parallel"
# تحقق اذا كان المتغيير يساوي2 اذا كذلك اعمل متغيير وخزن داخله القيم30 وقم وقم بعمل متغيير اخر وقم بجعل قيمته العدد العشري من الساعات ضربه بالمتغيير ويادة عليه الرقم250 وقم بعمل متغيير اخر وضع قيمته نفس قيمة رقم الاختيار
elif type_of_study == "3":
    international=30
    sum_all=float(hours) * international + 250
    study_type="international"
#ان لم يتحقق الشرط اطبع الموجود ين الاقواس واخرج من البرنامج
else:
    print("You did not write the type of study correctly!!")
    exit()
# عرض ملخص المعلومات السابقة طباعة الاسم الاول والاسم الاخير والرقم الجامعي واليميل وعدد الساعات التي يريد حجزه ونوع التعليم الذي يريد المستخدم تعلمه وطباعة مجموع الاموال المستحقة للجامعة
print(f"""
#####################################################################
             Show summary of all previous information               
                                                                    
first name : {first_name}                                                 
                                                                    
Last name : {last_name}                                             
                                                                    
University number : {university_number}                                     
                                                                    
Student email : {student_email}                                      
                                                                    
Number of hours you want to register : {hours}                           
                                                                    
the type of study : {study_type}                                    
                                                                     
Total money owed to the university : {sum_all}                          
#####################################################################
""")

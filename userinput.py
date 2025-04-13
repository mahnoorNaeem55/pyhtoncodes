#program for user's name and age 
print("hey user welcome!")
user_name=input("enter your name")
user_age=int(input("enter your age in as whole number"))
if user_age==0 or user_age<0:
    print("age cannot be 0 or less,please enter a valid age")
else:
    print("Name",user_name)
    print("you're",user_age,"old!")
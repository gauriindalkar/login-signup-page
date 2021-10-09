import json
print("WELCOME SIGNUP AND LOGIN PAGE")
user=input("do you want sign up or login page:")
if user=="signup":
    username=input("enter the name:")
    password_1=input("enter password:")
    password_2=input("enter confirm password:")
    if len(password_2)>=8 or len(password_2)<=15:
        if password_2 in "@" or "#" or "$":
            if "0" or "9" in password_2:
                descripation=input("enter the descripation:")
                date_of_brith=input("enter date of birth:")
                hobbies=input("enter the hobbies:")
                gender=input("enter the gender female/male/other:")
                print("congrates",username)
                user_details={"username":username,"password_2":password_2,"descripation":descripation,"data of birth":date_of_brith,"hobbies":hobbies,"gender":gender}
                with open("user_data.json","a")as file:
                    a=json.dump(user_details,file,indent=4)
            else:
                print("your password is not correct")
else:
    if user=="login":
        name=input("enter the name:")
        password=input("enter the password:")
        with open("user_data.json","r")as file:
            data=json.load(file)
            if password==data["password_2"]:
                print("login successfully")
                print(data)
    else:
        print("your details is wrong")

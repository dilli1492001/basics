user = "admi"
logged = False
if logged:
    print("user log id")
    if user == "admin":
        print("admin access grant")
    elif user == "editor":
        print("editor access grant")
    else:
        print("limted access grant")
else:
    print("log in first")
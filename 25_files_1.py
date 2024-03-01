employee_file = open("employees.txt","r")
#employee_file = open("employees.txt","w") #write to file
#employee_file = open("employees.txt","a") #append to file
#employee_file = open("employees.txt","r+") #read/write to file
while True:
    line = employee_file.readline()
    print(line)
    if ("" == line):
        print ("file finished")
        break;
employee_file = open("employees.txt","r")
print(employee_file.read())
#print(employee_file.readable())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readline())



employee_file.close()
employee_file = open("c:\Grad Programme Docs\Fall 2023\Computer Communication\Projects\learn_python\employees.txt","r")

print(employee_file.readlines()[1])
employee_file.close()
employee_file = open("c:\Grad Programme Docs\Fall 2023\Computer Communication\Projects\learn_python\employees.txt","r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()




#********** Writing to external files in python**********

employee_file=open("employee.txt","a")
employee_file.write("\nRamu-Human Resources")
# to create a new file
employee_fil1=open("employee1.txt","w")
employee_fil1.write("Joxin Jose")

# Creating HTML page
htmlpage=open("index.html","w")
htmlpage.write("<h1>This is HTML</h1>")

employee_file.close()

# using 'w' instead of 'a' will overwrite the entire file


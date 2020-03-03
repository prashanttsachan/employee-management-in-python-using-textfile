import os
class Employee:
	def __init__(self, name, dept, jobTitle):
		self.name = name
		self.dept = dept
		self.jobTitle = jobTitle
		print ("Employee added successfully.")

	def editName (self, name):
		self.name = name

	def editDept (self, dept):
		self.dept = dept

	def editTitle (self, title):
		self.jobTitle = title

	def delete (self):
		del self

	def display(self, id):
		print ("Employee details:\n" + self.name + " " + str(id) + " " + self.dept + " " + self.jobTitle)

	def data (self, id):
		return self.name + "," + str(id) + "," + self.dept + "," + self.jobTitle

emp = {}
try:
	f = open('myfile.txt', 'r')
	lines = f.read()
	lines = lines.split("\n")
	for line in lines:
		empdet = line.split(",")
		emp[int(empdet[1])] = Employee (empdet[0], empdet[2], empdet[3])
except IOError:
	f = open('myfile.text', 'w')
finally:
	f.close()
print ("Enter\n 0: Exit\n 1: New Employee\n 2: Edit Name\n 3: Edit Department\n 4: Edit Job Title\n 5: To display Employee\n 6: Delete Employee\n 7: Continue")
allTask = [0, 1, 2, 3, 4, 5, 6]
task = int(input(" ")) 
while task in allTask:
	if task == 0:
		break
	elif task == 1:
		print ("Employee details: ")
		name = input("Name: ")
		row = int(input("Id: "))
		dept = input("Department: ")
		title = input("job Title: ")
		emp[row] = Employee(name, dept, title)
	elif task == 2:
		row = int(input("Existing id: "))
		name = input("New name: ")
		emp[row].editName(name)
	elif task == 3:
		row = int(input("Existing id: "))
		dept = input("New Department: ")
		emp[row].editDept(dept)
	elif task == 4:
		row = int(input("Existing id: "))
		title = input("New job Title: ")
		emp[row].editTitle(title)
	elif task == 5:
		row = int(input("Id: "))
		emp[row].display(row)
	elif task == 6:
		row = int(input("Id: "))
		emp[row].delete()
		del emp[row]
	task = int(input("Operation: "))

data = ""
for row in emp:
	data += emp[row].data(row) + "\n"
data = data.strip("\n")
file = open('myfile.txt','w')
file.write(data)
file.close() 

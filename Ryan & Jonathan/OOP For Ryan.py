class Student(object):
#    """This is the Student class. It's the top class."""

    def __init__(self, firstname, lastname, gender, status, gpa):
        """Initialize the student-object with first and last name variables etc.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def show_myself(self):
        """Method: show_myself()
        prints out all the variables."""
        print("\n")
        print("-------------------------------")
        print("Name: {}".format(self.firstname), "{}".format(self.lastname))
        print("Gender: {}".format(self.gender))
        print("Status: {}".format(self.status))
        print("GPA: {}".format(self.gpa))
        print("-------------------------------")

    def study_time(self, studytime):
        """Method: study_time()
        Will increment the gpa of the student according to the formula:
        gpa = gpa + log(studytime)"""
        self.gpa += np.log(studytime)
        if self.gpa > 4.0:
            self.gpa = 4.0
            
##########################################################################
##########################################################################
##########################################################################

# Since the class definition is in a different file, we needed to import it
# So don't forget the myfun. prefix!!
firstnames = ['Jim', 'Jack', 'Michelle', 'Ron', 'Coline']
lastnames = ['Dorn', 'Boon', 'Mills', 'Woods', 'Jung']
genders = ['male', 'male', 'female', 'male', 'female']
statuses = ['junior', 'freshman', 'senior', 'sophomore', 'junior']
gpas = [3.8, 3.2, 2.0, 3.5, 3.4]

student_list =[]
for fname,lname,gen,stat,gpa in zip(firstnames,lastnames,genders,statuses,gpas):
    # Create students and append them to list
    student_list.append(myfun.Student(fname,lname,gen,stat,gpa))

studytime_list = [60, 100, 40, 300, 1000]
for i,stime in enumerate(studytime_list):
    student_list[i].show_myself()
    print("Study time is {}".format(stime))
    print("Now let the guy study ...")
    student_list[i].study_time(stime)

print(" ")
print("New GPA's: ")
for x in student_list:
    x.show_myself()








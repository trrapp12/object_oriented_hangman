# Create two classes, an Employee and a Job, where the Employee class has-a Job class.
# When printing an instance of the employee object the output should look something like this:
#
# My name is Morgan Williams, I am 24 years old and I am a Software Developer

class Job(object):
    def __init__(self,title,payrate)
        self.title = title
        self.payrate = payrate

class Employee(object):
    def __init__(self,name,age,job, job_title, job_payrate):
        self.name = name
        self.age = age
        self.job = Job(job_title, job_payrate)

new_employee = Employee("Morgan Williams", "24", "Software Developer")

print Morgan

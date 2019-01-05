
# check wheter an employee has achieved target for a week.

class Employee:
    name="Joxin"
    designation="Sales Executive"
    target_for_week=5

    def hasTargetAchieved(self):
        if self.target_for_week>=5:
            print(self.name+" has achieved the target for this week")
    
employeeOne=Employee()
employeeOne.hasTargetAchieved()
heello()
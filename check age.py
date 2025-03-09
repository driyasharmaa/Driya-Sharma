class StudentEnrollment:
    def __init__(self, max_students=20):
        self.max_students = max_students
        self.enrolled_students = []
    
    def enroll_student(self, name, age):
        if len(self.enrolled_students) >= self.max_students:
            print("Enrollment limit reached. Cannot enroll more students.")
            return
        
        if age < 10:
            self.enrolled_students.append({'name': name, 'age': age})
            print(f"Student {name} has been enrolled successfully.")
        else:
            print("Age must be below 10 to enroll.")
    
    def show_enrolled_students(self):
        if not self.enrolled_students:
            print("No students are enrolled yet.")
        else:
            print("Enrolled Students:")
            for student in self.enrolled_students:
                print(f"Name: {student['name']}, Age: {student['age']}")
    

# Create an instance of the StudentEnrollment class
enrollment_system = StudentEnrollment()
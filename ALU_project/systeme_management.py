#!/usr/bin/env python3
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, surname, age, grade):
        if any(student["StudentID"] == student_id for student in self.students):
            print("Error: Student ID must be unique.")
            return
        
        student = {
            "StudentID": student_id,
            "Name": name,
            "Surname": surname,
            "Age": age,
            "Grade": grade,
            "Attendance": []
        }
        self.students.append(student)
        print("Student added successfully!")
    
    def update_student(self, student_id, key, value):
        for student in self.students:
            if student["StudentID"] == student_id:
                if key in student:
                    student[key] = value
                    print("Student record updated successfully!")
                else:
                    print("Invalid field.")
                return
        print("Student not found.")
    
    def delete_student(self, student_id):
        for student in self.students:
            if student["StudentID"] == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found.")
    
    def search_student(self, student_id):
        for student in self.students:
            if student["StudentID"] == student_id:
                return student
        return "Student not found."
    
    def track_attendance(self, student_id, date, status):
        for student in self.students:
            if student["StudentID"] == student_id:
                student["Attendance"].append({"Date": date, "Status": status})
                print("Attendance recorded successfully!")
                return
        print("Student not found.")
    
    def generate_report(self):
        if not self.students:
            print("No students in the system.")
            return
        
        print("\nStudent Report:")
        for student in self.students:
            print(f"ID: {student['StudentID']}, Name: {student['Name']} {student['Surname']}, Age: {student['Age']}, Grade: {student['Grade']}")
            print("Attendance:")
            for attendance in student["Attendance"]:
                print(f"  Date: {attendance['Date']}, Status: {attendance['Status']}")
            print("-" * 30)
    
# Example Usage
if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student("S001", "John", "Doe", 16, "10th Grade")
    sms.add_student("S002", "Jane", "Smith", 15, "9th Grade")
    sms.update_student("S001", "Grade", "11th Grade")
    sms.track_attendance("S001", "2025-03-10", "Present")
    sms.track_attendance("S002", "2025-03-10", "Absent")
    print(sms.search_student("S001"))
    sms.generate_report()
    sms.delete_student("S002")
    sms.generate_report()


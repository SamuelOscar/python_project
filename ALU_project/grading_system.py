#!/usr/bin/python3
class Assignment:
    def __init__(self, name, category, grade, weight):
        self.name = name
        self.category = category.upper()
        self.grade = float(grade)
        self.weight = float(weight) / 100  # Convert percentage to decimal
        self.weighted_grade = self.grade * self.weight
    
    def __str__(self):
        return f"{self.name}\t{self.category}\t{self.grade}\t{self.weight*100}\t{self.weighted_grade:.1f}"


class GradeCalculator:
    def __init__(self):
        self.assignments = []
        self.formative_total = 0
        self.summative_total = 0
        self.total_weight = 0
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        if assignment.category == "FA":
            self.formative_total += assignment.weighted_grade
        elif assignment.category == "SA":
            self.summative_total += assignment.weighted_grade
        self.total_weight += assignment.weight
    
    def calculate_gpa(self):
        total_grade = self.formative_total + self.summative_total
        # Convert percentage to GPA (5-point scale)
        if total_grade >= 90:
            return 5.0
        elif total_grade >= 80:
            return 4.0
        elif total_grade >= 70:
            return 3.0
        elif total_grade >= 60:
            return 2.0
        else:
            return 1.0
    
    def determine_pass_fail(self):
        # Assume passing is 60% average for both categories
        formative_avg = self.formative_total / sum(a.weight for a in self.assignments if a.category == "FA") * 100 if any(a.category == "FA" for a in self.assignments) else 100
        summative_avg = self.summative_total / sum(a.weight for a in self.assignments if a.category == "SA") * 100 if any(a.category == "SA" for a in self.assignments) else 100
        
        pass_formative = formative_avg >= 60
        pass_summative = summative_avg >= 60
        
        if pass_formative and pass_summative:
            return "Pass"
        else:
            return "Fail and Repeat"
    
    def display_results(self):
        print("\nAssignment\tCategory\tGrade (%)\tWeight\tWeighted Grade")
        print("-" * 70)
        for assignment in self.assignments:
            print(assignment)
        
        print("\nCategory-wise Totals:")
        print(f"Formatives ({sum(a.weight*100 for a in self.assignments if a.category == 'FA'):.0f})\t\t\t{self.formative_total:.1f}")
        print(f"Summatives ({sum(a.weight*100 for a in self.assignments if a.category == 'SA'):.0f})\t\t\t{self.summative_total:.1f}")
        
        gpa = self.calculate_gpa()
        print(f"\nGPA\t{gpa:.3f}")
        
        status = self.determine_pass_fail()
        print(f"\nResult: {status}")


def get_valid_input(prompt, input_type=float, min_val=0, max_val=100):
    while True:
        try:
            value = input_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Grade Generator Calculator")
    print("=" * 50)
    print("This program helps you understand how your assignment grades contribute to your final course grade.\n")
    
    calculator = GradeCalculator()
    
    while True:
        print("\nEnter assignment details (or type 'done' to finish):")
        name = input("Assignment name: ")
        if name.lower() == 'done':
            if not calculator.assignments:
                print("Please enter at least one assignment.")
                continue
            break
        
        category = input("Category (FA for Formative, SA for Summative): ").upper()
        while category not in ["FA", "SA"]:
            print("Invalid category. Please enter FA or SA.")
            category = input("Category (FA for Formative, SA for Summative): ").upper()
        
        grade = get_valid_input("Grade obtained (0-100): ", float, 0, 100)
        weight = get_valid_input("Weight of assignment (0-100): ", float, 0, 100)
        
        # Check if adding this weight would exceed 100%
        current_total_weight = calculator.total_weight * 100 + weight
        if current_total_weight > 100:
            print(f"Warning: Total weight would be {current_total_weight}%. Maximum allowed is 100%.")
            continue
        
        assignment = Assignment(name, category, grade, weight)
        calculator.add_assignment(assignment)
        
        # Check if we've reached 100% weight
        if calculator.total_weight * 100 >= 100:
            print("\nTotal weight has reached 100%. No more assignments can be added.")
            break
    
    calculator.display_results()


if __name__ == "__main__":
    main()

if __name__ == '__main__':
    name = input("Enter value")
    class_name = input("Enter class name")
    score = int(input("Enter score"))
    
    score_percentage = (score/100) * 100
    
    if score >= 80:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'D'
        
    is_male = input("Are you male (0 = Male, 1 = Female)")
    
    headers = ['Name', 'Student ID', 'Score', 'Grade']
    gui_detail = []
    
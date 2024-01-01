def get_grade(score):
    if score >= 80:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'D'
        
    return grade

def data_is_blank(datas):
    for data in datas:
        if data == '':
            return True
    return False

if __name__ == '__main__':
    name = input("Enter value")
    class_name = input("Enter class name")
    score = input("Enter score")
    is_male = input("Are you male (0 = Male, 1 = Female)")
    
    is_blank = data_is_blank([name, class_name, score])
    if is_blank:
        print("Some Entry is not fill in!")
        quit()
        
    score = int(score)
    score_percentage = (score/100) * 100
    
    grade = get_grade(score)
    
    headers = ['Name', 'Student ID', 'Score', 'Grade']
    gui_detail = []

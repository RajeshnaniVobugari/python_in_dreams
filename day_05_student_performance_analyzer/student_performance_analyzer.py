name = input('Enter the your name : ')
number_of_subjects = int(input('Enter the number of subjects : '))



def grade_sheet(name, count_to_monitor):
    mark_dict = {}

    for i in range(1,count_to_monitor+1):
        subjects = input(f'Enter the subject {i} : ').lower()
        marks = int(input(f'Enter the marks secured in {subjects} : '))
        if marks > 100 or marks < 0:
            print('Marks should not be greater than 100 and less than 0')
            return False

        mark_dict[subjects] = marks

    marks_list = list(mark_dict.values())

    average_marks = sum(marks_list) / len(marks_list)

    result = 'Pass' if average_marks > 30 else 'Fail'

    if result == 'Pass':
        if average_marks>= 80:
            grade = 'A'

        elif average_marks >= 50:
            grade = 'B'

        elif average_marks >= 30:
            grade = 'C'
    else:
        grade = 'F'

    grade_sheet_dict = {
        'name' : name,
        'Marks_list' : marks_list,
        'Grade' : grade,
        'Average' : average_marks,
        'Status' : result
    }

    print(grade_sheet_dict)

grade_sheet(name, number_of_subjects)




    
    
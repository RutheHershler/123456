import datetime
import  io





from Students import StudentsArr
from Card import card
from Bill import bill
print("------success????----------")
b=bill()
s=StudentsArr()
c=card()
studentOrTeacher=0
print("ברוכים הבאים לתוכנת איחורית!")
select=input("ליציאה מהתוכנה הקש exite, להמשך הקש enter")
while select!="exite":
    studentOrTeacher=input("מורה הקישי 1 , תלמידה הקישי 2")
    if studentOrTeacher=="2":
        nameOfLateStudent=input("נא רשמי את שמך")
        s.find_student(nameOfLateStudent)
        # timeOfLate=input("נא הכניסי את השעה")
        # dateOfLate=input("נא הכניסי תאריך")
        num = s.return_my_lates(nameOfLateStudent)
        # print("nummmmm", int(num))
        s.add_late_for_student(nameOfLateStudent)
        # c.check_if_need_newcard()
        if s.num_of_lates(nameOfLateStudent):
            c.coins()
            c.print_card(nameOfLateStudent)
            # b.new_bill(nameOfLateStudent,num)

    elif studentOrTeacher=="1":
        selectAction=input("1-לקבלת רשימת הבנות שלא איחרו כלל , 2- לקבלת מערך התלמידות והכיתות, 3-לקבלת הכיתה עם הכי הרבה איחורים")
        if selectAction=="1":
            s.min_late()
        elif selectAction=="2":
            numclass=input("כניסי שם הכיתה /a/b/c")
            if numclass=="a" or numclass=="b" or numclass=="c":
                s.get_students_names_in_class(numclass)
        elif selectAction=="3":
            s.maxlateclass()
        else:
            continue
    else:
        """להחזיר כאן שגיאה"""
        continue

# # print("----")



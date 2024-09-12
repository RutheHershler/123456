import datetime
class Student:
    """פעולה בונה לתלמידה"""
    def __init__(self,name,classname,lateNum):
        self.name=name
        self.late = {
            "classname":classname,
            "date": datetime.date,
            "time": datetime.time,
            "lateNum": lateNum
        }
        print("name",self.name,"late",self.late)

"""מילון תלמידות"""
class StudentsArr:
    def __init__(self):
        self.dictstudent = [
            Student(name="rut",classname="a",lateNum=5),
            Student(name="shoshana", classname="b",lateNum=0),
            Student(name="rachel", classname="b",lateNum=9),
            Student(name="bella", classname="a",lateNum=0),
            Student(name="naama", classname="c",lateNum=0)
        ]

    def add_late_for_student(self,name):
        """פונקציה המעדכנת את האיחור"""
        for i in self.dictstudent:
            if name==i.name:
                i.late["date"] = datetime.date
                i.late["time"] = datetime.time
                i.late["lateNum"]=i.late["lateNum"]+1
                # print(i.late["lateNum"]+1)
                print("----------now------------")
                print(i.late["date"])
                # print(i.late["date"], i.late["time"])
                print("finish")
                # print(i.late)
                # x=i.late["lateNum"]
                # check_if_need_newcard(x)


    def num_of_lates(self,name):
        """פונקציה הבודקת האם צריך לקנות כרטיסיה """
        for i in self.dictstudent:
            if name == i.name:
                if i.late["lateNum"]==10:
                    i.late["lateNum"]=0
                    return True
        return False


    def get_students_names(self):
        """מחזירה את מערך התלמידות"""
        print("i am in get_students")
        print([item.name for item in self.dictstudent])
        return [item.name for item in self.dictstudent]

    def get_students_names_in_class(self,classNum):
        """מחזירה את מערך התלמידות"""
        for i in self.dictstudent:
            if i.late["classname"]==classNum:
                print(i.name)


    """בס"ד עובד מושלם!!"""

    def min_late(self,):
        """פונקציה המחזירה את שמות הבנות שלא אחרו"""
        # for item in self.dictstudent:
        print([item.name for item in self.dictstudent if item.late["lateNum"]==0])

    def find_student(self,name):
        """להוסיף שגיאה אם לא נמצא"""
        flag=True
        """פונקציית מציאת תלמידה"""
        """להוסיף כאן גנרטור yeld"""
        for i in self.dictstudent:
            if name==i.name:
                flag=True
                print(name," found!")
                return flag
                break
            else:
                flag=False
                #continue
        if flag==False:
            print(name, "not found!")
            return  False

    def find_student22(self, name):
        """להוסיף שגיאה אם לא נמצא"""
        print("i am here")
        for i in self.dictstudent:
            print("i am here2")
            try:
                print("i am here3")
                if name == i.name:
                    flag = True
                    print(name, " found!")
                    flag = True
                    return flag
            except Exception as e:
                print("ppppppppppppppppppppppppppppppp")
                print(name, "not found!".format(e))
        """פונקציית מציאת תלמידה"""
        """להוסיף כאן גנרטור yeld"""


    def maxlateclass(self):
        """מחזיר את הכיתה עם הכי הרבה איחורים"""
        max=0
        ii=0
        dictclass={"a":0,"b":0,"c":0}
        for i in self.dictstudent:
            p=i.late["classname"]
            dictclass[p]=dictclass[p]+i.late["lateNum"]
        for i in dictclass:
            if dictclass[i]>max:
                ii=i
                max=dictclass[i]
        print(f"class:{ii}  max:{max}")

    def return_my_lates(self,name):
        for i in self.dictstudent:
            if name==i.name:
                late=i.late["lateNum"]
                print(late)
                return late+1

    def generator(self,):
        for i in self.dictstudent:
            yield print(i .name)
            yield f'second yield {i}'
            yield print(i .late)

class bill:

    def __init__(self):
        self.i=1

    def new_bill(self,name,time,date,num):
        newbill1=open(f"C:/תכנות/שנה ב/PytonFinalPriject/Bills/lateOff{name}{self.i}.txt" ,"w")
        newbill1.write(f"האיחור של: {name}\n")
        newbill1.write(f"      שעה: {time} \n")
        newbill1.write(f"   תאריך : {date}  \n ")
        newbill1.write(f" מספר איחור :{num}\n")
        self.i=self.i+1
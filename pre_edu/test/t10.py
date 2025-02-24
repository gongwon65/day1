class Calculator:
    def __init__(self,num_list):
        self.num_list=num_list
    
    def sum(self):
        result=0
        for num in self.num_list:
            result += num
        return result
    
    def avg(self):
        return self.sum() / len(self.num_list)
        

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
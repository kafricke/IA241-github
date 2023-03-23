'''
lec 9
define class
'''
import lec8

import numpy 

print(numpy)

print(lec8.cal_abs(-9))

def report_maker(input):
    
    return input 
    
class car:
    maker = 'toyota'
    
   # def report_maker(self):
        
     #   return self.maker 

    def __init__(self,input_model):
        self.model = input_model
        
    def report(self):     
        return self.maker,self.model
        
my_camry = car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())
#my_highlander = car('highlander')
#print(my_highlander.maker)
#print(my_highlander.model)

my_camry.maker='Ford'
print(my_camry.report())
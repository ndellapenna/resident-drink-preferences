#******************************************************************************
# beverages.py
#******************************************************************************
# Name: Nadia Della Penna
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#none
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
##Any comment line that features two hashtags was personally used
#during the debugging process.

import math
import matplotlib.pyplot as plt

class Resident:
    
    def __init__(self, x, y, b): #initializing resident class method 
        self._xval = x #x-coordinate
        self._yval = y #y-coordinate
        self._bev = b #resident beverage preference 

    def distance (self, x_prime, y_prime): 
        x_c = self._xval - x_prime #distance from the resident in x-direction
        y_c = self._yval - y_prime #distance from resident in y-direction
        
        return math.sqrt((x_c)**2 + (y_c)**2) #distance formula
    

#This method below is used for processing our general data file.
def process_file(data_file_obj): 
                                
    resident_pref = []
    for line in data_file_obj:
        #The general idea is to float the coordinate elements in each line
        #since our distance formula could potentially yield a rational number. 
        resident_info = line.split()
        resident_info[0] = float(resident_info[0])
        resident_info[1] = float(resident_info[1])
        ##print(resident_info)
        resident_pref.append(resident_info) 
        
    return resident_pref #x-coordinate, y-coordinate, pepsi/coke preference

###########################################################      

def main():   
    survey_data = open("my_surveydata.txt", "r")   
    res_data = process_file(survey_data)
##    print(res_data)
    user_x = float(input("Enter x-coordinate between -4.0 and 4.0: "))
    user_y = float(input("Enter y-coordinate between -4.0 and 4.0: "))
    
    count_c = 0 #Program will keep track of number of coke and pepsi drinkers
    count_p = 0

    for i in res_data:
        #Below, we will find the distance between user input coordinates
        #and resident data coordinates        
        org_res_dist = Resident(i[0],i[1],i[2]).distance(user_x, user_y)
        
        if org_res_dist <= 1: #if the distance is within a 1 mile radius...
            if i[2]== "Coke": #if the resident data preference is Coke...
                plt.scatter(i[0],i[1], marker= "o", color = "r")
                count_c += 1 #...then we add 1 to our count for Coke
            else: #else, we will assume their drink preference is Pepsi
                plt.scatter(i[0],i[1], marker = "o", color = "b")
                count_p += 1 #... and here we will add 1 to our Pepsi count
    plt.scatter(user_x, user_y, marker = "*", color = "g", )            
    plt.show()
    print("""\nWithin a 1 mile radius from x = {0} and y = {1}:
There are {2} coke drinkers and {3} pepsi drinkers.""".format(user_x, user_y, count_c, count_p))            
    
    survey_data.close() 
###########################################################    
main()

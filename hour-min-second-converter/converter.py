"""
    this program will take the number 
    of seconds from the user and convert
    it to mins and hours 
"""
# getting number of seconds 
numberOfSeconds = int(input('please enter number of seconds : ')) 

#converting to hours 
hours = numberOfSeconds // 3600 

#converting to mins 
mins = (numberOfSeconds % 3600) // 60 

#converting to seconds 
seconds =  (numberOfSeconds % 3600) % 60

print(f"{hours}::{mins}::{seconds}") 

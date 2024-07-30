"""
    this is a simple program that making a simple operation for
    calculating the amount of money that you will have after some years 
    see the equation image 
    
"""

# taking the future value that the user want to have after a few years 
futureMoney = float(input("please enter amount of money that you want to have after a few years : "))

# taking the annual interst rate 
annualInterstRate = float(input("please enter amount of annual interst rate that you have in your country : "))

# taking the years that the user want his money be save
years = int(input("please enter amount of years that you want your money been save : "))

# making operation using equation to display how much he need to deposit today 
deposit =  futureMoney / (1 + annualInterstRate) ** years

print(f"the money that you want to have in future : \
{futureMoney}$\nannual interst rate : {annualInterstRate}\n\
years of deposit : {years}\nyou need to deposit : {deposit}$")


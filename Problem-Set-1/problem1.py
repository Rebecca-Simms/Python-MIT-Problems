
current_savings = 0.0

r = 0.04

annual_salary = float(input("What is your annual salary? "))

portion_saved = float(input("Enter a number between 0.0 and 1.0 to represent what portion of your salary you want to be saved: "))

total_cost = float(input("What is the cost of your dream home? "))

portion_down_payment = total_cost * 0.25

monthly_salary = annual_salary/12

monthly_savings = monthly_salary * portion_saved

numMonths = 0

while current_savings < portion_down_payment:
	current_savings += monthly_savings + (current_savings * (r / 12))
	numMonths += 1
print("The number of months it will take is ", numMonths)

 

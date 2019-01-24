def partc(portion_saved, annual_salary):

	current_savings = 0.0
	r = 0.04 
	total_cost = 1000000
	portion_down_payment = total_cost * 0.25
	monthly_salary = annual_salary/12
	monthly_savings = monthly_salary * portion_saved
	numMonths = 0
	semi_annual_raise = 0.07

	while current_savings < portion_down_payment:
		numMonths += 1	
		current_savings += (annual_salary / 12)*portion_saved + (current_savings * (r / 12))	
		if numMonths % 6 == 0:
                	annual_salary = annual_salary * (1 + semi_annual_raise)
	return(numMonths)

annual_salary = float(input("What is your annual salary? "))

epsilon = 0.01
high = 1.0
low = 0.0
guess = (high + low) / 2

test = partc(guess, annual_salary)

steps = 0

while test != 36:
	if test > 36:
		low = guess
	elif test < 36:
		high = guess
	guess = (high + low) / 2
	steps += 1
	test = partc(guess, annual_salary)

print("You need to save ", guess, "% of your salary.")
print("It took ", steps, "steps.")

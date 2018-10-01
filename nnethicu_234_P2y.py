#-------------------------------------------------------------------------------
# Name: <FILL IN YOUR NAME>
# Project 2
# Due Date: 12/31/1999
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, projects are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

# this time, the template does not have as much guidance - please
# look at at the actual project specification for the rules and
# meanings of each function. You can modify any part of the template
# code to get the job done (abiding by the project's rules). For
# instance, you might want a different start value, or to use multiple
# return statements. This template is only offered in order to help
# you get started, it is not truly required in any sense for the
# project. The function and parameter names must remain the same (e.g.,
# discount and age/major/is_in_military/gpa), but you can use any names you want
# inside of the functions (indented).

def discount(age, major, is_in_military, gpa):
	if age >= 65:
		ans = 'True'
	elif major =='Computer Science' and gpa >= 3.5:
		ans = 'True'
	elif is_in_military == True:
		ans = 'True'
	else:
		ans = 'False'
	return ans
def calculate_cost(plan, num_minutes, num_text):

	if plan == 'Basic':
		minutes_test = num_minutes - 100
		text_test = num_text - 10000

		if minutes_test  <= 0 and text_test <= 0:
			return  15
		elif minutes_test > 0 and text_test <= 0:
			overage_minutes_cost = minutes_test*1.5
			return  15 + overage_minutes_cost
		elif minutes_text <=  0 and text_test >= 0:
			overage_text_cost = text_test* .75
			return  15 + overage_text_cost
		else:
			return 15 + (1.5*minutes_test) + (.75*text_test)

	elif plan <= "Standard":
		minutes_test = num_minutes - 175
		text_test = num_text - 15000

		if minutes_test <= 0 and text_test <= 0:
			return 20;
		elif minutes_test > 0 and text_test <= 0:
			overage_minutes_cost = minutes_test * 1.25
			return 20 + overage_minutes_cost
		elif minutes_text <= 0 and text_test >= 0:
			overage_text_cost = text_test * .5
			return 20 + overage_text_cost
		else:
			return 20 + (1.25 * minutes_test) + (.5 * text_test)
	elif plan == "Premium":
		minutes_test = num_minutes - 250
		text_test = num_text - 2000

		if minutes_test <= 0 and text_test <= 0:
			return 25;
		elif minutes_test > 0 and text_test <= 0:
			overage_minutes_cost = minutes_test * 1
			return 25 + overage_minutes_cost_cost
		elif minutes_text <= 0 and text_test >= 0:
			overage_text_cost = text_test * .25
			return 25 + overage_text_cost
		else:
			return 25 + (1 * minutes_test) + (.25 * text_test)

def cost_efficient_plan(age, major, is_in_military, gpa, num_minutes,num_text):
	x = discount(age,major,is_in_military,gpa)
	basic_cost = calculate_cost("Basic",num_minutes, num_text)
	standard_cost = calculate_cost("Standard",num_minutes, num_text)
	premium_cost = calculate_cost("Premium", num_minutes, num_text)
	if x == True:
		basic_cost = basic_cost * .8;
		standard_cost  = standard_cost * .8;
		premium_cost = premium_cost * .8;

	if basic_cost < standard_cost and basic_cost < premium_cost:
		return "basic"
	if basic_cost == standard_cost and basic_cost < premium_cost:
		return "standard"
	if basic_cost == premium_cost and basic_cost < standard_cost:
		return "premium"
	if standard_cost < basic_cost and standard_cost < premium_cost:
		return "standard"
	if standard_cost == premium_cost and standard_cost < basic_cost:
		return "premium"
	if premium_cost < basic_cost and premium_cost <standard_cost:
		return "premium"
	if premium_cost == basic_cost and premium_cost == standard_cost:
		return "premium"

y = cost_efficient_plan(25, "Astronomy", False, 3.5, 260, 1500)
print(y)
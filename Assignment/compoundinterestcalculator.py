import math

initial_investment = float(input("Enter Initail Investment: "))

monthly_contribution = float(input("Enter Monthly Contribution: "))

length_of_time = int(input("Enter Years: "))

interest_rate = float(input("Enter Estimated Interest Rate: "))

compound_frequency = int(input("Enter Compound Frequency: "))
interest_rate = interest_rate / 100

compound_frequency = initial_investment * math.pow((1 * interest_rate / compound_frequency), (compound_frequency * length_of_time)) * monthly_contribution * (((math.pow((1 * interest_rate / compound_frequency), (compound_frequency * length_of_time)) - 1) / (interest_rate / compound_frequency)))

print(compound_frequency)
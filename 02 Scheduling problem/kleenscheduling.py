from gurobipy import *

setParam('OutputFlag', 0)
print()

# data
shift = [0, 1, 2, 3, 4, 5]  # shifts
officers = [20, 50, 80, 100, 40, 30]  # minimum requirements

# I have created "shift" and "officers" for length. So if you are going to test this model on some other data you might
# probably have to change the length of both? I tested it on my own data and it works fine.

# Create a new model
m = Model("Scheduling")

# variables
x = m.addVars(len(shift), vtype=GRB.CONTINUOUS, name="shifts")

# Set objective(s)
m.setObjective(x.sum(shift), GRB.MINIMIZE)

# constraints

# this uses the modulus. If you want the specific model, run asgn3.py included in the folder. I verified the answer.
m.addConstrs((x[i] + x[(i + 1) % 6] >= officers[(i + 1) % 6] for i in range(len(shift))))

# Optimize model
m.optimize()
# Print the results
print('The minimum officers required for %s: %g' % (m.ModelName, m.objVal))
for v in m.getVars():
    print('%s = %g officers' % (v.varName, v.x))
print()

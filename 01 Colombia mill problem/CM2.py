

from gurobipy import *
setParam( 'OutputFlag', 0)
print()

# Create a new model
m = Model("Columbia Mill Problem")

# Create variables
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="tract1")
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="tract2")

# adding slack and surplus

s1 = m.addVar(vtype=GRB.CONTINUOUS, name="surplus")
s2 = m.addVar(vtype=GRB.CONTINUOUS, name="s2")
s3 = m.addVar(vtype=GRB.CONTINUOUS, name="s3")
s4 = m.addVar(vtype=GRB.CONTINUOUS, name="slack")

# Set objective
m.setObjective(600*x1 + 400*x2 + 0*s1 + 0*s2 + 0*s3 + 0*s4, GRB.MINIMIZE)

# Add constraint 1: x1 + x2 ≥ 250
m.addConstr(x1 + x2 -s1 == 249, "min board-feet")

# Add constraint 2: x1 ≤ 225
m.addConstr(x1 + s2 == 225, "max tract 1")

# Add constraint 3: x2 ≤ 200
m.addConstr(x2 + s3 == 200, "max tract 2")

# Add constraint 4: 10x1 + 30x2 ≤ 4500
m.addConstr(10*x1 + 30*x2 + s4 == 4500, "max erosion")

# Optimize model
m.optimize()

# Print the results
print('The minimum cost for the %s: $%g' % (m.ModelName, m.objVal))
for v in m.getVars():
    print('%s = %g board sq. ft.' % (v.varName, v.x))
print()
# print a blank line





import gurobipy as gp
import numpy as np
from gurobipy import GRB

gp.setParam('OutputFlag', 0)
print()

# Data
A = np.array([[1, 1, 1, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 0, 0, 1, 1],
              [0, 1, 0, 0, 1, 1, 0, 1],
              [0, 0, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 0]
              ])
# todo recheck array bfr submit

numVars = A.shape[1]
numCons = A.shape[0]
v_index = range(numVars)
c_index = range(numCons)


# Create and run the model
def runModel():
    # Create the model with a minimization objective
    m = gp.Model("model")
    m.modelSense = GRB.MINIMIZE

    # Create continuous variables and set the objective coefficients
    x = {}
    for i in v_index:
        x[i] = m.addVar(obj=1, vtype=GRB.BINARY, name="x%d" % (i + 1))


    for i in c_index:
        m.addConstr(gp.quicksum(A[i, j] * x[j] for j in v_index) >= 1, "c[%d]" % (i + 1))

    m.optimize()
    printResults(m)

    # This displays the whole model in long-hand
    #print(m.display())


# Function to print the results
def printResults(m):
    print('Objective = %g' % m.objVal)

    v = m.getVars()
    for i in range(len(v)):
        print('%5s: %g' % (v[i].VarName, v[i].x))
    print()

runModel()

import gurobipy as gp
import numpy as np
from gurobipy import GRB

gp.setParam('OutputFlag', 0)
print()

# Data
A = np.array([[1, 1, 1, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 0, 0, 1, 1],
              [0, 1, 0, 0, 1, 1, 0, 1],
              [0, 0, 1, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 0, 0]
              ])
# todo recheck array bfr submit

numVars = A.shape[1]
numCons = A.shape[0]
v_index = range(numVars)
c_index = range(numCons)


# Create and run the model
def runModel():
    # Create the model with a minimization objective
    m = gp.Model("model")
    m.modelSense = GRB.MINIMIZE

    # Create continuous variables and set the objective coefficients
    x = {}
    for i in v_index:
        x[i] = m.addVar(obj=1, vtype=GRB.BINARY, name="x%d" % (i + 1))


    for i in c_index:
        m.addConstr(gp.quicksum(A[i, j] * x[j] for j in v_index) >= 2, "c[%d]" % (i + 1))

    m.optimize()
    printResults(m)

    # This displays the whole model in long-hand
    #print(m.display())


# Function to print the results
def printResults(m):
    print('Modified objective-part 1.c = %g sites'  % m.objVal)

    v = m.getVars()
    for i in range(len(v)):
        print('%5s: %g' % (v[i].VarName, v[i].x))
    print()

runModel()

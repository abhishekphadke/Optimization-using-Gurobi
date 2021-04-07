
import gurobipy as gp
import numpy as np  # import numpy to use quicksum
from gurobipy import GRB

gp.setParam('OutputFlag', 0)  # mute solver meta-info
print()  # print a blank line

# Data
A = np.array([[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],#* array checked
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],#*
              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#*
              [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],#*
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],#*
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],#*
              [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],#*
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]#*
              ])

ob = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) #Min. Objective function
b = np.array([1, 1, 1, 1, 1, 1, 1, 1]) #constraint RHS
v_index = range(len(ob))
c_index = range(len(b))


# Create and run the model twice
def runModel():
    # Create the Model
    m = gp.Model("model")

    # # The objective is to minimize the total costs
    m.modelSense = GRB.MINIMIZE

    # Create continuous variables and set the objective coefficients
    x = m.addVars(v_index, obj=ob, vtype=GRB.BINARY, name="x")


    for i in c_index:
        m.addConstr(gp.quicksum(A[i, j] * x[j] for j in v_index) >= b[i], "c[%d]" % i)


    print("ROOM PLACEMENT (0 is room 1)")
    x[0].vtype = GRB.BINARY

    m.optimize()
    printResults(m)

    # This displays the whole model in long-hand
    # print(m.display())


# Function to print the results

def printResults(m):
    print('Optimial Camera number = %g' % m.objVal)

    v = m.getVars()
    for i in range(len(v)):
        print('%s: %g' % (v[i].VarName, v[i].x))
    print()

runModel()

# Data
A = np.array([[1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],#* array checked
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],#*
              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#*
              [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],#*
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],#*
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],#*
              [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],#Corresponding number of cameras for this room is changed to 2
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]#*
              ])

ob = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) #Min. Objective function
b = np.array([1, 1, 1, 1, 1, 1, 2, 1]) #constraint RHS #camera number change is reflected here for q21 subsection c &d
v_index = range(len(ob))
c_index = range(len(b))


# Create and run the model twice
def runModel():
    # Create the Model
    m = gp.Model("model")

    # # The objective is to minimize the total costs
    m.modelSense = GRB.MINIMIZE

    # Create continuous variables and set the objective coefficients
    x = m.addVars(v_index, obj=ob, vtype=GRB.BINARY, name="x")


    for i in c_index:
        m.addConstr(gp.quicksum(A[i, j] * x[j] for j in v_index) >= b[i], "c[%d]" % i)


    print("ROOM PLACEMENT (0 is room 1)")
    x[0].vtype = GRB.BINARY

    m.optimize()
    printResults(m)

    # This displays the whole model in long-hand
    # print(m.display())


# Function to print the results

def printResults(m):
    print('Optimial Camera number with revised constraints = %g' % m.objVal)

    v = m.getVars()
    for i in range(len(v)):
        print('%s: %g' % (v[i].VarName, v[i].x))
    print()

runModel()

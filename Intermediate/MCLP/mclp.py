import sys
import gurobipy as gp
import numpy as np
from gurobipy import GRB
from scipy.spatial.distance import cdist
import plot
import readDataFiles
gp.setParam('OutputFlag', 0)
def Read_Problem(file): #*
    try:
        if file[-3:].lower() == 'dat':
            siteData = readDataFiles.readDAT(file)
        elif file[-3:].lower() == 'tsp':
            siteData = readDataFiles.readTSP(file)
    except IOError:
        print('Error reading file')
        raise
    return siteData

def ComputeCoverageMatrix(SD, siteData):
    xySites = siteData[:, [1, 2]]
    distMatrix = cdist(xySites, xySites, 'euclidean')
    dm = distMatrix <= SD
    matrix = [np.nonzero(t)[0] for t in dm]
    return matrix

def model(mclp, p, cover_rows, g, numSites): #*
    x = mclp.addVars(numSites, vtype=(GRB.BINARY), obj=0, name='x')
    y = mclp.addVars(numSites, vtype=(GRB.BINARY), obj=g, name='y')
    d_index = range(numSites)
    for i in d_index:
        mclp.addConstr(gp.quicksum((x[j] for j in cover_rows[i])) - y[i] >= 0)
    mclp.addConstr(gp.quicksum((x[j] for j in d_index)) == p)
    mclp.modelSense = GRB.MAXIMIZE  # objective-Max
    mclp.update()
    print('Number of variables & constraints = %d & %d respectively' % (mclp.numintvars, mclp.numconstrs))  # prints V&C
    return x

def MCLP(file, SD, p): #*
    siteData = Read_Problem(file)
    numSites = siteData.shape[0]
    g = siteData[:, 3]
    matrix = ComputeCoverageMatrix(SD, siteData)
    mclp = gp.Model('MCLP solver')
    c = model(mclp, p, matrix, g, numSites)
    mclp.optimize()
    objective = mclp.objVal
    displaySolution(c, p, objective, g, numSites, siteData)

def displaySolution(x, p, objective, g, numSites, siteData): #*
    print('Total demands = %g ' % sum(g))
    print('SD = %g' % SD)  # input 2
    print('Facilities input given = %g' % p)  # input 3
    print('Demands covered by solver = %g' % (objective))  # insight 1
    print('Percentage demands = %g' % (objective / sum(g) * 100))  # insight 2
    print('***************')
    for i in range(numSites):
        if x[i].x == 1.0:  # plot correlation
            print('Site selected- %g' % siteData[(i, 0)])
    plot.plotSolution(siteData, x, range(numSites), SD)
# argument length input and error
if len(sys.argv) < 4: #*
    print('Insufficient arguments\n')
    sys.exit(0)
file = '../data/' + sys.argv[1]
SD = int(sys.argv[2])
p = int(sys.argv[3])
MCLP(file, SD, p)

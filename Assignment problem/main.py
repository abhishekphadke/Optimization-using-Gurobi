from gurobipy import *

try:
    center = ['plano', 'nashville', 'flagstaff', 'springfield', 'boulder']
    zone = ['la', 'chicago', 'columbus', 'atlanta', 'newark', 'kansas', 'denver', 'dallas']

    # data
    network, cost = multidict({
        ('plano', 'la'): 70,
        ('plano', 'chicago'): 47,
        ('plano', 'columbus'): 22,
        ('plano', 'atlanta'): 53,
        ('plano', 'newark'): 98,
        ('plano', 'kansas'): 21,
        ('plano', 'denver'): 27,
        ('plano', 'dallas'): 13,

        ('nashville', 'la'): 75,
        ('nashville', 'chicago'): 38,
        ('nashville', 'columbus'): 19,
        ('nashville', 'atlanta'): 58,
        ('nashville', 'newark'): 90,
        ('nashville', 'kansas'): 34,
        ('nashville', 'denver'): 40,
        ('nashville', 'dallas'): 26,

        ('flagstaff', 'la'): 15,
        ('flagstaff', 'chicago'): 78,
        ('flagstaff', 'columbus'): 37,
        ('flagstaff', 'atlanta'): 82,
        ('flagstaff', 'newark'): 111,
        ('flagstaff', 'kansas'): 40,
        ('flagstaff', 'denver'): 29,
        ('flagstaff', 'dallas'): 32,

        ('springfield', 'la'): 60,
        ('springfield', 'chicago'): 23,
        ('springfield', 'columbus'): 8,
        ('springfield', 'atlanta'): 39,
        ('springfield', 'newark'): 82,
        ('springfield', 'kansas'): 36,
        ('springfield', 'denver'): 32,
        ('springfield', 'dallas'): 45,

        ('boulder', 'la'): 45,
        ('boulder', 'chicago'): 40,
        ('boulder', 'columbus'): 29,
        ('boulder', 'atlanta'): 75,
        ('boulder', 'newark'): 86,
        ('boulder', 'kansas'): 25,
        ('boulder', 'denver'): 11,
        ('boulder', 'dallas'): 37,

    })

    m = Model('assignment')

    # Add variables
    x = m.addVars(network, name='network diagram')

    # center constraints
    center = m.addConstrs((x.sum(c, '*') <= 3 for c in center), 'center')

    # zone constraints
    zone = m.addConstrs((x.sum('*', z) == 1 for z in zone), 'zone')

    # Set objective function
    m.setObjective(x.prod(cost), GRB.MINIMIZE)

    # Solve model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    print("Final answer is in thousands")

    print('obj: %g' % m.objVal)



except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

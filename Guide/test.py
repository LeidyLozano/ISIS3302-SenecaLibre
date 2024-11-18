import pyomo.environ as pyo
from highspy import Highs

model = pyo.ConcreteModel()
model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)
model.obj = pyo.Objective(expr=model.x[1] + model.x[2])

model.con1 = pyo.Constraint(expr=2 * model.x[1] + model.x[2] <= 3)
model.con2 = pyo.Constraint(expr=model.x[1] + 3 * model.x[2] <= 5)

opt = pyo.SolverFactory('appsi_highs')
results = opt.solve(model)

model.display()
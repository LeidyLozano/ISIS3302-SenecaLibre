from pyomo.environ import *


# Create model object
model = ConcreteModel()

# Declare decision variables
model.l = Var(within=NonNegativeReals)
model.g = Var(within=NonNegativeReals)

# Declare objective function
model.maximizeProfit = Objective(expr=200 * model.l + 300 * model.g,
sense=maximize)

# Declare constraints
# Farmer Brown has only 100 hours
model.LaborConstraint = Constraint(expr=3 * model.l + 2 * model.g <= 100)
# He only has $120 for medical
model.MedicalConstraint = Constraint(expr=2 * model.l + 4 * model.g <= 120)
# He only has 45 acres
model.LandConstraint = Constraint(expr=model.l + model.g <= 45)

# Show all available solvers
print(SolverFactory.__dict__["_cls"].keys())
print("")

# Test for availability of solver
my_solver = "highs"
if SolverFactory(my_solver).available():
    print("Solver " + my_solver + " is available.")
else:
    print("Solver " + my_solver + " is not available.")

optimizer = SolverFactory(my_solver)
optimizer.solve(model, options={"threads": 4}, tee=True)

model.display()
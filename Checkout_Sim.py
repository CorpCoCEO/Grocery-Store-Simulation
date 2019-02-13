import numpy as np
from matplotlib import pyplot as plt

class Customer():
    def __init__(self):
        self.checkout_time = int(np.random.chisquare(3))


class Register():
    def __init__(self):
        self.occupied = False
        self.total_wait = 0
        self.current_wait = 0
        self.line = []

trials = 10
end_time = 60
wait_times_all = []

for i in range(trials):
    register = Register()
    wait_times = []
    gen_customer = 0
    for gen in range(end_time):
        # Generates a customer every 4 generations
        if gen_customer == 0:
            customer = Customer()
            register.line.append(customer)
            register.total_wait += customer.checkout_time
            gen_customer = int(np.random.chisquare(3))
            
        # Downticks current customer wait time, and removes them if
        # they're done
        if register.occupied == True:
            if register.current_wait <= 0:
                register.current_wait = 0
                register.occupied = False
            
        # Adds next customer in line if register is empty
        if register.occupied == False and len(register.line) != 0:
            register.occupied = True
            customer_added = register.line[0]
            register.current_wait = customer_added.checkout_time

        # Saves the current total wait time and downticks the total
        # wait time
        wait_times.append(register.total_wait)
        if register.total_wait > 0:
            register.total_wait -= 1
        if gen_customer > 0:
            gen_customer -= 1

    # Appends simulation results to the list of results
    wait_times_all.append(wait_times)

# Plots results of each simulation
for sim in wait_times_all:
    plt.plot(range(60), sim)
plt.title('Wait Times at a Register')
plt.xlabel('Minutes After Lane Opens')
plt.ylabel('Wait Time of Last Person in Line (in Minutes)')

plt.show()



        
        

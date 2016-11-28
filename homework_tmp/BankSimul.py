'''
input specification 

list of following : 

nnumber of banker
number of customer 
(customer 1 arrive time, customer 1 required tiume)
....
(customer n arrive time, ...)

output specification 

customer 1 go to banker at x, leaves bank at x'
.... 
customer n go to banker at z, leaves bank at z' 
total time : z'-x 
'''

'''
input example 
[3, 5, 
(0, 3), 
(1,5), 
(4, 10), 
(5, 1),
(7, 3)]

output example 
customer 1 go to banker at 0, leaves bank at 3
customer 2 go to banker at ...

'''

class Banker:
	def __init__(self, id_num):
		self.id_num = id_num 
	def __str__(self):
		return str(self.id_num)

class Customer:
	def __init__(self, t_arrive, t_need):
		self.t_arrive = t_arrive
		self.t_need = t_need 

class BankSimulation:
	def __init__(self, banker_num, customer_list):
		self.banker_num = banker_num 
		self.customer_list = customer_list

	def simulate(self):
		for customer in self.customer_list:
			print(customer.t_arrive, customer.t_need)
			#time = 0
		tick = 0

		while(True): 
			if True: # if all customers are processed 
			 	return
			else: 
				if True: # if there is an empty banker
					pass # 온 시간이 적은 순서대로 은행원 할당  
				else: # if there is no empty banker
					pass # tick += 1

			

if __name__ == '__main__':
	customer_list = [Customer(0,3), 
					Customer(1,5), 
					Customer(4,10), 
					Customer(5,1),
					Customer(7,3)]

	BankSimulation(3,customer_list).simulate()

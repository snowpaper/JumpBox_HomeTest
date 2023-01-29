# Distribute all this work as evenly as possible onto servers.
def distribute(serv, job):
	count = 0
	list_serv = list()
	for serv in range(serv, 0, -1):
		job = int(job - count)
		# roundDown value count
		count = int(job / serv)

		# Create Jobs list for server
		list_jobs = list(range(job-count, job))

		# Add Jobs list to each server
		list_serv.append(list_jobs)
	list_serv.sort()
	return list_serv

# Input number of Servers and Jobs.
if __name__ == "__main__":
	x = int(input("How many Servers ? : "))
	y = int(input("How many Jobs ?    : "))
	print("distribute(",x,",",y," )#=> ",distribute(x,y))

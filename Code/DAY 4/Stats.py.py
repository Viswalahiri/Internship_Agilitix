class Data:
	def __init__(self, p):
		self.p = p

	def variance(self):
		self.variance = 0
		for i in self.p:
			self.variance +=(i-(sum(self.p)/len(self.p)))**2
		print(self.variance/(len(self.p)-1))

	def mean(self):
		print(sum(self.p)/len(self.p))

	def sd(self):
		self.variance = 0
		for i in self.p:
			self.variance +=(i-(sum(self.p)/len(self.p)))**2
		print((self.variance/(len(self.p)-1))**0.5)

	def median(self):
		self.p = sorted(self.p)
		if(len(self.p)%2 == 0):
			print((self.p[(len(self.p)-1)//2]+self.p[((len(self.p)-1)//2) + 1]) / 2)
		else:
			print(self.p[len(self.p)//2])

	def quartile(self,percentile):
		self.p = sorted(self.p)
		self.percentile = percentile
		self.index = (self.percentile/100) * (len(self.p)-1)
		# self.remainder = self.index - round(self.index)
		#print(self.remainder, self.index)
		print("__________")
		print(self.index)
		print(self.p[round(self.index)])# + self.remainder*(self.p[round(self.index)+1]) - self.p[round(self.index)]) 



if __name__ == "__main__":
# 1240 1200 1010 940 1100 1450 1750 2000 2100 1020 1500 2010 2750 3030 1400 750 1200 1100 1500 3510 4500 7000
	p = list(map(int,input().split()))
	q = [i-1500 for i in p]
	Data_Object = Data(p)
	Data_Object_2 = Data(q)
	Data_Object.quartile(25)
	Data_Object.quartile(50)
	Data_Object.quartile(75)
	Data_Object.quartile(99)
	# Data_Object.median()
	# Data_Object.mean()
	# Data_Object.variance()
	# Data_Object_1.sd()
	# Data_Object_2.sd()

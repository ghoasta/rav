#adding commenct to test git

class Dog:
	DOG_TO_HUMAN_YEARS_CONVERSION_FACTOR = 7

	def __init__(self,name,age,breed):
		self.name = name
		self.age = age
		self.breed = breed

	def __str__(self):
		if self.age == 1:
			return f"{self.name} is a {self.breed} and is a year old"
		else:		
			return f"{self.name} is a {self.breed} and is {self.age} years old"

	def age_in_human_years(self):
		return self.age* self.DOG_TO_HUMAN_YEARS_CONVERSION_FACTOR		
#second comment
def main():
	dog1 = Dog("Freddie",1,"King Charles")
	dog2 = Dog("Micky",6,"Greyhound")

	print(dog1)
	print(dog2)
	print("")

	print(f"{dog1}, which is {dog1.age_in_human_years()} in human years. ")
	print(f"{dog2}, which is {dog2.age_in_human_years()} in human years. ")
	print("")
	dog1.age +=1
	dog2.age +=1

	print(dog1)
	print(dog2)

	dog_file = open("dogs.txt","w")
	print(dog1, file=dog_file)
	print(dog2, file=dog_file)
	dog_file.close()


main()	

from Cat import cat
cat1 = cat('Pushistik', 'Male', 12)

print(cat1.get_name(), cat1.get_age(), cat1.get_gender())

class Dog(cat):
    def get_pet(self):
        return self.name, self.age

dog1 = Dog("hulio", 'male', 12)
print(dog1.get_pet())
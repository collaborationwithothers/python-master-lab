class Dog(object):
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def set_age(self, age):
        if( age < 0):
            raise ValueError("Age cannot be negative")
        self.age = age

my_dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
print(f"My dog's name is {my_dog.name}, age is {my_dog.age}, and breed is {my_dog.breed}.")

my_dog.set_age(5)
print(f"My dog's new age is {my_dog.age}.")

class VotingPoll(object):
    def __init__(self):
        self.Candidate_A = 0
        self.Candidate_B = 0
        self.Candidate_C = 0
    
    def vote_candidate_a(self):
        self.Candidate_A += 1
    
    def vote_candidate_b(self):
        self.Candidate_B += 1
    
    def vote_candidate_c(self):
        self.Candidate_C += 1

poll = VotingPoll()
poll.vote_candidate_a()
poll.vote_candidate_b()
print(f"Votes for Candidate A: {poll.Candidate_A}")
print(f"Votes for Candidate B: {poll.Candidate_B}")
print(f"Votes for Candidate C: {poll.Candidate_C}")
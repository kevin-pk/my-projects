# python project that involves the random module and oop
# this python project allows 
# the use of user data such as age etc
# compares the start and end time of users
# their will be a total of 3 user at a time, with each user moving on until the fastest user is crowned
# the end time of users will be determined by the random function in the time module
# ideas for moving forward, make it so that random users are selected and pitted against each by the computer's choice
# for now kevin josh and henry are pitted against each other by my doing 
import random
import math

class User():
    def __init__(self,name,age ):
        self.name = name
        self.age = age
        self.time_taken = 0
        
    def print_info(self):
        print(" the user's name is {}, and {} is {} years old".format(self.name,self.name,  self.age))
        pass
    
class timer(User):
    def __init__(self,name,age,):
        super().__init__(name,age,)
        self.correct_answer = 0
        
    def clock(self):
            start_time = 1
            end_time = random.uniform(2,10)
            self.time_taken = end_time - start_time
            print(f"{self.name}'s time taken is {self.time_taken}")
            
    def __lt__(self, other):
        return self.time_taken < other.time_taken 
    
    
    def show_winner(self,kevin, josh, henry):
        while True:
            if kevin < henry and kevin < josh:
                print('kevin is the fastest')
            elif josh < kevin and  josh < henry:
                print('henry is the fastest')
            elif henry < josh and henry < kevin:
                print('henry is the fastest')
                
            break
            
        
        
        
        pass

rounds = 1
kevin = timer('kevin', 19)
josh = timer('josh', 23)
henry = timer("henry", 17)

for i in range(rounds):
    kevin.clock()
    josh.clock()
    henry.clock()
    kevin.show_winner(kevin, josh, henry)



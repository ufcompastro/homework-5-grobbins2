import numpy as np
#code worked on by Grady Robbins (during class)
#probability for 2 people in a room to share the same birthday greater than 50%. how many ppl?

#repeat in loops to find probability
bday_dates = []
bday_counter = 0 
for N_people in range(1,30): #cycle through number of people in room
    kmax = 10000 #accuracy of probability, takes around half a second per loop when kmax = 10000, takes around a minute when kmax = 100000
    bday_counter = 0
    for k in range(0,kmax):
        bday_dates = []
        for i in range(0,N_people):
            bday = np.random.randint(1,366) #calculating random birthdays for amount of people in room                                                                                           
            bday_dates.append(bday)
        res = set([x for x in bday_dates if bday_dates.count(x) > 1]) #code found online to recognize repeat birthdays
        if len(res) >= 1:
            bday_counter +=1
        bday_dates = []
    prob = bday_counter*100/kmax #probability that a birthday is shared in a room
    if prob < 50:
        print("the probability that a birthday will be shared in a room with",N_people,"people is",prob,"%, not enough, so let's keep going.") 
    else: #print statements to follow along and end code when probability is above 50%
         print("the probability that a birthday will be shared in a room with",N_people,"people is",prob,"%, which is above 50%! so we can stop here")
         break
    
    

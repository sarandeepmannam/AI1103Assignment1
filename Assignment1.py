import random
n=1000000 #no of times the experiment is conducted
i=0
p=0 #no of cases favourable for first black ball
#caluclating theoritical probabilities
P1=10/15 #P1 is theoritical probability of selecting first ball as black
P2=9/14 #P2 is theoritical probability of selecting second ball as black given first one is black
P3=P1*P2 #P3 is the reqired probability
print('theoritical probabilityb of selecting first  black ball from urn is :',P1)
print('theoritical probability of taking second ball from the urn given first ball is black is:',P2)
print('theoritical probability of selecting first two balls as black is :',P3)
#caluclating simulated probabilities
while i<n:
  x=random.randint(1,15)#Assume 15 numbers represent 15 balls
  if x<=10:#Assume first 10 numbers represent 10 black balls
    p=p+1
  i=i+1
P_1=p/n
i=0
k=0 #no of cases favorable for second black ball given first is black
while i<n:
  x=random.randint(1,14)#since 1st ball(black) is taken out remaining balls count is 14
  if x<=9:#in that 14 assume 9 black balls represent first 9 numbers 
    k=k+1
  i=i+1
P_2=k/n
m=0#no of cases favorable for first two balls balls to be black
i=0
while i<n:
  x=random.randint(1,15)
  if x<=10: 
   x=random.randint(1,14)
  else:
    x=x
  if x<=9:
     m=m+1
  i=i+1
P_3=m/n
print('simulated probability of taking first black ball is:',P_1)
print('simulated probability of taking second black ball given first ball is black is: ',P_2)
print('simulated probability of taking first two balls as black is:',P_3)
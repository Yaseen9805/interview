name= input("What's your name user?\n")
print("\nWelcome",name,"to the show \n")
Questions= ["Who won Asia Cup 2023?","Who starred in Oppenheimer?","Which recent Indian movie broke records for fastest grossin movie?"]
Options1 =["1.Sri Lanka","2.Africa","3.India","4.Pakistan"]
Options2 =["1.Ryan Gosling","2.Patrick Bateman","3.Andrew Tate","4.Cillian Murphy"]
Options3 =["1.Jawan","2.Khushi","3.Barbie","4.Oppenheimer"]

print("Here's your first Question\n",Questions[0])
print("The Options are :\n",)
for i in Options1:
  print(i)
c=int(input("Enter your option:"))
if c==3:
  print("Congrats you've won 1000 rs\nYou may proceed to the next question")
  print(Questions[1])
  print("The Options are :\n",)
  for i in Options2:
   print(i)
  c=int(input("Enter your option:\n"))
  if c==4:
   print("Congrats you've won 10000 rs\nYou may proceed to the next question")
   print(Questions[2])
   print("The Options are :\n",)
   for i in Options3:
    print(i)
   c=int(input("Enter your option:\n"))
   if c==1:
    print("Congrats you've won 100000 rs\n")
   else:
    print("We're sorry to inform you but unfortunately your answer was wrong\nThe money you are taking home with you is 10000rs")
  else:
    print("We're sorry to inform you but unfortunately your answer was wrong\nThe money you are taking home with you is 1000rs")
else:
 print("We're sorry to inform you but unfortunately your answer was wrong \nBetter luck next year!!")

print("It was nice having you on our show MR",name,)
# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print ('''
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
''')
awser = int(input('la respuestae es = '))

if awser == 1:
 Gryffindor += 1
 Ravenclaw += 1
elif awser == 2:
 Hufflepuff += 1
 Slytherin += 1
else:
  print('eh')

print ('''
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
''')
awser = int(input('la respuestae es = '))

if awser == 1:
 Hufflepuff += 2
elif awser == 2:
 Slytherin += 2
elif awser == 3:
  Ravenclaw += 2
elif awser == 4:
  Gryffindor += 2
else:
  print('eh')

print ('''
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
''')
awser = int(input('la respuestae es = '))

if awser == 1:
 Hufflepuff += 4
elif awser == 2:
 Slytherin += 4
elif awser == 3:
  Ravenclaw += 4
elif awser == 4:
  Gryffindor += 4
else:
  print('eh')

print ('Gryffindor is ', Gryffindor)
print ('Ravenclaw is ', Ravenclaw)
print ('Hufflepuff is ', Hufflepuff)
print ('Slytherin is ', Slytherin)

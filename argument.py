# Positional argument : 
def name(fname,lname):
  print("Name : " , fname+" "+lname)
name("Aye", "Pyae")

#Keyword argument
def name(fname,lname):
  print("Name : " , fname+" "+lname)
name(fname="Aye",lname="Pyae")

#Default argument
def name(fname= 'Aye', lname ='Pyae'):
    print("Name : " , fname+" "+lname)
name()

#receive arg as in dict
def name(**kwargs):
#   print(type(kwargs))
  print("Name : " , kwargs)
name(fname ='Aye Pyae', lname ='Phyo Kyaw')

#receive arg as an array
def name(*argv):
    for res in argv:
        print(res)
name('Aye', 'Pyae', 'Phyo', 'Kyaw')


def name_fun(*name):
  print("My first name :  " + name[0] + name[1])
name_fun('Aye', 'Pyae', 'Phyo', 'Kyaw')


# Hello World program in Python
#http://www.tutorialspoint.com/python/python_date_time.htm
import time
import calendar
import support
    
import Phone


print "Hello World!\n"
dict = {}
dict['one'] = "valor de clave1"
dict[2]     = "valor de clave2"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

print "Soy %s y peso %d kg!" % ('Roi', 21) 

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

list = ['physics', 'chemistry', 1997, 2000];
print "Value available at index 2 : "
print list[2];
list[2] = 2001;
print "New value available at index 2 : "
print list[2];

list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;


ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks
localtime = time.localtime(time.time())
print "Local current time :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

cal = calendar.month(2015, 5)
print "Mayo 2015:"
print cal;

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;
# Now you can call printme function
printme("I'm first call to user defined function!");
printme("Again second call to the same function");   

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return
# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return
# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" );

# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" );
printinfo( name="miki" );

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;
# Now you can call printinfo function
printinfo( 10 );
printinfo( 70, 60, 50 );

# Function definition is here
# ES una LAMBDA
sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;
# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total 


total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;
# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 

# Now you can call defined function that module as follows
support.print_func("Zara")

#importando Phone, tengo estas clases
Phone.Pots()
Phone.Isdn()
Phone.G3()
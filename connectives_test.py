# Attempt to write a self-test program for students learning truth tables
# preliminary to writing something more interesting
# from connectives_test import *
import random
import string

VALUES = [True, False]

#right = "\n    Correct!\n"

#wrong = "\n    Sorry, the answer was'{0}'.\n".format(answer)

def produce_pair():
    global pair
    pair = [random.choice(VALUES), random.choice(VALUES)]

def test_conj():
    produce_pair()
    answer = str(pair[0] and pair[1])
    print "    What is the truth-value of the conjunction '{0} AND {1}'?\n".format(pair[0], pair[1])
    response = raw_input('> ')
    if response == answer:
    	print "\n    Correct!"
    elif string.capitalize(response) == answer:
    	print "\n    Correct!"
    else:
    	print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_disj():
	produce_pair()
	answer = str(pair[0] or pair[1])
	print "    What is the truth-value of the disjunction '{0} OR {1}'?\n".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_cond():
	produce_pair()
	answer = str(not pair[0] or pair[1])
	print "    What is the truth-value of the conditional 'IF {0} THEN {1}'?\n".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)
		
def test_bicond():
	produce_pair()
	answer = str((not pair[0] or pair[1]) and (not pair[1] or pair[0]))
	print "    What is the truth-value of the biconditional '{0} IF AND ONLY IF {1}'?\n".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_neg():
	unit = random.choice(VALUES)
	answer = str(not unit)
	print "    What is the truth-value of the negation 'NOT {0}'?\n".format(unit)
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)



def splash():
	print"""

            T R U T H - F U N C T I O N A L
                 C O N N E C T I V E S             
    _______________________________________________
    |                                             |
    | Test your knowledge of the truth functions! |
    | Quit at any time with CTRL-D.               |
    |                                             |
    | - Adam                                      |
    |_____________________________________________|
    
	"""

splash()

try:
	while True:
		probe = random.randint(0, 4)
		if probe == 0:
			test_conj()
		elif probe == 1:
			test_disj()
		elif probe == 2:
			test_cond()
		elif probe == 3:
			test_bicond()
		elif probe == 4:
			test_neg()

except EOFError:
	print "\n\n    Thanks for playing!\n\n"
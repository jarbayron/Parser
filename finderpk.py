def finder(f = '', spaces='yes', position= 'no'):
    pass

raw = list(filter(None, [elem.strip('\n') for elem in open('3630.txt').readlines()]))

f='8'

integer=[0,1,2,3,4,5,6,7,8,9]
lc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print(f[0].isdigit())





#Objective examples
##'Hi'
##searches two letter words for in order Capital Letter, lowercase letter
##'hi'
##searches two letter words with two lower casse letters
##'Hi5'
##searches word with upper, lower, integere
##'Hi5/'
##searches word with upper lower integer and '/'
##
##SPECIAL consionts
##'*Hi*555/555'
##Searches 'Hi' followed by int,int,int,'/',int,int,int
##
##SPECIAL conditions if you input
##spaces='no'
##seaches regardless if its next ot other things
### position = 'no' gives yout he postion in the list that it was found in at the list

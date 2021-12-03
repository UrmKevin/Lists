#nimed=["Anna","Inna"]
#for i in range(3):
#    nimi=input("Sisesta nimi: ")
#    nimed.append(nimi)

#print(nimed)
##nimed.sort(reverse=True)
##print(nimed)
##nimed.insert(1,input("Sisesta veel nimi: "))
##print(nimed)
#nimed.remove("Anna")
#print(nimed)
#nimed.pop(2)
#print(nimed)
#print(len(nimed))
#a=nimed.count(nimed[1])
#print(a)
# number 1
#index=""
#u=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        index = int(input("Write ur index: "))
#        if 10000<=index<=99999:
#            break
#    except ValueError:
#        print("Invalid input!")
#index=str(index)
#index=list(index)
#u=u[int(index[0])-1]
#print(u)
#if u=="Tallinn" or u=="Narva, Narva-Jõesuu" or u=="Kohtla-Järve":
#    print("Оставайтесь дома!")
#else:
#    print("Носите маски!")

# number 2
#from random import*
#l=[]
#N=randint(2,10)
#for i in range(N):
#    l.append(randint(10,20))
#print(l)
#while 1:
#    try:
#        k=int(input("How many numbers u want to change? "))
#        if k<=N//2:
#            break
#    except ValueError:
#        print("More than",l//2)
#k-=1
#for i in range(k,-1,-1):
#    print(l[i],end="<=>")
#    print(l[N-i-1])
#    x=l.pop(i)
#    l.insert((N-i-1)-1,x)
#    y=l.pop(N-i-1)
#    l.insert(i,y)

#print("Result: ",l)
# number 3
#from random import*
#l=[]
#N=randint(2,10)
#for i in range(N):
#    l.append(randint(1,20))
#print(l)
#max=1
#for element in l:
#    if element>max: 
#        max=element
#        y=l.index(max)
#x=max/N
#l.pop(y)
#l.insert(y,x)
#print(l)

# number 4
#from random import*
#l=[]
#N=randint(2,10)
#for i in range(N):
#    l.append(randint(1,20))
#print(l)
#nl=[]
#for e in l:
#    nl.append(abs(e))
#print(nl.sort())
#print(nl.sort(reverse=True))
#print(nl)

# number 5
#l = ['крот', 'белка', 'выхухоль']
#nl=[]
#max=0
#for i in range(len(l)):
#	x=len(l[i])
#	if x>max:
#		max=x
#for i in range(len(l)):
#	tl=l[i]
#	nl.append(tl.ljust(max,'_'))
#print(nl)

#l = ['крот', 'белка', 'выхухоль']
#nl=[]
#max=0
#for e in l:
#	x=len(e)
#	if x>max:
#		max=x
#for e in l:
#	nl.append(e.ljust(max,'_'))
#print(nl)

#l1=['крот', 'белка', 'выхухоль']
#l2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#l3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#sss=[l1,l2,l3]
#c=0
#for u in sss:
#	print(sss[c])
#	max=0
#	nl=[]
#	for e in sss[c]:
#		x=len(e)
#		if x>max: max=x
#	for e in sss[]:
#		nl.append(e.ljust(max,'_'))
#	print(nl)
#	c+=1

# number 6
name="0s"
gl=["e","u","i","o","a"]
cnt1=0
cnt2=0
while name.isalpha()==False:
    try:
        name=str(input("Name(eng): "))
    except: ValueError
l=list(name)
name=name.lower()
print("Hello, ",name.capitalize(),"!!")
print("You have ",len(l),"letters in name")

dub=[x for x in l if l.count(x)>=1]
dub=list(set(dub))

print(sorted(dub))





















# rock papper scissors
#from random import*
#l=["rock","papper","scissors"]
#name=input("Write your name: ")
#print("1 - ",l[0],", 2 - ",l[1],", 3 - ",l[2])
#p=input("")
#if p == 1 or p == 2 or p == 3:


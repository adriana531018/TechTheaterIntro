import random
Untrustworthy = ["lie"]
stud = ["Always participates in class"]
Extracurricular = ["volunteering"]
Friday = ["Watching movies"]
Study = ["Going to the library regularly"]
Cont= ["Making significant donations to his university"]
successful = ["is extremely talented"]
def academia():
    print("filler")
def ec():
    num = random.randint(0,len(Extracurricular)-1)
    print(Extracurricular[num])
def fri():
   num = random.randint(0,len(Friday)-1)
   print(Friday[num])
def study():
    num = random.randint(0,len(Study)-1)
    print(Study[num])
def Contributions():
    num = random.randint(0,len(Cont)-1)
    print(Cont[num])
def Success():
    num = random.randint(0,len(successful)-1)
    print(successful[num])
def trust():
   num = random.randint(0,len(Untrustworthy)-1)
   print(Untrustworthy[num])
def student():
    num = random.randint(0,len(stud)-1)
    print(stud[num])
def statement():
    print("______________________")
    print("If it pleases the judge and jury, let us talk to you a bit about our client.")
    print("everyone knows his name, the alleged story of abuse, but you simply do not know the kind of man he really is")
    print("unlike his accuser, our client is extremely involved in his community, and is even known for ")
    Contributions()
    print("A straight A student, our client ")
    student()
    print("He earned this academic success by " )
    study()
    print("When not in class, our client can be found ")
    ec()
    print(" or ")
    fri()
    print("We simply cannot say the same for his accuser, who keeps to herself and has been known to ")
    trust()
    print("All in all, our client has a bright future, ")
    Success() 
    print("And should not have this compromised with a momentary alleged mistake")
def interact():
    category = input("Which category does this data belong to?")
    if (category == ("student")):
        dat = input("insert data")
        stud.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("untrustworthy")):
        dat = input("insert data")
        Untrustworthy.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("ec")):
        dat = input("insert data")
        Extracurricular.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("fri")):
        dat = input("insert data")
        Friday.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("study")):
        dat = input("insert data")
        Study.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("cont")):
        dat = input("insert data")
        Cont.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
    elif (category == ("success")):
        dat = input("insert data")
        successful.append(dat)
        done = input("done?")
        if (done == ("Y")):
            statement()
        elif (done == ("N")):
            interact()
interact()

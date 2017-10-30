#_*_ coding:utf-8 _*_

class myclass:
    def __init__(self,username,userage):
        self.name = username
        self.age = userage
        print("This user info is:\n" + self.name + "\n" + str(self.age))        
    def addAge(self,username,userage):
        print("My name is %s,my age is %d." % (self.name,self.age))
    
user1 = myclass("smnra",30)
user2 = myclass("haha",23)

print(user1.name + "_" + user2.name)
user1.addAge("didi",8)


class myuser(myclass):
    pass

    
user3 = myuser("juai",45)
user3.addAge("yidao",9)


class myuser2(myclass):
    def addAge(self,username,userage):
        print("hahahhaha %s,gagagaga %d." % (self.name,self.age))
user4 = myuser2("mimi",33)
user4.addAge("shenzhou",5)        

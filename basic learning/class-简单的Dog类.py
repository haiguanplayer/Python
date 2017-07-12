class Dog() :
    def __init__(self,name,age) :
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self) :
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting. ")
    def roll_over(self) :
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over! ")

my_dog = Dog("BigDog",1)
my_dog.sit()
my_dog.roll_over()
print (my_dog.name+"!!!"+str(my_dog.age))
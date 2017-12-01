def greet_user():
    '''this is greet words'''
    print("hello")
greet_user()

def greet_user(username):
    '''向一个人简单问候'''
    print('hello,'+username.title())
greet_user('wangdi')

'''位置实参的例子'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
'''关键字实参'''
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

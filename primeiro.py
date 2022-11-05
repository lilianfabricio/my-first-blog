# print('Hello, Django Girls!')
# print('Teste!')
# name = ''
# if (name == 'Lilian'):
    
#     print('Oi ' + name + '!')
# else:
#     name = 'Fabrício'
#     print('Oi ' + name + '!')

# #volume = int(input("Volume:" ))
# volume = 40 
# if volume < 20:
#     print("It's kinda quiet.")
# elif 20 <= volume < 40:
#     print("It's a nice background music.")
# elif 40 <= volume < 60:
#     print("Perfect, I can hear all the details!")
# elif 60 <= volume < 80:
#     print("Nice for parties.")
# elif 80 <= volume < 100:
#     print("a bit loud!")
# else:
#     print("My ears are hurting!")

# if volume < 20 or volume > 80:
#     volume = 50
#     print("That's better!")

# #print(volume)

# def hi():
#     print('Hi there!')
#     print('How are you?')

# name = 'Ola'
# def hi(name):
#     if name == 'Ola':
#         print('Hi Ola!')
#     elif name == 'Sonja':
#         print('Hi Sonja!')
#     else:
#         print('Hi anonymous!')

# hi(name)

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

# quantidade = len(girls)
# print(quantidade)

for i in range(1, 6):
    print(i)
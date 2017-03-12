print('Hello, Django girls!')
if 3>2:
	print('Funguje to!')
name ='Sonja'
if name == 'Martina':
    print('Ahoj Martina!')
elif name == 'Janka':
	print('Ahj Janka!')
else:
	print('Ahoj!')

def hi():
	print('Ahoj!')
	print('Ako sa mas?')
hi()
def hi(meno):
	print('Ahoj' + meno + '!')
hi('Katka')
def hi(meno):
	print('Ahoj' + meno + '!')
dievcata = ['Katka', 'Monika', 'Zuzka', 'Ola', 'Ty']
for meno in dievcata:
	hi (meno)
	print('Dalsie dievca')

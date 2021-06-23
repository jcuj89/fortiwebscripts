x=int(input('Ingrese la cantidad de servers pools: '))
y=int(input('A partir de que numero desea comenzar el server pool: '))
z=int(input('Ingrese el puerto para este server pool: '))
a=(x+y)
for i in range(y,a):
       print(f'edit {i}')
       print(f'set port {z}')
       print(f'set ssl enable')
       print(f'next')
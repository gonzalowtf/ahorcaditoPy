# ahorcado en python


      


class Palabra():
     lista=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']
     letrasusadas=[]
     


     def formar(self,letra,clave):
           
       for ind in range(0,len(clave)):
              if letra[0]==clave[ind]:
                self.lista[ind]=letra[0]
              
       
        
         
        
     def usada(self,letra):
      for ind in range(0,len(self.letrasusadas)):
        if self.letrasusadas[ind]==letra:
          print ('ya usaste esta letra')
          return -1
      self.letrasusadas.append(letra)

     def mostrar(self,clave):
      print("""
                             
                             """)
      print(' PALABRA : ')                       
      print(self.lista[:len(clave)])
      print(' ')
      print('letras usadas :')
      print(self.letrasusadas)
    
     def dibujo(self,intentos):
           if intentos<=8 and intentos>6:                      
                print('__________')
                print('| O     O|')
                print('|        |')
                print('|________|')
           if intentos <=6 and intentos > 4:
                print('__________')
                print('| O    O |')
                print('|        |')                
                print('|________|')
                print('    |     ')
                print('    |     ')          
           if intentos<=4 and intentos > 2:
                print('__________')
                print('| O    O |')
                print('|        |')
                print('|________|')
                print('    |     ')
                print('----|-----')
                print('    |     ')
                print('    |     ')                                                                  
           if intentos<=2 and intentos > 1:
                print('__________')
                print('| O    O |')
                print('|        |')
                print('|________|')
                print('    |     ')
                print('----|-----')
                print('    |     ')
                print('    |     ')
                print('   . .    ')
                print('  .   .   ')
                print(' .     .  ')     
           if intentos==1:
                print('__________')
                print('| O    O |')
                print('|        |')
                print('|________|')
                print('----|------>     ')
                print('----|-----')
                print('    |     ')
                print('    |     ')
                print('   . .    ')
                print('  .   .   ')
                print(' .     .  ')    
                          
     def retornar(self,clave, letra):
      if self.lista[:len(clave)]==clave:
        return -1
      elif len(letra) != 1:
          letra=list(letra)
          if letra==clave:
            return -1
      else:
        return 5
dic=('esclerosis', 'myxomatosis', 'albania', 'judaismo','antropologia','sistemas','gandalf','sailing','gelatina',
  'mani','alemania','inglaterra','karma','boom','ambiguo','cena', 'politrote','francia','mexico')
  

import random

n=random.randint(0,len(dic))

intentos=10

clave=dic[n]
clave=list(clave)


print ('                   BIENVENIDO AL AHORCADITO =P')

print ("""

             adivina la palabra en menos de diez intenos! 



(en caso de saber la palabra definitiva simplemente escribela y pulsa enter)


                                                         """)

print('la palabra tiene : %d letras '%(len(clave)))
pal=Palabra()
control=10

contarmal = 0

while intentos>0: 
            print ('\n\n\n elige una letra : ')
   
            letra=input()
                        

                                       
            for ind in range(0,len(clave)):
                  
                   if letra==clave[ind]:
                        print('\n la letra esta en la posicion: %d\n'%(ind+1)) 
                        pal.formar(letra,clave)
                   
                   else :
                        contarmal = contarmal +1             
                        

                                  
           
            if contarmal == len(clave):
              print ('\nla letra %s\n'%(letra))
              print ('\n no se encuentra en la palabra') 
              contarmal = 0
            else :
              contarmal = 0   

            pal.dibujo(intentos)      
            pal.usada(letra)  
            pal.mostrar(clave)
            intentos=intentos-1
            print ("""
                    
                                        """)
            print (' te quedan : %d intentos'%intentos)
            control=pal.retornar(clave,letra)
            if control == - 1:
              print ("""GANASTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:D
              


                                                 """)
                        
              
              break


if intentos == 0:
  if control != - 1:
      print (""" 
      
                  
                    se acabaron los intentos :( , suerte la proxima
      



                                              """)
print( """
              
              """)
print (' la palabra era : ')
print (clave)
input("presiona enter para salir")





















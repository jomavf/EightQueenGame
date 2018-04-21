import random
import time

#Funciones de dibujo

def printNumbersHorizontal(t):
    n=len(t)
    for i in range(n):
        print("   {}".format(i),end='')
    print("")
def printHorizontalLines(t):
    n=len(t)
    print(" ",end='')            
    print(("+---")*n,end='')
    print('+')       

def draw(t,c):
    n = len(t)
    printNumbersHorizontal(t)
    printHorizontalLines(t)     
    for i in range(n):
        s = '{}|'.format(i) 
        for j in range(n):
            s += ' {} |{}'.format( c if t[j] == i else ' ',i if j==n-1 else "")
        print(s)
        printHorizontalLines(t) 
    printNumbersHorizontal(t)

#Clase Maquina
    ##
    
class Maquina:
    def __init__(self):       
        self.values = []
        self.count =0
        self.max_count=10
        
    def copyArray(self,pArray):        
        array= [-1]*len(pArray)
        for i in range(len(pArray)):
            array[i] = pArray[i]
        return array
    
    def isLegal(self,t,fil,col):
        n=len(t)
        for i in range(n):
            if t[i]!=-1:
                if col==i or fil==t[i]:                
                    return False
                elif abs(i-col) == abs(t[i]-fil):            
                    return False                
        return True
       
        
    def generator(self,t,col=0):         
        n= len(t)
        EDGE = n-1
        if col< n:
            for col in range(n):            
                for fil in range(n):
                    if t[col] ==-1 or col==EDGE:
                        if self.isLegal(t,fil,col):                        
                            t[col]=fil                                                
                            self.generator(t,col+1)
                            t[col]=-1
                        elif col==EDGE and fil==EDGE:                            
                            newArray = self.copyArray(t)
                            self.values.append(newArray)                        
        else:            
            newArray = self.copyArray(t)
            self.values.append(newArray)           

#Funcion Obtener Coordenadas
def getCoorXY(t,vectors,coox=0,cooy=0):   
    randomNumber = random.randint(0,len(vectors)-1)
    n = len(t)    
    vector = vectors[randomNumber]
    vector_x=[]
    vector_y=[]
    for col in range(n):
        if t[col]==-1 and vector[col]!=-1:
            coox = vector[col]
            cooy = col
            vector_x.append(coox)
            vector_y.append(cooy)
    if len(vector_x)==0 or len(vector_y)==0:
        return "Imposible","Imposible"
    randomXY = random.randint(0,len(vector_x)-1)    
    coox= vector_x[randomXY]        
    cooy= vector_y[randomXY]                
    return coox,cooy           
    
#Funciones Basicas
            
def ask_play():
    a,b=input("Ingrese su jugada ( en terminos fil,col ): ").split(",")
    return a,b

def insert_square(t,f,c):
    t[int(c)]=int(f)
    return t

def CrearBot():
    bot = Maquina()
    return bot

def isMoveLegal(t,col,fil):
    AuxBot = Maquina()
    return AuxBot.isLegal(t,int(col),int(fil))

n=8
REINAS=0
MAX_REINAS = n
MAX_ERRORES=3
ERRORES = 0
RESULTADO = "Has Perdido"
T = [-1]*n
JUGADAS=0
noAsk=True
TIME_LEFT = 30

   
def DeshacerJugada(t,fil,col):
    
    flag=input("Desea deshacer la jugada (Si/No): ")
    if flag == "Si" or flag=="si":
        t[col]=-1
        draw(t,'@')
    elif flag =="No" or flag == "no":
        pass
    
def reloj(time_sec):
    for i in range(0,time_sec,-1):
        print("Te quedan {} segundos.".format(i),end='')
        print("".format(i),end='')
        
        

while REINAS<=MAX_REINAS and ERRORES<MAX_ERRORES:
    if JUGADAS!=0 and noAsk==True:
        DeshacerJugada(T,AI_fil,AI_col)

    #print("Te quedan {} segundos".format())    
    fil,col = ask_play()
    
    if isMoveLegal(T,fil,col):
        bot = CrearBot()
        T = insert_square(T,fil,col)
        draw(T,'Q')
        print("Maquina esta pensando...")
        bot.generator(T)
        AI_fil,AI_col = getCoorXY(T,bot.values)
        
        if AI_fil  == "Imposible":
            Resultado="Has ganado!!!"
            break
        t = insert_square(T,AI_fil,AI_col)
        draw(T,'@')
        REINAS+=1
        noAsk = True
    else:
        ERRORES+=1
        print("La jugada no es correcta , Errores = {}".format(ERRORES))
        noAsk = False
    JUGADAS = JUGADAS + 1
    
print(Resultado)










import random

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


def sumScore(score):
    score += 10
    return score

n=8
REINAS=0
MAX_REINAS = n
MAX_ERRORES=3
ERRORES = 0
RESULTADO = "Has Perdido"
T = [-1]*n
PLAYER_SCORE = 0
BOT_SCORE = 0
MAX_SCORE = 40


while REINAS<=MAX_REINAS or ERRORES<MAX_ERRORES :
    fil,col = ask_play()
    if isMoveLegal(T,fil,col):
        bot = CrearBot()
        T = insert_square(T,fil,col)
        draw(T,'Q')
        PLAYER_SCORE += 10
        print ("Human Score = {} , Bot Score = {}".format(PLAYER_SCORE , BOT_SCORE))
        
        print("Maquina esta pensando...")
        bot.generator(T)
        AI_fil,AI_col = getCoorXY(T,bot.values)

        if AI_fil  == "Imposible":
            Resultado="Has ganado!!!"
            break
    
        t = insert_square(T,AI_fil,AI_col)
        draw(T,'@')

        BOT_SCORE += 10
        print ("Human Score = {} , Bot Score = {}".format(PLAYER_SCORE , BOT_SCORE))
        if BOT_SCORE >= MAX_SCORE:
            Resultado = "Winner Bot"
            break
        elif PLAYER_SCORE >= MAX_SCORE:
             Resultado = "Winner Human"
             break
        elif PLAYER_SCORE >= MAX_SCORE and BOT_SCORE >= MAX_SCORE:
             Resultado = "Empateee !!!!!"
             break
        REINAS+=1
        
    else:
        ERRORES+=1
        PLAYER_SCORE -= 5
        print ("Human Score = {} , Bot Score = {}".format(PLAYER_SCORE , BOT_SCORE))
        print("La jugada no es correcta , Errores = {}".format(ERRORES))
   
    
print(Resultado)










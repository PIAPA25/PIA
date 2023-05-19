class Agregar():
    def __init__(self,frase,autor,calif,id_frase):
        self.frase = frase
        self.autor = autor 
        self.calif = calif
        self.id_frase = id_frase

        
    def agregar_frase(self):
        a = open("frases.txt","a",encoding="utf8")
        a.write(f"ID:{self.id_frase}~~~NOMBRE:{self.autor} ~~~FRASE:{self.frase} ~~~CALIFICACION:{self.calif}\n")
        a.close()
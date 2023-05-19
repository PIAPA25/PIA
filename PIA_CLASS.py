class Agregar():
    def __init__(self,frase,autor,calif,id_frase):
        self.frase = frase
        self.autor = autor 
        self.calif = calif
        self.id_frase = id_frase

        
    def agregar_frase(self):
        a = open("frases.txt","a")
        a.write(f"{self.id_frase} {self.autor} {self.frase} {self.calif}\n")
        a.close()
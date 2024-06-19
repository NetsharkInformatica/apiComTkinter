from tkinter import *
import requests
import json

#9867ae59

class Api:
    def __init__(self):
        
        self.janela= Tk()
        self.janela.title('api com tkinter')
        self.janela.geometry('500x300+250+30')
        self.janela.resizable(0,0)
        #'https://www.omdbapi.com/?s=starwars&apikey=9867ae59'
        """ self.request= requests.get()
        self.dict=json.loads(self.request.text) """
        
        self.frame=Frame(self.janela)
        self.frame.pack(fill='x')
        
        self.label=Label(self.frame,text='insira um link aqui',font='Arial  16 bold')
        self.label.grid(row=0,column=0)
        self.entryDados=Entry(self.frame,font='Arial 16')
        self.entryDados.grid(row=0, column=1)
        
        self.btnSearch=Button(self.frame,text='buscar',command=self.searchServ,padx=5)
        self.btnSearch.grid(row=0,column=3)
        
        
        self.frame2=Frame(self.janela)
        self.frame2.pack()
        
        self.lista=Listbox(self.frame2,width=130)
        self.lista.grid(row=3,column=0,pady=10)
        
        self.janela.mainloop()
        
        
    def searchServ(self):
        
        try:
            request= requests.get('https://www.omdbapi.com/?t=' + self.entryDados.get() + '&apikey=9867ae59')
            dict=json.loads(request.text)
            
            self.lista.insert(END,('Title: ' + dict['Title']))
            self.lista.insert(END,('Year: ' + dict['Year']))
            self.lista.insert(END,('Released: ' + dict['Released']))
            self.lista.insert(END,('Time: ' + dict['Runtime']))
            self.lista.insert(END,('Genre: ' + dict['Genre']))
            self.lista.insert(END,('Director: ' + dict['Director']))
        except:
            self.lista.delete(0,END)
            self.lista.insert(END,'Nao ha nenhum filme com esse numero')
      
        


Api()
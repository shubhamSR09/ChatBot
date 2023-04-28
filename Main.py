
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title('Gabha Chatbot')
        self.root.geometry('700x620+0+0')


        frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        frame.pack()

        img=Image.open('gabha.png')
        img=img.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)




        title_label=Label(frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)


        self.scroll_y=ttk.Scrollbar(frame,orient=VERTICAL)
        self.text=Text(frame,width=65,height=20,bd=4,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=X)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar() 
        self.entry1=ttk.Entry(btn_frame,width=40,textvariable=self.entry,font=('arial',13,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=3,padx=3,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label8=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.label8.grid(row=1,column=1,padx=5,sticky=W)

#======================================function========
    def enter_fun(self,event):
        self.send.invoke()

    def clear(self):
        self.text.delete('1.0',END)
        self.entry


    def send(self):
        send = '\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

        if (self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.label8.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label8.config(text=self.msg,fg='red')

        if (self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='what is gabha'):
            self.text.insert(END,'\n\n'+'Bot: GABHA is a Welfare TRUST namely Growing Astronomers of Bhartiya Astronomy.'
                                        'It is established in 2019, with the objective of serving the society in Astronomy'
                                            'Education, Health care, Entertainment and Services. GABHA excels all through the '
                                            'areas of Astronomy, Artificial Intelligence and Robotics. Who hasn''t wondered about' 
                                            'the divine ponders and encountered the feeling of amazement at being a piece of such a vast span?'
                                            'GABHA looks to expand on this interest and bring development, energy and complete pledge to its vision '
                                            'of spreading the mindfulness and information of cosmology.')

        elif (self.entry.get()=='What is Python'):
            self.text.insert(END,'\n\n'+'Bot: Python is an interpreted, object-oriented, high-level programming '
                             'language with dynamic semantics developed by Guido van Rossum. It was originally released in 1991. '
                             'Designed to be easy as well as fun, the name "Python" is a nod to the British comedy group Monty Python. '
                             'Python has a reputation as a beginner-friendly language, replacing Java as the most widely used introductory '
                             'language because it handles much of the complexity for the user, allowing beginners to focus on fully grasping '
                             'programming concepts rather than minute details.')
        
        elif (self.entry.get()=='What is AI'):
            self.text.insert(END,'\n\n'+'Bot: AI has become a catchall term for applications that perform complex tasks that once required human input,' 
                             'such as communicating with customers online or playing chess. The term is often used interchangeably with its subfields, which'
                             'include machine learning (ML) and deep learning.')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I did not get it")



if __name__ =='__main__':
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()
        
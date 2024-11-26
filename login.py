import os
import sqlite3
from tkinter import*
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Restaurant Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#607d8b")
        
        # ===Login Frame===
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#767171")
        login_frame.place(x=525,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="#767171").place(x=0,y=30,relwidth=1)
        
        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="#767171",fg="white").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ececec").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="#767171",fg="white").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ececec").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00b0f0",activebackground="#00b0f0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=320,width=250,height=45)
        

    def login(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.employee_id.get()=="admin" and self.password.get()=="1234": #default id and password
                self.root.destroy()
                os.system("python dashboard.py")
            else:
                cur.execute("select * from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Employee ID / Password",parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()

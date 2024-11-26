from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from employee import employeeClass
from category import categoryClass
from items import itemsClass
from sales import salesClass
from table import tableManagementClass
import os
import sqlite3
import time

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Restaurant Management System | Developed By Team Not Noobs")
        self.root.config(bg="white")
        
        self.sub_windows = []  # List to store all sub-windows
        
        #===title====
        self.icon_title = PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Restaurant Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0, relwidth=1, height=70)
        
        #===btn_logout===
        btn_logout = Button(self.root, text="Logout", command=self.logout,font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        
        #===clock====
        self.lbl_clock = Label(self.root, text="Welcome to Restaurant Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        
        #===Left Menu===
        
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        
        self.icon_side = PhotoImage(file="images/side.png")
        
        btn_dashboard = Button(LeftMenu, text="Dashboard", command=self.dashboard, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_items = Button(LeftMenu, text="Items", command=self.items, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_table_management = Button(LeftMenu, text="Tables", command=self.table_management, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)  # New button
        btn_order = Button(LeftMenu, text="Order", command=self.order, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        
        #===content====
        
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bg="#33bbf9", bd=5, relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)
        
        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bg="#ff5722", bd=5, relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=650, y=120, height=150, width=300)
        
        self.lbl_items = Label(self.root, text="Total Items\n[ 0 ]", bg="#009688", bd=5, relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_items.place(x=1000, y=120, height=150, width=300)
        
        self.lbl_tables = Label(self.root, text="Total Table\n[ 0 ]", bg="#607d8b", bd=5, relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_tables.place(x=300, y=300, height=150, width=300)
        
        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bg="#ffc107", bd=5, relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        
        #===footer====
        lbl_footer = Label(self.root, text="RMS-Restaurant Management System | Developed By Team Not Noobs\nFor any Technical Issue Contact: mahmud15-6115@s.diu.edu.bd", font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X) 
        
        self.update_content()
        
#==================================================================

    def clear_sub_window(self):
        for win in self.sub_windows:
            win.destroy()
        self.sub_windows.clear()
        
    def dashboard(self):
        self.clear_sub_window()

    def employee(self):
        self.clear_sub_window()
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        self.sub_windows.append(self.new_win)
        
    def category(self):
        self.clear_sub_window()
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        self.sub_windows.append(self.new_win)
        
    def items(self):
        self.clear_sub_window()
        self.new_win=Toplevel(self.root)
        self.new_obj=itemsClass(self.new_win)
        self.sub_windows.append(self.new_win)
        
    def table_management(self):
        self.clear_sub_window()
        self.new_win = Toplevel(self.root)
        self.new_obj = tableManagementClass(self.new_win)
        self.sub_windows.append(self.new_win)
        
    def order(self):
        self.clear_sub_window()
        self.root.destroy()
        os.system("python order.py")
        
    def sales(self):
        self.clear_sub_window()
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        self.sub_windows.append(self.new_win)
        
    def update_content(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from items")
            items=cur.fetchall()
            self.lbl_items.config(text=f"Total Items\n[ {str(len(items))} ]")
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")
            
            cur.execute("select * from tables")
            tables=cur.fetchall()
            self.lbl_tables.config(text=f"Total Table\n[ {str(len(tables))} ]")
            
            self.lbl_sales.config(text=f"Total Sales\n[ {str(len(os.listdir('bill')))} ]")
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Restaurant Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
        
if __name__=="__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()

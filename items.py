from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class itemsClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1100x500+220+130")
        self.root.title("Restaurant Management System | Developed By Team Not Noobs")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========Variables==========
        self.var_cat = StringVar()
        self.var_itm_id = StringVar()
        
        self.cat_list=[]
        
        self.fetch_cat()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        # items Frame (Left Side)
        items_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        items_Frame.place(x=10, y=10, width=450, height=480)

        ########## Title ##########
        title = Label(items_Frame, text="Manage Items Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        ########## Labels ##########
        #====column 1====
        lbl_category = Label(items_Frame, text="Category", font=("goudy old style", 15), bg="white", fg="black")
        lbl_category.place(x=30, y=60)

        lbl_items_name = Label(items_Frame, text="Name", font=("goudy old style", 15), bg="white", fg="black")
        lbl_items_name.place(x=30, y=110)

        lbl_price = Label(items_Frame, text="Price", font=("goudy old style", 15), bg="white", fg="black")
        lbl_price.place(x=30, y=160)

        lbl_qty = Label(items_Frame, text="Quantity", font=("goudy old style", 15), bg="white", fg="black")
        lbl_qty.place(x=30, y=210)

        lbl_status = Label(items_Frame, text="Status", font=("goudy old style", 15), bg="white", fg="black")
        lbl_status.place(x=30, y=260)

        ########## Dropdowns ##########
        # Category Dropdown
        #====column 2====
        cmb_category = ttk.Combobox(items_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_category.place(x=150, y=60, width=200)
        cmb_category.current(0)

        ########## Entry Fields ##########
        txt_name = Entry(items_Frame, textvariable=self.var_name, font=("goudy old style", 13), bg="lightyellow")
        txt_name.place(x=150, y=110, width=200)

        txt_price = Entry(items_Frame, textvariable=self.var_price, font=("goudy old style", 13), bg="lightyellow")
        txt_price.place(x=150, y=160, width=200)

        txt_qty = Entry(items_Frame, textvariable=self.var_qty, font=("goudy old style", 13), bg="lightyellow")
        txt_qty.place(x=150, y=210, width=200)

        ########## Status Dropdown ##########
        cmb_status = ttk.Combobox(items_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_status.place(x=150, y=260, width=200)
        cmb_status.current(0)

        ########## Buttons ##########
        btn_save = Button(items_Frame, text="Save", command=self.add, font=("goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2")
        btn_save.place(x=10, y=400, width=100, height=40)

        btn_update = Button(items_Frame, text="Update", command=self.update, font=("goudy old style", 13), bg="#2196f3", fg="white", cursor="hand2")
        btn_update.place(x=120, y=400, width=100, height=40)

        btn_delete = Button(items_Frame, text="Delete", command=self.delete,  font=("goudy old style", 13), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=400, width=100, height=40)

        btn_clear = Button(items_Frame, text="Clear", command=self.clear, font=("goudy old style", 13), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=400, width=100, height=40)

        # Search Frame (Right Side)
        search_Frame = LabelFrame(self.root, text="Search Items", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        search_Frame.place(x=480, y=10, width=600, height=80)

        # Search by Dropdown
        #===options====
        cmb_search = ttk.Combobox(search_Frame, textvariable=self.var_searchby, values=("Select", "Category", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        # Search Text
        txt_search = Entry(search_Frame, textvariable=self.var_searchtxt, font=("goudy old style", 13), bg="lightyellow")
        txt_search.place(x=200, y=10)

        # Search Button
        btn_search = Button(search_Frame, text="Search", command=self.search,font=("goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=410, y=9, width=150, height=30)

        # Data Table
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

# >>>>>>>>>>>>>>>>>>>>>>
        self.items_table = ttk.Treeview(p_frame, columns=("itm_id", "category", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.items_table.xview)
        scrolly.config(command=self.items_table.yview)

        self.items_table.heading("itm_id", text="Itm ID")
        self.items_table.heading("category", text="Category")
        self.items_table.heading("name", text="Name")
        self.items_table.heading("price", text="Price")
        self.items_table.heading("qty", text="Qty")
        self.items_table.heading("status", text="Status")
        self.items_table["show"] = "headings"

        self.items_table.column("itm_id", width=90)
        self.items_table.column("category", width=100)
        self.items_table.column("name", width=150)
        self.items_table.column("price", width=100)
        self.items_table.column("qty", width=100)
        self.items_table.column("status", width=100)

        self.items_table.pack(fill=BOTH, expand=1)
        self.items_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        
#=================================================================

    def fetch_cat(self):
        self.cat_list.append("Empty")
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        


    def add(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_name.get()=="" or self.var_price.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from items where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Items already present, try different",parent=self.root)
                else:
                    cur.execute("Insert into items (category, name, price, qty, status) values(?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Items added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        
    def show(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from items")
            rows=cur.fetchall()
            self.items_table.delete(*self.items_table.get_children())
            for row in rows:
                self.items_table.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        
    def get_data(self,ev):
        f=self.items_table.focus()
        content=(self.items_table.item(f))
        row=content['values']
        self.var_itm_id.set(row[0])
        self.var_cat.set(row[1])
        self.var_name.set(row[2])
        self.var_price.set(row[3])
        self.var_qty.set(row[4])
        self.var_status.set(row[5])
        
        
    def update(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_itm_id.get()=="":
                messagebox.showerror("Error","Please select items from list",parent=self.root)
            else:
                cur.execute("Select * from items where itm_id=?",(self.var_itm_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid items",parent=self.root)
                else:
                    cur.execute("Update items set category=?,name=?,price=?,qty=?,status=? where itm_id=?",(
                        self.var_cat.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_itm_id.get() 
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Items updated successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
 
    def delete(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_itm_id.get()=="":
                messagebox.showerror("Error","Select items from the list",parent=self.root)
            else:
                cur.execute("Select * from items where itm_id=?",(self.var_itm_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid items",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from items where itm_id=?",(self.var_itm_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Items deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        
        
        
    def clear(self):
        self.var_cat.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_itm_id.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        
        
    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
                
            cur.execute("select * from items where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            
            if len(rows)!=0:
                self.items_table.delete(*self.items_table.get_children())
                for row in rows:
                    self.items_table.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found!!!",parent=self.root)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
        


if __name__ == "__main__":
    root = Tk()
    obj = itemsClass(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  
import sqlite3

class tableManagementClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+100")
        self.root.title("Table Management | Restaurant Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_tid = StringVar()
        self.var_table_no = StringVar()
        self.var_waitress = StringVar()
        self.var_cleaner = StringVar()
        self.var_water_boy = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()

        # Table Management Frame
        table_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        table_Frame.place(x=10, y=10, width=450, height=580)

        # Title
        title = Label(table_Frame, text="Manage Table Assignments", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        # Labels and Entry Fields
        lbl_table_no = Label(table_Frame, text="Table No", font=("goudy old style", 15), bg="white", fg="black")
        lbl_table_no.place(x=30, y=60)
        txt_table_no = Entry(table_Frame, textvariable=self.var_table_no, font=("goudy old style", 13), bg="lightyellow")
        txt_table_no.place(x=150, y=60, width=200)

        lbl_waitress = Label(table_Frame, text="Waitress", font=("goudy old style", 15), bg="white", fg="black")
        lbl_waitress.place(x=30, y=110)
        txt_waitress = Entry(table_Frame, textvariable=self.var_waitress, font=("goudy old style", 13), bg="lightyellow")
        txt_waitress.place(x=150, y=110, width=200)

        lbl_cleaner = Label(table_Frame, text="Cleaner", font=("goudy old style", 15), bg="white", fg="black")
        lbl_cleaner.place(x=30, y=160)
        txt_cleaner = Entry(table_Frame, textvariable=self.var_cleaner, font=("goudy old style", 13), bg="lightyellow")
        txt_cleaner.place(x=150, y=160, width=200)

        lbl_water_boy = Label(table_Frame, text="Water Boy", font=("goudy old style", 15), bg="white", fg="black")
        lbl_water_boy.place(x=30, y=210)
        txt_water_boy = Entry(table_Frame, textvariable=self.var_water_boy, font=("goudy old style", 13), bg="lightyellow")
        txt_water_boy.place(x=150, y=210, width=200)

        lbl_time = Label(table_Frame, text="Time Slot", font=("goudy old style", 15), bg="white", fg="black")
        lbl_time.place(x=30, y=260)
        cmb_time = ttk.Combobox(table_Frame, textvariable=self.var_time, values=["5 AM - 12 PM", "12 PM - 8 PM", "8 PM - 5 AM"], state="readonly", justify=CENTER, font=("goudy old style", 13))
        cmb_time.place(x=150, y=260, width=200)
        cmb_time.current(0)

        lbl_date = Label(table_Frame, text="Date", font=("goudy old style", 15), bg="white", fg="black")
        lbl_date.place(x=30, y=310)
        txt_date = DateEntry(table_Frame, textvariable=self.var_date, font=("goudy old style", 13), bg="lightyellow", date_pattern='yyyy-mm-dd')
        txt_date.place(x=150, y=310, width=200)

        # Buttons
        btn_save = Button(table_Frame, text="Save", command=self.add, font=("goudy old style", 13), bg="#4caf50", fg="white", cursor="hand2")
        btn_save.place(x=10, y=500, width=100, height=40)

        btn_update = Button(table_Frame, text="Update", command=self.update, font=("goudy old style", 13), bg="#2196f3", fg="white", cursor="hand2")
        btn_update.place(x=120, y=500, width=100, height=40)

        btn_delete = Button(table_Frame, text="Delete", command=self.delete, font=("goudy old style", 13), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=500, width=100, height=40)

        btn_clear = Button(table_Frame, text="Clear", command=self.clear, font=("goudy old style", 13), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=500, width=100, height=40)

        # Data Table
        data_Frame = Frame(self.root, bd=3, relief=RIDGE)
        data_Frame.place(x=480, y=10, width=600, height=580)

        scrolly = Scrollbar(data_Frame, orient=VERTICAL)
        scrollx = Scrollbar(data_Frame, orient=HORIZONTAL)

        self.table_table = ttk.Treeview(data_Frame, columns=("tid", "table_no", "waitress", "cleaner", "water_boy", "time_slot", "table_date"), 
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.table_table.xview)
        scrolly.config(command=self.table_table.yview)

        self.table_table.heading("tid", text="T ID")
        self.table_table.heading("table_no", text="Table No")
        self.table_table.heading("waitress", text="Waitress")
        self.table_table.heading("cleaner", text="Cleaner")
        self.table_table.heading("water_boy", text="Water Boy")
        self.table_table.heading("time_slot", text="Time Slot")
        self.table_table.heading("table_date", text="Date")
        self.table_table["show"] = "headings"

        self.table_table.column("tid", width=90)
        self.table_table.column("table_no", width=150)
        self.table_table.column("waitress", width=150)
        self.table_table.column("cleaner", width=150)
        self.table_table.column("water_boy", width=150)
        self.table_table.column("time_slot", width=100)
        self.table_table.column("table_date", width=100)

        self.table_table.pack(fill=BOTH, expand=1)
        self.table_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # Database Connection
    def db_connection(self):
        return sqlite3.connect(database='rms.db')

    def add(self):
        try:
            if self.var_table_no.get() == "" or self.var_date.get() == "":
                messagebox.showerror("Error", "Table No and Date are required", parent=self.root)
            else:
                with self.db_connection() as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO tables (table_no, waitress, cleaner, water_boy, time_slot, table_date) VALUES (?, ?, ?, ?, ?, ?)", (
                        self.var_table_no.get(),
                        self.var_waitress.get(),
                        self.var_cleaner.get(),
                        self.var_water_boy.get(),
                        self.var_time.get(),
                        self.var_date.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Table Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Table No already exists", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        try:
            with self.db_connection() as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM tables")
                rows = cur.fetchall()
                self.table_table.delete(*self.table_table.get_children())
                for row in rows:
                    self.table_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.table_table.focus()
        content = self.table_table.item(f)
        row = content['values']
        self.var_tid.set(row[0])
        self.var_table_no.set(row[1])
        self.var_waitress.set(row[2])
        self.var_cleaner.set(row[3])
        self.var_water_boy.set(row[4])
        self.var_time.set(row[5])
        self.var_date.set(row[6])

    def update(self):
        try:
            if self.var_tid.get() == "":
                messagebox.showerror("Error", "Please select a table from the list", parent=self.root)
            else:
                with self.db_connection() as con:
                    cur = con.cursor()
                    cur.execute("UPDATE tables SET table_no=?, waitress=?, cleaner=?, water_boy=?, time_slot=?, table_date=? WHERE tid=?", (
                        self.var_table_no.get(),
                        self.var_waitress.get(),
                        self.var_cleaner.get(),
                        self.var_water_boy.get(),
                        self.var_time.get(),
                        self.var_date.get(),
                        self.var_tid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Table Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        try:
            if self.var_tid.get() == "":
                messagebox.showerror("Error", "Please select a table from the list", parent=self.root)
            else:
                with self.db_connection() as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM tables WHERE tid=?", (self.var_tid.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Table Deleted Successfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_tid.set("")
        self.var_table_no.set("")
        self.var_waitress.set("")
        self.var_cleaner.set("")
        self.var_water_boy.set("")
        self.var_time.set("5 AM - 12 PM")
        self.var_date.set("")
        self.show()


if __name__ == "__main__":
    # Initialize Database for Tables if not exists
    def init_table_db():
        with sqlite3.connect(database='rms.db') as con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tables (
                    tid INTEGER PRIMARY KEY AUTOINCREMENT,
                    table_no TEXT UNIQUE NOT NULL,
                    waitress TEXT,
                    cleaner TEXT,
                    water_boy TEXT,
                    time_slot TEXT,
                    table_date TEXT
                )
            """)
            con.commit()
    init_table_db()

    root = Tk()
    obj = tableManagementClass(root)
    root.mainloop()

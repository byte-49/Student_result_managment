from tkinter import *
from PIL import Image, ImageTk
import time
import math 
import sqlite3
import os
from  tkinter import messagebox,ttk

class Log_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login here!")
        self.root.geometry("1445x870")   
        self.root.resizable(False, False)
        self.root.config(bg="#082032") 

        # ================= Background Colour =================
        left_lbl=Label(self.root,bg="#08a3d2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031f3c",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        # ================= Frame =================

        login_frame=Frame(self.root,bg="#9abde4")
        login_frame.place(x=290, y=180,width=900, height=520)

        title=Label(login_frame,text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="#9abde4", fg="#0d2e38").place(x=400, y=60)

        email=Label(login_frame,text="EMAIL ADDRESS", font=("times new roman", 20, "bold"), bg="#9abde4", fg="#000000").place(x=305, y=150)
        self.txt_email=Entry(login_frame, font=("times new roman", 20, "bold"), bg="lightgray", fg="#000000")
        self.txt_email.place(x=305, y=200)

        pass_=Label(login_frame,text="PASSWORD", font=("times new roman", 20, "bold"), bg="#9abde4", fg="#000000").place(x=305, y=280)
        self.txt_pass_=Entry(login_frame, font=("times new roman", 20, "bold"), bg="lightgray", fg="#000000")
        self.txt_pass_.place(x=305, y=330)

        btn_reg=Button(login_frame,cursor="hand2", text="Register New Account?", command=self.register_window, font=("times new roman",14), bg="#9abde4", bd=0, fg="#b00857").place(x=305, y=420)

        btn_forget=Button(login_frame,cursor="hand2", text="Forget Password?", command=self.forget_password_window, font=("times new roman",14), bg="#9abde4", bd=0, fg="#b00857").place(x=670, y=420)

        btn_login=Button(login_frame,text="LOGIN", command=self.login, font=("times new roman",20, "bold"), bg="#931a4f", fg="#ffffff", cursor="hand2").place(x=670, y=330, width=180, height=40)

        # ================= CLOCK CONTAINER =================
        self.clock_frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        self.clock_frame.place(x=90, y=230, height=420, width=410)

        self.canvas = Canvas(
            self.clock_frame,
            width=300,
            height=300,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(anchor="nw", padx=50, pady=50)


        # Load background image
        self.bg_img = Image.open("images/cl.jpg")
        self.bg_img = self.bg_img.resize((300, 300))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        self.canvas.create_image(150, 150, image=self.bg_photo)

        # Center of clock
        self.cx, self.cy = 150, 150

        self.update_clock()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="select" or self.txt_answer.get()==""or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root2)
        else :
            try: 
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=? and question=? and answer=?", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Select The Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update users set password=? where email=?" , (self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Succes","Your password has been reset, Please login with new password", parent=self.root2) 
                    self.reset()
                    self.root2.destroy()         

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter your email address to reset you password",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please enter your vaild email to reset you password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Foraget Password")
                    self.root2.geometry("450x450+550+250")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

                    #-------------forget password----------------------
                    question=Label(self.root2,text="Security Question.",font=("times new roman",15, "bold"), bg="white", fg="black").place(x=150,y=100)

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman", 13),state='readonly',justify=CENTER)
                    self.cmb_quest['values'] = ("select","Your First Pet Name", "Your Birth Place", "Your Best friend Name")
                    self.cmb_quest.place(x=100, y=140, width=250)
                    self.cmb_quest.current(0)

                    answer=Label(self.root2,text="Answer",font=("times new roman",15, "bold"), bg="white", fg="black").place(x=180,y=190)
                    self.txt_answer=Entry(self.root2,font=("times new roman", 15),bg="lightgray")
                    self.txt_answer.place(x=100, y=230, width=250)

                    new_pass=Label(self.root2,text="New Password",font=("times new roman",15, "bold"), bg="white", fg="black").place(x=160,y=280)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman", 15),bg="lightgray")
                    self.txt_new_pass.place(x=100, y=320, width=250)

                    btn_change_pass=Button(self.root2,text="Reset Password", command=self.forget_password, bg="green",fg="white",font=("times new roman", 15, "bold")).place(x=120, y=375, width=195)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)             

    def register_window(self):
        if hasattr(self, "after_id"):
            self.root.after_cancel(self.after_id)
        self.root.destroy()
        from register import Register
        root = Tk()
        Register(root)
        root.mainloop()


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error", "All fiels are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from users where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password!", parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}" , parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)

    def update_clock(self):
        self.canvas.delete("hands")

        t = time.localtime()
        sec = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12

        # Second hand
        sec_angle = math.radians(sec * 6 - 90)
        self.canvas.create_line(
            self.cx, self.cy,
            self.cx + 110 * math.cos(sec_angle),
            self.cy + 110 * math.sin(sec_angle),
            fill="red", width=2, tags="hands"
        )

        # Minute hand
        min_angle = math.radians(minute * 6 - 90)
        self.canvas.create_line(
            self.cx, self.cy,
            self.cx + 90 * math.cos(min_angle),
            self.cy + 90 * math.sin(min_angle),
            fill="black", width=4, tags="hands"
        )

        # Hour hand
        hour_angle = math.radians((hour * 30 + minute / 2) - 90)
        self.canvas.create_line(
            self.cx, self.cy,
            self.cx + 65 * math.cos(hour_angle),
            self.cy + 65 * math.sin(hour_angle),
            fill="black", width=6, tags="hands"
        )

        self.after_id = self.root.after(1000, self.update_clock)



# Run app
if __name__ == "__main__":
    root = Tk()
    Log_window(root)
    root.mainloop()

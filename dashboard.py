from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import time
import math
import sqlite3


class RMS:
    def __init__(self, root):
        self.clock_running = True
        self.root = root
        self.root.title("🧑‍🎓")
        self.root.geometry("1530x870+0+0")
        self.root.config(bg="white")

        # ---- Load Image ----
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # ---- Title Bar ----
        title_bar = Frame(self.root, bg="#033054")
        title_bar.place(x=0, y=0, relwidth=1, height=50)

        # ---- Center Title Text ----
        Label(
            title_bar,
            text="Student Result Management System",
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(relx=0.5, rely=0.5, anchor=CENTER)

        #----Menu----
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1410, height=80)

        # ================= ANALOG CLOCK =================
        self.clock_frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        self.clock_frame.place(x=100, y=250, width=400, height=400)

        self.canvas = Canvas(
            self.clock_frame,
            width=400,
            height=400,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()

        # Load clock background image
        self.clock_img = Image.open("images/cl.jpg")
        self.clock_img = self.clock_img.resize((400, 400), Image.LANCZOS)
        self.clock_photo = ImageTk.PhotoImage(self.clock_img)

        self.canvas.create_image(200, 200, image=self.clock_photo)

        # Center point
        self.cx, self.cy = 200, 200

        self.update_clock()


        #----Button----
        btn_course=Button(M_Frame,text="Course",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)

        btn_student=Button(M_Frame,text="Student",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_stdent).place(x=260,y=5,width=200,height=40)

        btn_result=Button(M_Frame,text="Result",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=490,y=5,width=200,height=40)

        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=720,y=5,width=200,height=40)

        btn_logut=Button(M_Frame,text="Logout",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=950,y=5,width=200,height=40)

        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1175,y=5,width=200,height=40)

        #----content_window----
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=570,y=180,width=780,height=500)

        #----update_details----
        self.lbl_course=Label(self.root,text="Total Courses\n [ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=570,y=720,width=250,height=80)

        self.lbl_student=Label(self.root,text="Total Students\n [ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#076451",fg="white")
        self.lbl_student.place(x=835,y=720,width=250,height=80)

        self.lbl_result=Label(self.root,text="Total Results\n [ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#0d89b6",fg="white")
        self.lbl_result.place(x=1100,y=720,width=250,height=80)

        # ---- footer ----
        footer = Label(
            self.root,
            text="SRMS - Student Result Management System \n Contact us for any technical issue: +91 70****1523",
            font=("goudy old style", 15, "bold"),
            bg="#262626",
            fg="white"
        ).pack(side = BOTTOM, fill=X)
        self.update_details()
        
    #-------------------------------------------------------------------------------------------------------------------------------------
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")


            cur.execute("Select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total students\n[{str(len(cr))}]")

            cur.execute("Select * from result ")
            cr=cur.fetchall() 
            self.lbl_result.config(text=f"Total results\n[{str(len(cr))}]")


            self.lbl_course.after(200,self.update_details)
    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add_course(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=CourseClass(self.new_win)

    def add_stdent(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=StudentClass(self.new_win)

    def add_result(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=resultClass(self.new_win)

    def add_report(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.clock_running = False  
            self.root.destroy()

            from login import Log_window
            root = Tk()
            Log_window(root)
            root.mainloop()



    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.clock_running = False   
            self.root.destroy()


    def update_clock(self):
        # remove old hands
        self.canvas.delete("hands")

        # get current time
        t = time.localtime()
        sec = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12

        # second hand
        sec_angle = math.radians(sec * 6 - 90)
        self.canvas.create_line(
            200, 200,
            200 + 170 * math.cos(sec_angle),
            200 + 170 * math.sin(sec_angle),
            fill="red", width=2, tags="hands"
        )

        # minute hand
        min_angle = math.radians(minute * 6 - 90)
        self.canvas.create_line(
            200, 200,
            200 + 140 * math.cos(min_angle),
            200 + 140 * math.sin(min_angle),
            fill="black", width=4, tags="hands"
        )

        # hour hand
        hour_angle = math.radians((hour * 30 + minute / 2) - 90)
        self.canvas.create_line(
            200, 200,
            200 + 100 * math.cos(hour_angle),
            200 + 100 * math.sin(hour_angle),
            fill="black", width=6, tags="hands"
        )

        # run again after 1 second
        if self.clock_running:
            self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()

from tkinter import *
from tkinter import messagebox
import pyqrcode
from fpdf import FPDF

window = Tk()
window.title("CV Generator")

class PDFCV(FPDF):
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")

    def footer(self):
        pass

    def generate_cv(self, name, email, address, phone, website, skills, work_experience, education, about_me):
        self.add_page()
        self.ln(20)
        # Displaying the name
        self.set_font("Arial", "B", 26)
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align="C")

        # Display the contact information header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Contact Information", new_x="LMARGIN", new_y="NEXT", align="L")

        # Display the contact information
        self.set_font("Arial", "", 10)
        self.cell(0, 5, f"Email: {email}", new_x="LMARGIN", new_y="NEXT", align="L")
        self.cell(0, 5, f"Phone: {phone}", new_x="LMARGIN", new_y="NEXT", align="L")
        self.cell(0, 5, f"Address: {address}", new_x="LMARGIN", new_y="NEXT", align="L")

        # Skills
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Skills", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 5, f"- {skill}", new_x="LMARGIN", new_y="NEXT")

        # Experience header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Arial", "", 10)
        for experience in work_experience:
            self.cell(0, 5, f"{experience['title']}: {experience['description']}", new_x="LMARGIN", new_y="NEXT")

        # Education header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Arial", "", 10)
        for education_item in education:
            self.cell(0, 5, f"{education_item['degree']}: {education_item['university']}", new_x="LMARGIN", new_y="NEXT")

        # About Me header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "About Me", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, about_me)

        self.output("cv1.pdf")


def generate_cv():
    name = entry_name.get()
    email = entry_email.get()
    address = entry_address.get()
    phone = entry_phone.get()
    website = entry_website.get()
    skills = entry_skills.get('1.0', END).strip().split("\n")
    work_experience = []
    education = []
    about_me = entry_about.get(1.0, END).strip()

    work_experience_lines = entry_experience.get('1.0', END).strip().split("\n")
    for line in work_experience_lines:
        if ":" in line:
            title, description = line.split(":", 1)
            work_experience.append({'title': title.strip(), 'description': description.strip()})

    education_lines = entry_education.get('1.0', END).strip().split("\n")
    for line in education_lines:
        if ":" in line:
            degree, university = line.split(":", 1)
            education.append({'degree': degree.strip(), 'university': university.strip()})

    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not address or not phone or not website or not skills or not work_experience or not education or not about_me:
        messagebox.showerror("Error", "Please fill in all the details")
        return

    cv = PDFCV()
    cv.generate_cv(name, email, address, phone, website, skills, work_experience, education, about_me)


label_name = Label(window, text="Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text="Email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone = Label(window, text="Phone: ")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(window, text="Address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_website = Label(window, text="Website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

label_skills = Label(window, text="Skills (Enter one skill per line): ")
label_skills.pack()
entry_skills = Text(window, height=3)
entry_skills.pack()

label_education = Label(window, text="Education (one per line 'Degree:University'): ")
label_education.pack()
entry_education = Text(window, height=3)
entry_education.pack()

label_experience = Label(window, text="Experience (one per line 'Job Title:Description'): ")
label_experience.pack()
entry_experience = Text(window, height=3)
entry_experience.pack()

label_about = Label(window, text="About Me: ")
label_about.pack()
entry_about = Text(window, height=3)
entry_about.pack()

button_generate = Button(window, text='Generate CV', command=generate_cv)
button_generate.pack()

window.mainloop()












# from tkinter import *
# from tkinter import messagebox
# import pyqrcode
# from fpdf import FPDF
#
# window =Tk()
# window.title("CV Generator")
#
# class PDFCV(FPDF):
#     def header(self):
#         self.image("mywebsite.png",10,8,33,title="Portfolio Site")
#
#     def footer(self):
#         pass
#     def generate_cv(self,name,email,address,phone,website,skills,work_experience,education,about_me):
#         self.add_page()
#         self.ln(20)
#         # displaying the names
#         self.set_font("Arial","B",26)
#         self.cell(0,10,name,new_x="LMARGN",new_y="NEXT",align="C")
#         #dispaly the contact information header
#         self.set_font("Arial","B",12)
#         self.cell(0,10,"contact information",new_x="LMARGIN",new_y="NEXT",align="L")
#
#         # dispaly the contact information
#         self.set_font("Arial", "", 10)
#         self.cell(0, 5, f"email: {email}", new_x="LMARGIN", new_y="NEXT", align="L")
#         self.cell(0, 5, f"Phone: {phone}", new_x="LMARGIN", new_y="NEXT", align="L")
#         self.cell(0, 5, f"Address: {address}", new_x="LMARGIN", new_y="NEXT", align="L")
#
#         #skill
#         self.ln(10)
#         self.set_font("Arial","B",12)
#         self.cell(0,10,"SKills",new_x="LMARGIN",new_y="NEXT",align="L")
#         #adding skills
#         self.set_font("Arial","",10)
#         for skill in skills:
#             self.cell(0,5,"- {}".format(skill),new_x="LMARGIN",new_y="NEXT")
#
#         # experiencen header
#         self.ln(10)
#         self.set_font("Arial", "B", 12)
#         self.cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT", align="L")
#         # work experience
#         self.set_font("Arial", "", 10)
#         for experience in work_experience:
#             self.cell(0, 5, "{}: {}".format(experience["title"],experience["discription"]), new_x="LMARGIN", new_y="NEXT")
#
#
#         # education header
#         self.ln(10)
#         self.set_font("Arial", "B", 12)
#         self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align="L")
#         # education details
#         self.set_font("Arial", "", 10)
#         for education_item in education:
#             self.cell(0, 5, "{}: {}".format(education_item["degree"], education["University"]), new_x="LMARGIN",new_y="NEXT")
#
#         # About header
#         self.ln(10)
#         self.set_font("Arial", "B", 12)
#         self.cell(0, 10, "About ME", new_x="LMARGIN", new_y="NEXT", align="L")
#         # about me
#         self.set_font("Arial", "", 10)
#         self.multi_cell(0,5,about_me)
#
#         self.output("cv1.pdf")
#
#
#
# def generated_cv():
#     name =entry_name.get()
#     email=entry_email.get()
#     address =entry_address.get()
#     phone =entry_phone.get()
#     website =entry_website.get()
#     skills =entry_skills.get('1.0', END).strip().split("\n")
#     work_experience =[]
#     education=[]
#     about_me = entry_about.get(1.0, END)
#
#     work_experience_lines =entry_experience.get('1.0', END).strip().split("\n")
#     for line in work_experience_lines:
#         title, Discription =line.split(":")
#         work_experience.append({'title':title.strip(),'discription':Discription.strip()})
#     education_lines =entry_education.get('1.0', END).strip().split("\n")
#     for line in education_lines:
#         degree, University =line.split(":")
#         work_experience.append({'degree': degree.strip(), 'university': University.strip()})
#
#     qrcode = pyqrcode.create(website)
#     qrcode.png("mywebsite.png",scale=6)
#     if not name or not email or not address or not phone or not website or not skills or  not work_experience or not education or not about_me:
#         messagebox.showerror("Error", "Please fill in all the details")
#         return
#     cv =PDFCV()
#     cv.generate_cv(name,email,address,phone,website,skills,work_experience,education,about_me)
#
#
#
#
#
#
#
#
#
# label_name =Label(window,text="Name: ")
# label_name.pack()
# entry_name=Entry(window)
# entry_name.pack()
#
# label_email =Label(window,text="Email: ")
# label_email.pack()
# entry_email=Entry(window)
# entry_email.pack()
#
# label_phone =Label(window,text="Phone: ")
# label_phone.pack()
# entry_phone=Entry(window)
# entry_phone.pack()
#
# label_address =Label(window,text="Address: ")
# label_address.pack()
# entry_address=Entry(window)
# entry_address.pack()
#
# label_website =Label(window,text="Website: ")
# label_website.pack()
# entry_website=Entry(window)
# entry_website.pack()
#
# label_skills =Label(window,text="Skills (Enter one skill per line) ")
# label_skills.pack()
# entry_skills=Text(window,height=3)
# entry_skills.pack()
#
# label_education =Label(window,text="Education(one per in line 'Degree':'University')")
# label_education.pack()
# entry_education=Text(window,height=3)
# entry_education.pack()
#
# label_experience =Label(window,text="Experience (one per in line 'Job Title':'Discription') ")
# label_experience.pack()
# entry_experience=Text(window,height=3 )
# entry_experience.pack()
#
# label_about=Label(window,text="About Me ")
# label_about.pack()
# entry_about=Text(window,height=3)
# entry_about.pack()
#
# button_generate=Button(window, text= 'Generate cv',command=generated_cv)
# button_generate.pack()
# window.mainloop()

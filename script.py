class Profile_widgets():
    def __init__(self, Gender="M", Company=None, blood_group=None, website=None, username=None, name=None, sex=None, address=None, Job=None, mail=None):
        self.gender = Gender
        self.company = Company
        self.bg = blood_group
        self.website = website
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.job = Job
        self.mail = mail
    def Create_profile(self):
        from faker import Faker
        faker = Faker()
        profile = faker.profile(sex=f"{self.gender}")
        del profile["ssn"]
        del profile["residence"]
        del profile["current_location"]
        del profile["birthdate"]
        if self.job != None: profile["job"] = self.job
        elif self.company != None: profile["company"] = self.company
        elif self.bg != None: profile["blood_group"] = self.bg
        elif self.website != None: profile["website"] = self.website
        elif self.username != None: profile["username"] = self.username
        elif self.name != None: profile["name"] = self.name
        elif self.sex != None: profile["sex"] = self.sex
        elif self.address != None: profile["address"] = self.address
        elif self.mail != None: profile["mail"] = self.mail
        result = list(profile.values())
        if self.website == None: result[3] = result[3][0]
        return result
    def Create_result(self, result):
        from tkinter import Tk, Frame, Label 
        from tkhtmlview import HTMLLabel
        from PIL import ImageTk, Image
        root = Tk()
        address = r"File\qr.png"
        img = ImageTk.PhotoImage(Image.open(address))
        qr = Label(root, image = img)
        label = HTMLLabel(root, html=f"""
____________________________________________
<br /> Created by <b>Tik Ten</b>
<br />Github: <b>github.com/tik-ten</b> 
<h3> Information: </h3>
Job: <b>{result[0]}</b> <br />
Company: <b>{result[1]}</b> <br />
Blood group: <b>{result[2]}</b> <br />
Website: <b>{result[3]}</b> <br />
Username: <b>{result[4]}</b> <br />
Name: <b>{result[5]}</b> <br />
Sex: <b>{result[6]}</b> <br />
Address: <b>{result[7]}</b> <br />
Mail: <b>{result[8]}</b> <br /> 
____________________________________________
""")
        label.pack(pady=20, padx=20)
        qr.pack()
        root.geometry("400x500")
        root.title("Your fake profile is ready!")
        root.mainloop()
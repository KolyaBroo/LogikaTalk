from customtkinter import *
from PIL import Image

class MenuAuth(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.geometry("950x500")
        self.title("LogiTalk")
        self.configure(fg_color="White")

        #--------------------------ВЕЛИКА ЧАСТИНА------------------------------
        self._set_appearance_mode("White")
        self.img = CTkImage(dark_image=Image.open(r"C:\Python\LogiTalk\welcome.jpg"),size=(570,270))
        self.img_lb = CTkLabel(self, image=self.img, text="")
        self.img_lb.pack(padx=10, side="left", fill="both")

        #---------------------------МАЛА ЧАСТИНА-------------------------------
        self.authframe = CTkFrame(self, width=380, height=500, fg_color="#D9FFFF")
        self.authframe.pack_propagate(False)
        self.authframe.pack(side="right", fill="y")
        self.txt = CTkLabel(self.authframe,text="АВТОРИЗАЦІЯ",text_color="#004046",font=("Arial", 30, "bold"))
        self.txt.place(relx=0.5, rely=0.5, y=-150, anchor="center")
        self.txt = CTkLabel(self.authframe,text="LogiTalk-Version: Test 0.0.1",text_color="Black",font=("Arial", 10, "bold"))
        self.txt.place(relx=0.5, rely=0.5, y=160, anchor="center")
        self.inp_name = CTkEntry(self.authframe,width=250,height=40,placeholder_text="👤 - Логін",fg_color="#3FD5FF",placeholder_text_color="Black",text_color="Black")
        self.inp_name.place(relx=0.5, rely=0.5, y=-80, anchor="center")
        self.host_pass = CTkEntry(self.authframe,width=250,height=40,placeholder_text="💬 - Хост",fg_color="#00BFFF",placeholder_text_color="Black",text_color="Black")
        self.host_pass.place(relx=0.5, rely=0.5, y=-20, anchor="center")
        self.port_pass = CTkEntry(self.authframe,width=250,height=40,placeholder_text="🔒 - Порт",fg_color="#00BFFF",show="*",placeholder_text_color="Black",text_color="Black")
        self.port_pass.place(relx=0.5, rely=0.5, y=40, anchor="center")
        self.show_btn = CTkButton(self.authframe,text="👁",width=40,command=self.toggle_password,fg_color="#00BFFF",text_color="Black",bg_color="#00BFFF")
        self.btn_log = CTkButton(self.authframe,width=250,height=45,text="УВІЙТИ",corner_radius=10,fg_color="#0087B5", command=self.go_to_app)
        self.btn_log.place(relx=0.5, rely=0.5, y=100, anchor="center")
        self.show_btn.place(relx=0.5, rely=0.5, x=80, y=27)
        #self.show_btn.place(relx=0.5, x=260, y=237)
    def toggle_password(self):
        if self.port_pass.cget("show") == "":
            self.port_pass.configure(show="*")
        else:
            self.port_pass.configure(show="")
    def go_to_app(self):
        self.env={"name":self.inp_name.get(),"host":self.host_pass.get(),"port":int(self.port_pass.get())}
        self.destroy()
if __name__ == "__main__":
    MenuAuth().mainloop()
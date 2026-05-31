from customtkinter import *
from PIL import Image
import LogiTalkAuth
import socket
import threading

win = LogiTalkAuth.MenuAuth()
win.mainloop()
env = win.env
class Window(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("950x500")
        self.title("LogikaTalk")
        self.name = env.get("name","anonim")
        self.text = CTkTextbox(self,width=650,height=480,text_color="Red")
        self.text.configure(state="disabled")
        self.text.pack(side="right",pady=5, padx=5)
        self.sent_text = CTkEntry(self,width=400,placeholder_text="Введіть повідомлення")
        self.sent_text.place(x=350,y=450)
        self.sent = CTkButton(self,text="Відправити",command=self.sent_message)
        self.sent.place(x=770,y=450)
        
        self.profile_name = CTkLabel(self,text=env.get("name"))
        self.profile_name.pack(padx=100,side="right")
        self.img = CTkImage(dark_image=Image.open(r"C:\Python\LogiTalk\default_profile.jpg"),size=(300,400))
        self.img_lb = CTkLabel(self, text="")
        self.img_lb.pack(padx=7)
        
        self.host = env.get("host")
        self.port = env.get("port")
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.connect((self.host,self.port))
            self.sock.send(f"TEXT@{self.name}@{self.name} приєднався\n".encode())
            threading.Thread(target=self.recv_msg,daemon=True).start()
        except:
            self.add_message("Не вдається підключитись до сервера")
    
    def recv_msg(self):
        buffer = ""
        while True:
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buffer+=chunk.decode(errors="ignore")
                while "\n" in buffer:
                    line,buffer = buffer.split("\n", 1)
                    self.handle_line(line.strip())
            except:
                print("Server error")
        self.sock.close()

    def handle_line(self,line):
        if not line:
            return
        parts = line.split("@", 3)
        msg_type = parts[0]
        if msg_type == "TEXT":
            if len(parts) >= 3:
                author = parts[1]
                message = "@".join(parts[2:])
                self.add_message(f"{author} : {message}")
        elif msg_type == "PIC":
            pass
    
    def add_message(self, text):
        self.text.configure(state="normal")
        self.text.insert(END,text+"\n")
        self.text.configure(state="disabled")
    
    def sent_message(self):
        message = self.sent_text.get()
        if message:
            self.add_message(f"{self.name}: {message}")
            data = f"TEXT@{self.name}@{message}\n"
            try:
                self.sock.send(data.encode())
            except:
                print("Error")
        self.sent_text.delete(0,END)
    
    def sent_pic(self):
        path = r"namepic"
        with open(path, "rb") as pic:
            data = pic.read()
        print(data)

Window().mainloop()

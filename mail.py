from email import message
import smtplib
import sys
import os
from email.message import EmailMessage
import time
from tkinter import messagebox
import pyfiglet
import socket as ip

os.system("clear")
host = ip.gethostname()
if sys.platform == "linux":
    pass
else:
    print("THIS PROGRAM ONLY WORKS ON LINUX.\nClosing Program...")
    sys.exit(0)
class renk:
        BLACK = "\033[90m"
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        RED = '\033[31m'
        PURPLE = '\033[95m'
        YELLOW = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        BGRED = '\033[41m'
        BGREEN = '\033[42m'
        BGYELLOW = '\033[43m'
        BGBLUE = '\033[44m'
        BGPURPLE = '\033[45m'
        WHITE = '\033[37m'
        ALERT = '\033[5m'
print(renk.BOLD+renk.YELLOW)
os.system("figlet -c Isma1ll")
print(renk.BOLD+renk.GREEN+"""
                            ========================
                            ## github.com/isma1ll ##
                            ========================
"""+renk.ENDC)
def main():
    def t():
        current_time = time.localtime()
        ctime = time.strftime('%H:%M:%S', current_time)
        return '[' + ctime + ']'
        
    try:
        Sender_Email = input(renk.BOLD+renk.BLUE+"[>] Your E-Mail Adress:"+renk.BOLD+renk.PURPLE+renk.ENDC)
        Password = input(renk.BOLD+renk.BLUE+"[>] Your 2-Step Authantication Code:"+renk.ENDC+renk.BOLD+renk.PURPLE+renk.ENDC)
        if Sender_Email == "" and Password == "":
            print("Please Enter Your E-Mail Adress And 2-Step Verification Code.")
            os.system("python mail.py")
        
        Reciever_Email = input(renk.BLUE+renk.BOLD+"[>] Reciever e-mail Adress: "+renk.ENDC)
    except KeyboardInterrupt:
        print(renk.BOLD+renk.RED+renk.ALERT+f"""
{t()} [!] USER PRESS CTRL+C PROGRAM CLOSING..."""+renk.ENDC)
        sys.exit()
    
    try:
        s = input(renk.BOLD+renk.BLUE+renk.BLUE+"[>] Enter The Subject:"+renk.ENDC)
        m = input(renk.BOLD+renk.PURPLE+renk.BLUE+"[>] Enter Your Message:"+renk.ENDC)
    except KeyboardInterrupt:
        print(renk.BOLD+renk.RED+renk.ALERT+t()+"""
[!] USER PRESS CTRL+C PROGRAM CLOSING..."""+renk.ENDC)
        sys.exit()
    
    newMessage = EmailMessage()                         
    newMessage['Subject'] = s.format() 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email.format()            
    newMessage.set_content(m.format()) 
    fi = input(renk.PURPLE+renk.BOLD+"[*] Enter File Name Or File Path:"+renk.ENDC)
    if fi == "":
        print(renk.RED+renk.BOLD+"The file part has been left blank!\nAre you sure it will be continued?"+renk.ENDC)
        input(renk.ALERT+renk.BOLD+renk.BLUE+"Press Enter To Continue."+renk.ENDC)
    else:
        if os.path.exists(fi.format()) != True:
            print("No such file was found.")
            s = input("Do You Want to Continue?y/n: ")
            if s == "y":
                pass
            elif s == "n":
                print(renk.ALERT+renk.BOLD+renk.RED+"Program Closing...")
                time.sleep(3)
                print(renk.GREEN+renk.BOLD+"Restarting program..."+renk.ENDC)
                time.sleep(1)
                os.system("python mail.py")
                sys.exit()
        else:
            print(renk.BOLD+renk.GREEN+"{} File found.\n".format(fi)+renk.ALERT+renk.YELLOW+renk.BOLD+"Adding to your message.."+renk.ENDC)
            files = ['{}'.format(fi)]
            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            try:
                smtp.login(Sender_Email,Password)
                print(renk.BOLD+renk.GREEN+f"{t()} [$] Successfuly log in {Sender_Email}"+renk.ENDC)
            except smtplib.SMTPAuthenticationError:
                print(renk.BOLD+t()+renk.RED+"""
[!] An error has occurred!
[!] Your 2-step verification code is incorrect. Please Create a New One or Try Again.
            """+renk.ENDC)
                sys.exit() 
            try:
                smtp.send_message(newMessage)
                print(renk.BOLD+renk.GREEN+t()+" [$] Your message has been sent to {}!".format(Reciever_Email)+renk.ENDC)
                time.sleep(3)
                with open("log.txt","a") as f:
                    if fi == "" or m == "" or s == "":
                        fi = "No Files Selected."
                        s = "No Subject"
                        m = "No Message"
                    
                    f.write("When: "+t()+"""
    ================================
    Sender~${}
    Reciever~${}
    File Name~${}
    Subject~${}
    Message~${}
    Host Name~${}
    ================================
                    

            """.format(Sender_Email,Reciever_Email,fi,s,m,host))
                
            
                time.sleep(1)
            except:
                print(renk.BOLD+renk.RED+"""
    [!] An error has occurred!"""+renk.GREEN+"""
    [i] Maybe there is unwanted content in the File named {} or in the File Itself
    [i] Check This Website: https://support.google.com/mail/answer/6590?hl=en#zippy=%2Cmessages-that-have-attachments
                """.format(fi))
                time.sleep(1)
main()
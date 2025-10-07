#my code #my code

import requests #used to send http requests  cam fetch the html content of a webpage
from bs4 import BeautifulSoup  # can extract specific data on html or xml
import smtplib #for sending emails using smtp
from email.mime.text import MIMEText #creates plain text email content to specify the message body in text form.
from email.mime.multipart import MIMEMultipart #Purpose: Allows sending emails with multiple parts (text + attachments + HTML). Use case: If your email includes text + files, you wrap everything inside MIMEMultipart.
from email.mime.base import MIMEBase #Purpose: Used for handling attachments (binary data like images, PDFs, etc.). Use case: When attaching files to an email, MIMEBase is used to encode and attach them.
from email import encoders #Purpose: Provides encoding functionality for email attachments.Use case: Converts the file into a format that can be sent via email safely (e.g., base64).
import os #Work with files, directories, and paths (create folders, list files, check if file exists, etc.).

class news_scraper:
    def __init__(self):
        self.headlines=[]
        self.img_urls=[]



    def scrap_headlines(self):
        url="https://www.bbc.com/"
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        self.headlines=soup.find_all("h2")
        
    def save_headlines(self):
        with open("headlines.txt","w",encoding="utf-8") as file:
            for i,headline in enumerate(self.headlines,start=1):
                file.write(f"{i}.{headline.text}\n")
        print(f"headlines saved to file")        
            

    def send_headlines_mail(self):
        sender="dilshan9532@gmail.com"
        receiver="msha02615@gmail.com"
        password="qrki eijy webp jhla"

        with open("headlines.txt","r",encoding="utf-8") as file:
            line=file.readlines()
        content="".join(line)

        msg=MIMEText(content,"plain","utf-8")
        msg["subject"]="BBC NEWS"
        msg["from"]=sender
        msg["to"]=receiver

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string()) 

        print("mail sent")               

    def scrape_images(self):
        url="https://www.bbc.com/"
        response=requests.get(url)
        response.raise_for_status()
        soup=BeautifulSoup(response.text,"html.parser")
        img_tags=soup.find_all("img")

        self.img_urls = []
        for img in img_tags:
            src = img.get("src")
            if src:
                if src.startswith("http"):     # absolute URL
                    self.img_urls.append(src)
                elif src.startswith("/"):      # relative URL
                    base_url = url.rstrip("/")
                    self.img_urls.append(base_url + src)

        self.img_urls=self.img_urls[:10]            

        print(f"🔎 Found {len(self.img_urls)} images")


    def save_images(self,folder="images"):
        os.makedirs(folder,exist_ok=True) 

        for i,url in enumerate(self.img_urls,start=1):
            try:
                img_data=requests.get(url).content
                filename=os.path.join(folder,f"image_{i}.jpg") 
                with open(filename,"wb") as file:
                    file.write(img_data)
                print(f"saved {filename}")
            except Exception as e:
                print(f"could not save {url}-{e}") 

    def send_images_mail(self ,subject="Scraped Images", folder="images"):

        sender="dilshan9532@gmail.com"
        receiver="msha02615@gmail.com"
        password="qrki eijy webp jhla"

    
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Email body
        msg.attach(MIMEText("Here are the scraped images.", "plain"))

        # Attach all images from the folder
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath) and filename.lower().endswith((".jpg", ".png", ".jpeg")):
                with open(filepath, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={filename}")
                msg.attach(part)

        # Send via Gmail SMTP
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, msg.as_string())
            print("📧 Email with images sent successfully!")
        except Exception as e:
            print("❌ Error sending email:", e)
    






myobj=news_scraper()
myobj.scrap_headlines()
myobj.save_headlines()
myobj.send_headlines_mail()
myobj.scrape_images()
myobj.save_images()
myobj.send_images_mail()
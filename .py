import subprocess
import tkinter as tk
import threading
import urllib.request
import json

class CmdThread (threading.Thread):
   def __init__(self, textvar):
        threading.Thread.__init__(self)
        self.command = f"java -jar {soft}.jar"
        self.textvar = textvar
        run()

def run(self, version="Latest", software="Spigot"):
    global soft
    with urllib.request.urlopen("https://raw.githubusercontent.com/sonyakun/MCBuilder-Data/main/versions.json") as version_json:
        data = version_json.read()
        with open("./json_data/versions.json", mode='wb') as local_file:
            local_file.write(data)
            versions_json = open('./json_data/versions.json', 'r')
            versions_load = json.load(versions_json)
            if version == "Latest":
                soft = version + "-" + software
            else:
                soft = f"{software}{version}"
            url = versions_load[soft]
            urllib.request.urlretrieve(url, './soft.jar')
            if software == "Paper":
                proc = subprocess.Popen(self.command, stdout=subprocess.PIPE)
            else:
                proc = subprocess.Popen(self.command2, stdout=subprocess.PIPE)
        while not proc.poll():
            data = proc.stdout.readline()
            if data:
                print(data)
                self.textvar.set(data)
            else:
                break

root = tk.Tk()
root.geometry("400x100")
root.title("main window")
text = tk.StringVar()
label = tk.Label(textvariable=text)
label.pack()

thread = CmdThread(['netstat'], text)
thread.start()

#サブ画面
sub_window = tk.Toplevel()
sub_window.title("sub window")
sub_window.geometry("400x100")

root.mainloop()

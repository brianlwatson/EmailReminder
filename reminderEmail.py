import Tkinter
import datetime
import smtplib
from email.mime.text import MIMEText

GMAIL = 'smtp.gmail.com'
GMAIL_PORT = 587


class BugScript(object):
	def __init__(self, root):
		self.reminder_active = 0

		self.username=""
		self.destname=""
		self.password=""
		self.subject =""
		self.message=""
		self.msg     ={}

		self.lUser    = Tkinter.Label(root, text="Username: ").grid(row=0)
		self.lPass    = Tkinter.Label(root, text="Password: ").grid(row=1)
		self.lTo      = Tkinter.Label(root, text="To: ").grid(row=2)
		self.lSubject = Tkinter.Label(root, text="Subject: ").grid(row=3)
		self.lMessage = Tkinter.Label(root, text="Message: ").grid(row=4)

		self.fUser	=Tkinter.Entry(root)
		self.fUser.grid(row=0,column=1,columnspan=2)
		self.fPass	=Tkinter.Entry(root, show="*")
		self.fPass.grid(row=1,column=1,columnspan=2)
		self.fDest	=Tkinter.Entry(root)
		self.fDest.grid(row=2,column=1,columnspan=2)
		self.fSubject=Tkinter.Entry(root)
		self.fSubject.grid(row=3,column=1,columnspan=2)
		self.fMessage=Tkinter.Text(root)
		self.fMessage.grid(row=4,column=1, columnspan=2)
		Tkinter.Button(root, text = 'Submit', command = self.sendMessage).grid(row=5)
		self.activeButton = Tkinter.Button(root, text = 'ACTIVE', command = self.toggleDisable)
		self.activeButton.grid(row=5, column=2)
		self.activeButton.configure(bg="red")
	def sendMessage(self):
		self.setValues()

	def sendEmail(self, user, pwd, recipient, subject, body):
	    recip = recipient if type(recipient) is list else [recipient]

	    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	    """ % (user, ", ".join(recip), subject, body)

	    print message

	    try:
	        server = smtplib.SMTP(GMAIL, GMAIL_PORT)
	        server.ehlo()
	        server.starttls()
	        server.login(user, pwd)
	        server.sendmail(user, recipient, message)
	        server.close()
	        print 'successfully sent the mail'
	    except:
	        print "Failed to send mail"
		
	def setValues(self):
		self.username = self.fUser.get()
		self.password = self.fPass.get()
		self.destname = self.fDest.get()
		self.subject =  self.fSubject.get()
		self.message = self.fMessage.get("1.0", "end-1c")
		self.reminder_active = 1

		self.sendEmail(self.username, self.password, self.destname, self.subject, self.message)

	def toggleDisable(self):
		self.reminder_active = not self.reminder_active
		if self.reminder_active:
			print "0"
			self.activeButton = Tkinter.Button(root, text = 'ACTIVE', command = self.toggleDisable)
			self.activeButton.configure(bg="red")
		else:
			print "1"
			self.activeButton = Tkinter.Button(root, text = 'INACTIVE', command = self.toggleDisable)
			self.activeButton.configure(bg="green")

root = Tkinter.Tk()
root.title("BugScript")
bs = BugScript(root)
root.mainloop()


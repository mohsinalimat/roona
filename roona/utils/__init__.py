import urllib.request
import urllib.parse
import frappe

def sendSMS(numbers, message):
    sendSMSTextLocal()

def sendSMSTextLocal(self):
    """
        resp =  sendSMS('apikey', '918123456789',
        'Jims Autos', 'This is your message')
        print (resp)

    """
    testlocal_settings = frappe.get_single("Textlocal Setting")

    data =  urllib.parse.urlencode({'apikey': testlocal_settings.apikey, 'numbers': self.numbers,
        'message' : self.message, 'sender': testlocal_settings.default_sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
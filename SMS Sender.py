from twilio.rest import Client

ACOUNT_SID = 'ACfad4296c81b0cfddfe73cd796d368905'
AUTH_TOKEN = '47af17496bcbc10f2a793cf8ef899479'
TWILIO_PHONE = '+18606501959'
MY_PHONE = '+919867499710'

client = Client(ACOUNT_SID, AUTH_TOKEN)

def sendSMS(message, to_phone):
    data = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=to_phone
    ) 
    print(data)

sendSMS("Lol works only for verfied acc in twilio!", MY_PHONE)

from twilio.rest import Client

client = Client("AC8c***************", "AUTH_TOKEN")

try:
    client.messages.create(to="+263717522510",from_="+19387777419",body="Hi from Blessed.")
    print("Message Sent!!!")
except:
    print("Message Not Sent!!!")


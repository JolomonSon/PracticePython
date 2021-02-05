from twilio.rest import TwilioRestClient
from credentials import accountSID,  authToken, cellNumber, twilioNumber

client = TwilioRestClient(accountSID, authToken)

myMsg = 'You message here..'

message = client.messages.create(to=myCell, from_=myTwilio, body=myMsg)
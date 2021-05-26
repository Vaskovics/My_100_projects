from twilio.rest import Client

TWILIO_SID = "ACfb14f346953d61ac3759ace3638dde53"
TWILIO_AUTH_TOKEN = "96d74541092d27e7f3c3952c4eb12f5c"
TWILIO_VIRTUAL_NUMBER = "************"
TWILIO_VERIFIED_NUMBER = "************"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

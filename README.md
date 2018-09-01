
from twilio.rest import Client

account_sid = 'ACf898edea7a622a627a21b0d0debe012c'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+13478433231',
                        from_='+17868977089'
                    )

print(call.sid)

from twilio.rest import client
from twilio.twiml.voice_response import Say, VoiceResponse, Dial, Gather
from gtts import gTTS
import os

response = VoiceResponse()

account_sid = 'ACf898edea7a622a627a21b0d0debe012c'
auth_token = '071c18ce6d17dea36a79d29da83f7052'
client = Client(account_sid, auth_token)

call = client.calls.create(
    to='+13474398136',
    from_='+16312397132',
    URL= 'http://static.fullstackpython.com/phone-calls-python.xml')

tts = gTTS(text="Hello", lang="en")
speech.say("I am calling you to remind you to take you medication")
speech.say("Press one to take the first pill")
say.ssml_break(strength='x-weak', time='10s')

gather = Gather(action='/process_gather.php', method='GET')
gather.say("You took your first pill. Please press number two and take your second pill,\nfollowed by the pound sign")
response.append(gather)
response.say('We didn\'t receive any input. Please take your first pill then press two')

gather = Gather(action='/process_gather.php', method='GET')
gather.say('Please press number three,\nfollowed by the pound sign')
response.append(gather)
response.say('We didn\'t receive any input. Please take your second pill then press three')

gather = Gather(action='/process_gather.php', method='GET')
gather.say('Please press number four,\nfollowed by the pound sign')
response.append(gather)
response.say('We didn\'t receive any input. Please take your third pill then press four')


print(response)







 










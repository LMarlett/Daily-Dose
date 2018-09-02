from twilio.rest import TwilioRestClient

TWILIO_PHONE_NUMBER = "+16312397132"


DIAL_NUMBERS = ["+13474398136",]

TWIML_INSTRUCTIONS_URL = \
  "file:///Users/tiffany.truong/Desktop/Coding.xml"

client = TwilioRestClient("ACf898edea7a622a627a21b0d0debe012c", "071c18ce6d17dea36a79d29da83f7052")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)

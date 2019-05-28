import os
import getbusjson
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_parse_request():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    msg = 'Error: No Message'

    if "go home" not in body.lower() and "go work" not in body.lower():
        msg = send_generic_message()
    else:
        bothflag = False
        if "go home" in body.lower():
            msg = send_home_info()
            bothflag = True
        if "go work" in body.lower():
            if bothflag:
                msg += send_work_info()
            else:
                msg = send_work_info()

    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Signature
    msg +="\nEmail bcai@twilio.com to report any bugs (: :)"

    # Add a message
    resp.message(msg)

    return str(resp)

def send_generic_message():
    message = "\nHello 2019 Twilio Intern\n"
    message += "Text \"Go Home\" or \"Go Work\" for the F Line Bus Times"
    return message

def send_home_info():
    return getbusjson.go_home()

def send_work_info():
    return getbusjson.go_beale_st()

if __name__ == "__main__":
    app.run(debug=True)


import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        # This is the first request. Note how we start the response with CON
        response = "CON Welcome to Teketeke\n" \
                   "1. To book\n" \
                   "2. To pay"

    elif text == '1':
        # User selected booking option
        response = "CON Select pick up point\n"

    elif text == '2':
        # User selected payment option
        response = "CON Show current trip and cost\n" \
                   "1. Agree\n" \
                   "2. STK push"

    elif text == '1*1':
        # This is a second level response where the user selected 1 in the first instance
        # Business logic for booking
        booking_id = generate_booking_id()  # Implement this function to generate booking ID
        send_confirmation_sms(phone_number, booking_id)  # Implement this function to send SMS confirmation
        response = "END Booking confirmed. Your booking ID is: {}".format(booking_id)

    elif text == '2*1':
        # User agreed to pay
        # Business logic for payment
        response = "END Payment confirmed. Thank you!"

    elif text == '2*2':
        # User selected STK push
        # Business logic for initiating STK push
        response = "END STK push initiated. Please check your phone for payment prompt."

    else:
        # Invalid choice
        response = "END Invalid choice"

    # Send the response back to the API
    return response

def generate_booking_id():
    # Implement logic to generate a unique booking ID
    return "BK123456"

def send_confirmation_sms(phone_number, booking_id):
    # Implement logic to send SMS confirmation to the user
    pass  # Placeholder, replace with actual implementation

if __name__ == '__main__':
    app.run(debug=True)

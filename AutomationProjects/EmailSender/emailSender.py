import requests

# specify the Mailgun API endpoint and credentials
MAILGUN_API_ENDPOINT = "https://api.mailgun.net/v3/sandbox68dd52764e6b414187f809166e2fc5b1.mailgun.org/messages"
MAILGUN_API_KEY = 'your api key'

# define a function to send an email
def send_email(to, subject, body):

    # create a dictionary with the email data
    data = {
        # ! Fill in
        'from': 'brucosta2002@gmail.com',
        'to': to,
        'subject': subject,
        'text': body
    }

    # send a POST request to the Mailgun API endpoint
    response = requests.post(
        MAILGUN_API_ENDPOINT,
        auth=('api', MAILGUN_API_KEY),
        data=data
    )

    # check if the request was successful
    if response.status_code == 200:
        print('Email sent successfully!')
    else:
        print('An error occurred while sending the email.')

# example usage - ! Fill in
to = "brucosta2002@gmail.com"
subject = 'HI'
body = 'Hello '
send_email(to, subject, body)
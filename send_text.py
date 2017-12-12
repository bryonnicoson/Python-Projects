from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC325ecf211e8aea83502968dbfd013731"
auth_token  = "2c09517b6bc7326fdb447c548c468ee1"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello.",
    to="+13094446180",    # Replace with your phone number
    from_="+13093401265") # Replace with your Twilio number
print(message.sid)

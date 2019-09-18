 import requests
  
  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "BusinessShortCode": " ",
    "Password": " ",
    "Timestamp": " ",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": " ",
    "PartyA": " ",
    "PartyB": " ",
    "PhoneNumber": " ",
    "CallBackURL": "https://ip_address:port/callback",
    "AccountReference": " ",
    "TransactionDesc": " "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
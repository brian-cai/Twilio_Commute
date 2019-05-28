# Twilio Intern Bus Commute SMS Bot
Text 470-288-3613 to get the bus routes.

`Text "Go Home" or "Go Work" for the F Line Bus Times`

## Cloning this Application
The bus route was from Emeryville to Salesforce Transit Center. Those 2 locations are hard coded. If you want to clone this application you will need to replace those locations in the API request.

1. Get a AC Transit Token [here](http://api.actransit.org/transit/Account/Register)

You will need your own token.txt file that has your token in it like this:
`?token=ABCDEF1234567890`

2. Clone repository

`git clone https://github.com/<repository>.git`

3. Change stops in API request within the code appropriately

To change your stops, just find your stop number and replace it with the appropriate stop number.
`r = requests.get("https://api.actransit.org/transit/stops/50242/predictions" + token.read())`

becomes

`r = requests.get("https://api.actransit.org/transit/stops/{YOUR_STOP_NUMBER}/predictions" + token.read())`

## Tools
* Twilio SMS
* Flask
* [AC Transit API](http://api.actransit.org/transit/)

## Deployment
* Heroku
* Gunicorn

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os

url = "https://worldcup.sfg.io/matches/country?fifa_code="

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
 'ARG', 'AUS', 'BEL', 'BRA', 'CAN', 'CHI', 'CIV', 'CMR', 'CRC', 
 'CRO', 'CUB', 'CZE', 'DEN', 'ECU', 'EGY', 'ESP', 'FRA', 'GER', 'GHA',
  'GRE', 'HON', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'KSA', 'KUW',
   'MAR', 'NGA', 'NED', 'NIR', 'NOR', 'NZL', 'PAR', 'PER', 'POR', 'ROU',
    'RUS', 'SCO', 'SRB', 'SUI', 'SWE', 'TUN', 'TUR', 'URU', 'USA', 'VEN',
     'WAL', 'ZAM']

app = Flask(__name__)

@app.route("/",methods=['GET'])
def sms():
    body = request.values.get("body", "")
    print("***********************")
    print(body)
    print("***********************")
    resp = MessagingResponse()

    if body.upper() in countries:
        get_req = requests.get(url+ body).json()
        headline = "\n -- Past Matches -- \n"


        for m in get_req:
            if m["status"] == "completed":
               headline += f"{m['home_team']['country']} {m['home_team']['goals']} vs {m['away_team']['country']} {m['away_team']['goals']}\n"

        
        resp.message(headline)
        print(resp)
    return str(resp)



if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host="localhost", port=port)
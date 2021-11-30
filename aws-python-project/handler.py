import json
import arrow
import requests


def hello(event, context):
    datetime = arrow.now().shift(hours=2)

    response = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast", params={
        "datetime": datetime
    })

    body = response.json()
    forecasts = body['items'][0]['forecasts']

    return {"statusCode": 200, "body": forecasts}

import requests

parameters={
    "amount":20,
    "category":18,
    "type":"boolean"

}

response=requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data=response.json()

question_data=data['results']

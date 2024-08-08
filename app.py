from flask import Flask,request,jsonify
import requests

app=Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency']['currency']
    amount=data['queryResult']['parameters']['unit-currency']['amount']
    target_currnecy=data['queryResult']['parameters']['currency-name']

    cf=fetch_conversion_factor(source_currency,target_currnecy)
    final_amount=amount*cf
    final_amount=round(final_amount,2)
    response={
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currnecy)
    }
    return jsonify(response)

def fetch_conversion_factor(source,target):
    url="https://v6.exchangerate-api.com/v6/5c5c29ec8e3a399172dfc233/pair/{}/{}".format(source,target)
    response=requests.get(url)
    data=response.json()
    if 'conversion_rate' in data:
        return data['conversion_rate']
    else:
        None
# if __name__=="__main__":
#     app.run(debug=True) 
    
    
    
    
#we used ngrok (as chatbot running on google server which is on9 & hamar code of9) to ngrok hamar of9 code co bhi on9 rakhta hai kuch samay k liye it is a software
#jo ham code likh rhe dialogflow use webhook bolta hai
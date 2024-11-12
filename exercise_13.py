from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/prime_number')
def find_prime():
    args = request.args
    number = int(args.get("number"))
    is_prime = False
    if number == 0 or number == 1:
        pass
    elif number > 1:
        for i in range(2,number):
            if(number % i) == 0:
                break
        else:
            is_prime = True
        
    response = {
        "number": number,
        "isPrime": is_prime
    }
    return json.dumps(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
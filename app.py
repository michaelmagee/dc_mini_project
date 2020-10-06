import os
from flask import Flask

#  These are the environments that this will run in 
#environment = "flask"
#datafile = "flask/data/company.json"
#-
environment = "vscode"
#datafile = "data/company.json"
#-
#environment = "heroku"
#datafile = "data/company.json"

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Hello World  ....again  </h1>"



"""
    Select the correct environment 
"""
if environment == "flask":
    if __name__ == '__main__':
        app.run(use_debugger=False, use_reloader=False,
                passthrough_errors=True)

elif environment == "vscode":
    if __name__ == '__main__':
        app.run(use_debugger=False, use_reloader=False,
                passthrough_errors=True)

elif environment == "heroku":
    if __name__ == '__main__':
        url = host = os.environ.get('IP')
        port = os.environ.get('PORT')

        app.run(host=os.environ.get('IP'),
                port=int(os.environ.get('PORT')),
                debug=True)

else:
    print(" Unknown environment")

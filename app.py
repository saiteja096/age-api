from flask import Flask
from flask_restful import Api
from resources.emp import Profile

app=Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS']=True
api=Api(app)
api.add_resource(Profile,'/profile')




if __name__=='__main__':
    app.run()
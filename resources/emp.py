from flask_restful import Resource,reqparse
from db import query
from werkzeug.security import safe_str_cmp
from datetime import datetime

class Profile(Resource):
    def get(self):
        try:
            return query("""SELECT * FROM user""")
        except:
            return {"message":"There was an error connecting to user table."},500

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('name',type=str,required=True,help="name cannot be left blank!")
        parser.add_argument('gender',type=str,required=True,help="gender cannot be left blank!")
        parser.add_argument('age',type=int,required=True,help="age cannot be left blank!")
        parser.add_argument('pref_r_age',type=int,required=True,help="pref_r_age cannot be left blank!")
        parser.add_argument('income',type=int,required=True,help="income cannot be left blank!")
        parser.add_argument('incomerate',type=int,required=True,help="incomerate cannot be left blank!")
        parser.add_argument('expenditure',type=int,required=True,help="expenditure cannot be left blank!")
        parser.add_argument('savingsrate',type=int,required=True,help="savingsrate cannot be left blank!")
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO user (name,gender,age,pref_r_age,income,incomerate,expenditure,savingsrate)
                                                    VALUES('{data['name']}',
                                                        '{data['gender']}',
                                                        {data['age']},
                                                        {data['pref_r_age']},
                                                        {data['income']},
                                                        {data['incomerate']},
                                                        {data['expenditure']},
                                                        {data['savingsrate']})""")
        except Exception as e:
            return {"message":"There was an error inserting into user table."+str(e)+""},500

        return {"message":"Successfully Inserted."},201

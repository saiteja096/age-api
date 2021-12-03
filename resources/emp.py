from flask_restful import Resource,reqparse
from db import query
from werkzeug.security import safe_str_cmp
from datetime import datetime
from flask_cors import CORS 
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
        parser.add_argument('age',type=str,required=True,help="age cannot be left blank!")
        parser.add_argument('pref_r_age',type=str,required=True,help="pref_r_age cannot be left blank!")
        parser.add_argument('income',type=str,required=True,help="income cannot be left blank!")
        parser.add_argument('incomerate',type=str,required=True,help="incomerate cannot be left blank!")
        parser.add_argument('expenditure',type=str,required=True,help="expenditure cannot be left blank!")
        parser.add_argument('savingsrate',type=str,required=True,help="savingsrate cannot be left blank!")
        data=parser.parse_args()
        try:
            data['age']=int(data['age'])
            data['pref_r_age']=int(data['pref_r_age'])
            data['income']=int(data['income'])
            data['incomerate']=int(data['incomerate'])
            data['expenditure']=int(data['expenditure'])
            data['savingsrate']=int(data['savingsrate'])
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

        return {"success":"Successfully Inserted."},201

def inf_grow(i,j):
    i = i + (j/100)*i
    return i

class Age(Resource):
    def get(self):
        try:
            return query("""SELECT * FROM user""")
        except:
            return {"message":"There was an error connecting to user table."},500

    def post(self):
        try:
            parser=reqparse.RequestParser()
            parser.add_argument('name',type=str,required=True,help="name cannot be left blank!")
            parser.add_argument('gender',type=str,required=True,help="gender cannot be left blank!")
            parser.add_argument('age',type=str,required=True,help="age cannot be left blank!")
            parser.add_argument('pref_r_age',type=str,required=True,help="pref_r_age cannot be left blank!")
            parser.add_argument('income',type=str,required=True,help="income cannot be left blank!")
            parser.add_argument('incomerate',type=str,required=True,help="incomerate cannot be left blank!")
            parser.add_argument('expenditure',type=str,required=True,help="expenditure cannot be left blank!")
            parser.add_argument('savingsrate',type=str,required=True,help="savingsrate cannot be left blank!")
            data=parser.parse_args()
            income = int(data['income'])
            expense = int(data['expenditure'])
            saving_rate = int(data['savingsrate'])
            inflation = int(data['incomerate'])
            growth = int(data['incomerate'])
            a = int(data['age'])
            total_saving = 0

            saving = income - expense
            total_saving = total_saving + saving


            for age in range(a+1,86):
                print("Age = "+str(age))
                income = inf_grow(income,inflation)
                expense = inf_grow(expense,inflation)
                rate_return = (10/100)*total_saving
                saving = income - expense
                total_saving = int(total_saving + saving + rate_return)
                print("cashflow = " + str(total_saving))

                n_total_saving = total_saving
                n_rate_return = rate_return
                n_expense = expense

                for j in range(age+1,86):
                    n_total_saving = int(n_total_saving - n_expense + n_rate_return)
                    n_rate_return = (10/100)*n_total_saving
                    n_expense = inf_grow(n_expense,inflation)
                    if n_total_saving < 0:
                        print("If retired at age = " + str(age) + " Savings completed at the age = " + str(j))
                        break
                if  n_total_saving >0:
                    return {"success":str(age)},201
        except Exception as e:
            return {"message":"There was an error inserting into user table."+str(e)+""},500
class Chart(Resource):
    def post(self):
        return {"yaxis":[70,68,65,60,55,50,45,40,35,32]},201

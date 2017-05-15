from flask import Flask, render_template, request
from flask_recaptcha import ReCaptcha
import sqlite3 as sql
app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         email = request.form['email']
         phone = request.form['phone']
         college = request.form['college']
         dep = request.form['dep']
         facad = request.form['facad']
         hod = request.form['hod']
         dean = request.form['dean']
         father = request.form['father']
         fathermob = request.form['fathermob']
         mother = request.form['mother']
         mothermob = request.form['mothermob']
         

         
         
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,email,phone,college,dep,facad,hod,dean,father,fathermob,mother,mothermob) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(nm,email,phone,college,dep,facad,hod,dean,father,fathermob,mother,mothermob) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()



if __name__ == '__main__':
   app.run(debug = True)
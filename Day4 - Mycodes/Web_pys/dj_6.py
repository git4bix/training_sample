from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
     return f'''
     <body bgcolor="lightblue">
     <h1 align="center" style="color:blue;"><a href="{url_for('login_get')}">Login Page</a></h1>
     </body>
 '''

@app.get('/login/')
def login_get():
    return """<html>
<head>
<style>
#myHeader {
  background-color: lightblue;
  color: black;
  padding: 40px;
  text-align: center;
} 
</style>
</head>
<body>
<h1 >Please Login</h1>
<form method="post" id="myHeader">
<table style="width:100%">
  <tr>
    <th><label for="username">Username:</label></th>
    <td><input type="text" name="username"><br></td>
    
  </tr>
  <tr>
    <th><label for="password">Password:</label></th>
    <td><input type="password" name="password"></td>
  </tr>
  <tr>
    <th><input type="submit" value="Login"></th> 
  </tr>
</table>
</form>
</body>
</html>
"""

def valid(username, password ):
    return (
        username == "admin"
        and password == "pass"
        )

@app.post('/login/')
def login_post():
    username = request.form['username']
    password = request.form['password']
    if valid(username, password ):
        return render_template('profile.html')
    else:
        return render_template('Denied.html')

app.run()
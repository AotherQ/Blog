from flask import*
from flask_session import*
from sqlite3 import*

app=Flask(__name__, static_folder='static/')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    return render_template('signin.html')


@app.route('/signin', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        name = request.form['uName']
        pas = request.form['uPassword']
        email = request.form['uEmail']

        con = connect("users.db")
        cursor = con.cursor()

        cursor.execute(("select * from users where Name=? and Password=? and Email=?"),(name, pas, email))

        liste = cursor.fetchall()

        if len(liste) > 0:
            a=1
            session["name"]=request.form.get("uName")
            session["pas"]=request.form.get("uPassword")
            # Burada giriş başarılı olduğunda yapılacak.
            
            
            return render_template('Home.html',a=a)

    return redirect(url_for('Home'))

@app.route('/save', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pas=request.form['password']


        con = connect("users.db")
        cursor=con.cursor()
        cursor.execute(("select * from users where Name=? or Password=? or Email=?"),(name,pas,email))
        liste = cursor.fetchall()
        l=list(liste)


        for b in l:
            if b[0]==name or b[1]==pas or b[2]==email:
                a=1
                return render_template('signup.html',a=a)
            
        

        else:
            if not liste:
                cursor.execute(("insert into users values(?,?,?)"),(name,pas,email))
            
        con.commit()
        return render_template('signup.html')

    return render_template('signup.html')

@app.route('/post', methods=['GET','POST'])
def post():
    if request.method=='POST':
        name=session.get("name")
        posta=request.form['post']
            
        con = connect("users.db")
        cursor=con.cursor()
        cursor.execute(("insert into post values(?,?)"),(name,posta))
                
        con.commit()
        return render_template('eposta.html',name=name,posta=posta)
    return render_template('eposta.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/1984')
def e():
    return render_template('1984.html')

@app.route('/animal-farm')
def animalfarm():
    return render_template('animal-farm.html')

@app.route('/nutuk')
def nutuk():
    return render_template('nutuk.html')

@app.route('/pageTwo')
def pageTwo():
    return render_template('pageTwo.html')

@app.route('/republic')
def republic():
    return render_template('republic.html')

@app.route('/sherlock')
def sherlock():
    return render_template('sherlock.html')

@app.route('/The-Brother-Karamazov')
def Thebro():
    return render_template('The-Brother-Karamazov.html')

@app.route('/the-socratic-method')
def thesoc():
    return render_template('the-socratic-method.html')

@app.route('/whitefang')
def whitefang():
    return render_template('whitefang.html')

if __name__== "__main__":

    app.run(debug=True)
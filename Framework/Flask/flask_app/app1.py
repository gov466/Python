from flask import Flask,render_template




app = Flask(__name__)

all_posts = [
	{
		'title':'post1 ',
		'content':'This is content of post 1'
	},
	{
		'title':'post2 ',
                'content':'This is content of post 2'

	}


]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
	return render_template('posts.html',posts =all_posts)

@app.route('/home/<string:name>')

def hello(name):
        return "HEllow , "+ name

if  __name__ == "__main__":
        app.run(debug= True)







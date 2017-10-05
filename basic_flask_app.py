from flask import Flask

app = Flask(__name__)

@app.route('/<name>', methods=['GET'])
def index(name):
	return f"hello, {name}!"
	
if __name__ == '__main__':
	app.run('0.0.0.0')

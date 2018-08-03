from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)

# SCSS Configuration
Scss(app, static_dir='static', asset_dir='assets')


# Routes
@app.route('/')
def main():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)

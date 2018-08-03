from flask import Flask, render_template
#from flask_scss import Scss

app = Flask(__name__, static_url_path='/static')

# SCSS Configuration
#Scss(app, static_dir='static', asset_dir='assets')


# Routes
@app.route('/')
def main():
    return render_template('/home.html')

@app.route('/terms-of-use')
def toc():
    return render_template('/terms-of-use.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('/privacy-policy')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import datetime
import requests

# initialize Flask app
app = Flask(__name__)

GENDER_API_ENDPOINT = 'https://api.genderize.io'
AGE_API_ENDPOINT = 'https://api.agify.io'


@app.route('/')
def home():
    current_year = datetime.date.today().year
    return render_template('index.html', year=current_year)


@app.route('/guess/<name>')
def guess(name):
    parameters = {
        'name': name
    }
    gender_api_response = requests.get(url=GENDER_API_ENDPOINT, params=parameters)
    gender_data = gender_api_response.json()['gender']
    age_api_response = requests.get(url=AGE_API_ENDPOINT, params=parameters)
    age_data = age_api_response.json()['age']
    return render_template('guess.html', person_name=name, person_gender=gender_data, person_age=age_data)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_post_endpoint = 'https://api.npoint.io/a07f053a8d856c53187b'
    blog_response = requests.get(url=blog_post_endpoint)
    blog_posts = blog_response.json()
    return render_template('blog.html', all_blog_posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)

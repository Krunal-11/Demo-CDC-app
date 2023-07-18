from flask import *
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def check():
    if request.method == 'POST':
        name = request.form['name']
        chefu = request.form['chefu']
        leetu = request.form['leetu']
        chefr = coderate(chefu)
        leetr = leetrate(leetu)
        return render_template('ranking.html', name=name, chefr=chefr, leetr=leetr)
    else:
        return render_template('index.html')


@app.route('/ranking')
def result():
    return render_template('ranking.html')


def coderate(chefu):
    url = f"https://www.codechef.com/users/{chefu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(class_="rating-number")
        if rank_element:
            rank = rank_element.get_text().strip()
            return rank
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to CodeChef."


def leetrate(leetu):
    url = f"https://leetcode.com/{leetu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")
        if rank_element:
            rank = rank_element.get_text().strip()
            return rank
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to LeetCode."


if __name__ == '__main__':
    app.run(debug=True)

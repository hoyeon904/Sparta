from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.articles.find({}, {'_id': 0}))

    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'articles':result})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # ajax에서 보낸 데이터 받기
    article_url = request.form['article_url']
    comment = request.form['comment']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(article_url,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')


    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    #몽고DB에 저장할 도큐먼트 데이터 생성
    document = {
        'image': url_image,
        'title': url_title,
        'description': url_description,
        'article_url': article_url,
        'comment': comment,
    }
    
    # 몽고db에 articles 컬렉션에 도큐먼트 저장
    db.articles.insert_one(document)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
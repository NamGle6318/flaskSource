# render_template : html 파일 가져오기?
# request : 사용자 요청 처리

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


## 평범한 getMapping
@app.route("/")  # == @GetMapping("/")
def index():
    return "Hello!!!"


## GetMapping, PostMapping 한 공간에서 사용 방법
@app.route("/create", methods=["GET", "POST"])  # @getMapping + @PostMapping
def create():
    ## 사용자 요청 종류에 따른 분기 처리
    if request.method == "GET":
        ## 원하는 페이지 띄워줌
        return render_template("create.html")
    else:
        name = request.form["name"]  # dictionary 식 post한 form 값 가져오기
        print(f"name : {name}")
    return redirect("/")


## 주소 값 가변으로 받기 /read/원하는 숫자
@app.route("/read/<int:post_id>")  # == @GetMapping("/read1")
def read(post_id):
    return f"Read {post_id}"

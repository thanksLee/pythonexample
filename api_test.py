from flask import Flask, jsonify, request, json


app = Flask(__name__)

works = [
    {"id":100,
     "title":"식품구매",
     "description":"우유, 치즈, 과일, 피자",
     "done":False
     },
    {"id": 200,
     "title": "플라스크배우기",
     "description": "웹프로그래밍",
     "done": False
     }
]

wok = {"id": 200,
     "title": "플라스크배우기",
     "description": "웹프로그래밍",
     "done": False
     }

@app.route("/json", methods=["GET"])
def get_works():
    return jsonify(works)


@app.route("/demo_test_post", methods=["GET", "POST"])
def demo_test_post():
    if request.method == "POST":
        print("post")
    else:
        print("get")
    print (request.is_json)
    data = request.json
    print (data)
    data = dict(data)
    data["jjj"] = "abadafadsfasdf"
    print(data)


    bb = json.dumps(request.json, indent=2)
    
    print(bb)
    print(type(bb)) # str 이기때문에 dict로 변환
    cc = json.loads(bb)
    print(cc)
    print(type(cc))

    cc["jadfadfadf"] = "adfasdfadfasdffd" # dict 변환 후 add 한다.
    print(cc)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() :
    return render_template("index.html")


@app.route("/demo_02", methods=["GET", "POST"])
def demo_02():
    return render_template("demo_02.html")

@app.route("/demo_test", methods=["GET", "POST"])
def demo_test():
    lv_test = "python test"
    return render_template("demo_test.html", lv_test=lv_test)

@app.route("/demo_03", methods=["GET", "POST"])
def demo_03():
    return render_template("demo_03.html")

@app.route("/demo_test_post", methods=["GET", "POST"])
def demo_test_post():
    if request.method == "POST":
        print("post")
    else:
        print("get")
    print (request.is_json)
    data = request.json
    lv_title = data["title"]
    lv_article = data["article"]
    print (data["title"])    
    return render_template("demo_test_post.html", lv_title=lv_title, lv_article=lv_article)


@app.route("/demo_04", methods=["GET", "POST"])
def demo_04():
    return render_template("demo_04.html")


@app.route("/demo_05", methods=["GET", "POST"])
def demo_05():
    return render_template("demo_05.html")


@app.route("/demo_06", methods=["GET", "POST"])
def demo_06():
    return render_template("demo_06.html")

@app.route("/demo_07", methods=["GET", "POST"])
def demo_07():
    return render_template("demo_07.html")

@app.route("/demo_08", methods=["GET", "POST"])
def demo_08():
    return render_template("demo_08.html")

@app.route("/demo_09", methods=["GET", "POST"])
def demo_09():
    return render_template("demo_09.html")

@app.route("/demo_10", methods=["GET", "POST"])
def demo_10():
    return render_template("demo_10.html")

@app.route("/demo_11", methods=["GET", "POST"])
def demo_11():
    return render_template("demo_11.html")

@app.route("/demo_12", methods=["GET", "POST"])
def demo_12():
    return render_template("demo_12.html")

@app.route("/demo_13", methods=["GET", "POST"])
def demo_13():
    return render_template("demo_13.html")

@app.route("/demo_14", methods=["GET", "POST"])
def demo_14():
    return render_template("demo_14.html")

@app.route("/demo_15", methods=["GET", "POST"])
def demo_15():
    return render_template("demo_15.html")

if __name__ == "__main__":
    app.run(debug=True)
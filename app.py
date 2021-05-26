from flask import Flask, render_template, redirect, request
import Caption_it as cap

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    result_dic = {}
    if request.method == 'POST':

        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        caption = cap.caption_this_image(path)
        print(f.filename)

        name = f.filename
        result_dic = {
            'image' : path,
            'caption' : caption,
        }

    return render_template("index.html",results=result_dic)




if __name__ == '__main__':
    app.run(debug = True)
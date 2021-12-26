from flask import Flask, render_template, request
import Caption_it as cap
import os
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    result_dic = {}
    dir = 'static'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
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
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def play():
    width = 600
    height = 600
    color1 = "red"
    color2 = "grey"
    return render_template("index.html", timesX=8, timesY=8, width=str(width) + "px", height=str(height) + "px", color1 = color1, color2 = color2)

@app.route("/<int:timesY>")
def playX(timesY):
    width = 600
    height = timesY * 75
    color1 = "red"
    color2 = "grey"
    return render_template("index.html", timesX=8, timesY=timesY, width=str(width) + "px", height=str(height) + "px", color1 = color1, color2 = color2)

@app.route("/<int:timesX>/<int:timesY>")
def playXY(timesX, timesY):
    width = timesX * 75
    height = timesY * 75
    color1 = "red"
    color2 = "grey"
    return render_template("index.html", timesX=timesX, timesY=timesY, width=str(width) + "px", height=str(height) + "px", color1 = color1, color2 = color2)

@app.route("/<int:timesX>/<int:timesY>/<color1>/<color2>")
def playXYColor(timesX, timesY, color1, color2):
    width = timesX * 75
    height = timesY * 75
    return render_template("index.html", timesX=timesX, timesY=timesY, width=str(width) + "px", height=str(height) + "px", color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)


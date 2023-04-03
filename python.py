from flask import Flask, url_for, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def render_about():
    return render_template('about.html')
    
@app.route('/query')
def render_query():
    return render_template('query.html')

@app.route('/data')
def render_data():
    with open('health.json') as health_data:
        data = json.load(health_data)
    disease = request.args['disease']
    number = 0
    num=0
    year = 0
    loc = ""
    string = "Disease Data: "
    for s in data:
        if s["disease"].lower() == disease.lower():
            if s["number"] > num:
                num = s["number"]
                year = s["year"]
                loc = s["loc"]
                pop = s["population"]
            string += s["disease"]
            number += s["number"]
            popo = str(num/pop)[0] + str(num/pop)[1] + str(num/pop)[2] +str(num/pop)[3] + str(num/pop)[4] + str(num/pop)[5]
    if num == 0:
        return render_template('data.html', number = "Unfortunately, this disease is not present in the dataset.")
    return render_template('data.html', disease = disease + " had its worst year in " + str(year) + " in " + loc.lower() + " when " + str(num) + " people contracted the disease.", number = "There have been " + str(number) + " documented cases of " + disease + " in this dataset", percent = "About " + popo + "% of the population contracted the disease at this time.")
if __name__=="__main__":
    app.run(debug=False)

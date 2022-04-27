from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/about') 
def about():
    return render_template('about.html')

#(Process)Modify app.py to collect the data from your estimate.html form into variables. Calculate the cost estimate
#based on the formulas found in the details section above
#(Output)The calculation should produce a value stored in a varaible that is displayed on estimate.html after processing

@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float (form['radius'])
        height = float (form['height'])    
        PI= 3.14
        Labor=15
        Material=25
        
        TankTop=PI*(radius*radius)
        TankSides=(PI*(radius*height)*2)
        TotalAreaIn=TankTop+TankSides
        TotalSqft=TotalAreaIn/144

        MaterialCost=TotalSqft*Material
        LaborCost=TotalSqft*Labor
    
        estimate=MaterialCost+LaborCost
        return render_template('index.html', data=estimate)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



#{{{3.14*radius}+{2*{3.14*{radius*height}}}/144}*25}+{{{3.14*radius}+{2*{3.14*{radius*height}}}/144}*15}

#tank_top = 3.14 * radius^2
#tank_sides = 2(3.14(radius*height))
#total_area_in= tank_top + tank_sides
#total_sqft = toatl_area_in/144
#material_cost = total_sqft*25
#labor_cost = total_sqft*15
#total_cost = material_cost + labor_cost
from bokeh.io import output_notebook, show, reset_output
import bokeh
from bokeh.plotting import figure, output_file, save
#import create_connection function from the sql.py file
from sql import create_connection

def total_visits():
    #connect to database
    conn = create_connection("sqlite.db")
    #set output structure of the select query
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute('select SUM(total) from Data where country="ΓΕΝΙΚΟ ΣΥΝΟΛΟ"')
    total = cur.fetchall()
    return total[0]


def country_visits(limit):
    #connect to database
    conn = create_connection("sqlite.db")
    #set output structure of the select query
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    #get countries
    cur.execute('select country  from Data where country is not NULL and country not like "ΓΕΝΙΚΟ ΣΥΝΟΛΟ" and country not like "" GROUP BY country order by sum(total) desc limit ' + str(limit))
    countries = cur.fetchall()
    #get sum total visits from every country
    cur.execute('select sum(total) from Data where country is not NULL and country not like "ΓΕΝΙΚΟ ΣΥΝΟΛΟ" and country not like "" GROUP BY country order by sum(total) desc limit ' + str(limit))
    total = cur.fetchall()

    # data
    x_bar = countries
    y_bar = total

    #create plot
    bar_chart = figure(x_range=x_bar, title='Total Visits By Country', x_axis_label='x', y_axis_label='y', plot_height=800, plot_width=800, sizing_mode='stretch_both')
    bar_chart.vbar(x_bar, top=y_bar, color='blue', width=0.5)
    bar_chart.y_range.start = 0
    
    #create file and open in browser
    output_file("countries.html")
    show(bar_chart)


def transportation_visits():
    #connect to db
    conn = create_connection("sqlite.db")
    #set output structure
    conn.row_factory = lambda cursor, row: [row[0], row[1],row[2],row[3]]
    cur = conn.cursor()
    #execute sql query
    cur.execute('select sum(plane) as Plane, sum(boat) as Boat, sum(train) as Train, sum(car) as Car from Data where country is not NULL and country not like "ΓΕΝΙΚΟ ΣΥΝΟΛΟ" and country not like ""')
    total = cur.fetchall()

    # data
    x_bar = ["plane", "boat", "train", "car"]
    y_bar = total[0]

    print(y_bar)
    # sort data (sort x by its cooresponding y)
    sorted_categories = sorted(x_bar, key=lambda x: y_bar[x_bar.index(x)], reverse=True)

    # plot
    bar_chart = figure(x_range=sorted_categories, title='Transportation Statistics', x_axis_label='x', y_axis_label='y', plot_height=800, plot_width=1400, sizing_mode='stretch_both')
    bar_chart.vbar(x_bar, top=y_bar, color='purple', width=0.3)
    bar_chart.y_range.start = 0

    output_file("transportation.html")
    show(bar_chart)




def trimino_visits():
    conn = create_connection("sqlite.db")
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cur.execute('select sum(plane) as Plane, sum(boat) as Boat, sum(train) as Train, sum(car) as Car, sum(total) as Total  from Data where country is not NULL and country not like "ΓΕΝΙΚΟ ΣΥΝΟΛΟ" and country not like ""')
    total = cur.fetchall()


    month_name = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    #execute a query for every Trimester in the 2011-2015 period
    listTotal = []
    listTrimino = []
    for year in range(2011,2015):
        for trimino in range(0,4):
            #print(year , month_name[trimino*3+0], month_name[trimino*3+1], month_name[trimino*3+2])
            cur = conn.cursor()
            cur.execute('    select sum(total) from Data where country="ΓΕΝΙΚΟ ΣΥΝΟΛΟ" and year=? and  ( month=? or month=? or month=?)',
                        (year , month_name[trimino*3+0], month_name[trimino*3+1], month_name[trimino*3+2]))
            total = cur.fetchall()

            #add data to list
            listTrimino.append(str(year) + "-" + str(trimino+1))
            listTotal.append(total[0])

    #every Trimester seperate 
    x_bar = listTrimino
    y_bar = listTotal


    #added trimester of every year
    x_bar = ["Trimino 1", "Trimino 2", "Trimino 3", "Trimino 4"]
    y_bar = [0,0,0,0]
    for i in range(0,13):
        if i % 4 == 0: y_bar[0] = y_bar[0] + listTotal[i]
        elif i % 4 == 1: y_bar[1] = y_bar[1] + listTotal[i]
        elif i % 4 == 2: y_bar[2] = y_bar[2] + listTotal[i]
        elif i % 4 == 3: y_bar[3] = y_bar[3] + listTotal[i]

    # plot
    bar_chart = figure(x_range=x_bar, title='Visits every Trimester', x_axis_label='x', y_axis_label='y', plot_height=800, plot_width=1400, sizing_mode='stretch_both')
    bar_chart.vbar(x_bar, top=y_bar, color='green', width=0.3)
    bar_chart.y_range.start = 0

    #create file and open in browser
    output_file("trimino.html")
    show(bar_chart)



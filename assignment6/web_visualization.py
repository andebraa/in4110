import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import tempfile
from flask import Flask, render_template, request
alt.renderers.enable('altair_viewer')
app = Flask(__name__)



#TODO: MAKE FETCH_DATA HANDLE PD.DATETIME OBJECT IN START AND END

def fetch_data(county = 'alle_fylker', start = False, end = False, range = 'day'):
    """
    function for fetching data from csv files to pandas DataFrame type.
    if start and end is specified the data is truncated to handle This.

    args:
        county (string): name of the norwegian county (fylke) from which
                        the data will be fetched
        start (string): beginning date of dataset
        end (string): end date of dataset
        range(string): 'day' or 'week', indicates cases per week or per day
    returns:
        pandas dataframe of either weekly or daily data
    """


    cols = ['Prøvetakingsdato:T', 'Kumulativt antall:Q', 'Nye tilfeller:Q']
    dato = 'Prøvetakingsdato'
    cum = 'Kumulativt antall:Q'
    new = 'Nye tilfeller:Q'

    #checking if day or week is defined
    if range =='day':
        data = pd.read_csv(
            "resources/"+county+'.csv',

            parse_dates = [dato],
            date_parser= lambda col: pd.to_datetime(col, utc =True, format="%Y-%m-%d")

        )
    else:
        cols = ['Dato:T', 'Kumulativt antall:Q', 'Nye tilfeller:Q']
        dato = 'Dato:T'
        data = pd.read_csv(
            "resources/weekly_"+county+'.csv',

        )
        data['Dato'] = pd.to_datetime(data['Dato'] + '-1', format='%Y-%W-%w')

    #Checking if start end end is defined
    if isinstance(start, str) and start < pd.to_datetime('2020-02-21'):
        if start < pd.to_datetime('2020-02-21'):
            print('start date is before start of dataset')
            start = False
        else:
            mask = (data[dato] > start)
            data = data.loc[mask]
    if isinstance(end, str):
        if end > pd.to_datetime('2020-11-11'):
            print('end date is later than end of dataset')
            end = False
        else:
            mask = (data[dato] <= end)
            data=data.loc[mask]
    print(data.head())
    return data

def plot_reported_cases(county = 'alle_fylker', start = False, end = False, range='day'):
    """
    Finds the reported cases and plots these for the given county, for a given
    time interval.

    args:
        county (string, optional): the Norwegian county the reported cases will be from
        start (string, optional): date indicating beginning of the plot (YYYY-MM-DD)
        end (string), optional: date indicating end of plot (YYYY-MM-DD)
    """
    data = fetch_data(county, start, end, range)
    if range == 'day':
        dato = 'Prøvetakingsdato:T'
    else:
        dato = 'Dato:T'

    brush = alt.selection_interval(encodings=['x'])
    chart = alt.Chart(data).mark_bar().encode(
        alt.X(dato, axis=alt.Axis(title='dato')),
        alt.Y('Nye tilfeller',
            axis=alt.Axis(title='smittetilfeller')),
        tooltip=[dato, 'Nye tilfeller:Q'],
    ).properties(
        title =f'{county}'
    ).add_selection(
    brush
    )
    return chart



def plot_cumulative_cases(county = 'alle_fylker', start = False, end = False, range='day'):
    data = fetch_data(county, start, end, range)
    dato = None
    #NOTE due to some messy stuff about headers being different with weekly data,
    #I have to manually check this each time
    if range == 'day':
        dato = 'Prøvetakingsdato:T'
    else:
        dato = 'Dato:T'
    print(dato)
    nearest = alt.selection(type='single', nearest = True, on='mouseover',
                            fields=[dato], empty='none')
    chart = alt.Chart(data).mark_line().encode(
        x=dato,
        y = 'Kumulativt antall:Q',
        tooltip=[dato, 'Kumulativt antall:Q']
    ).properties(
        title =f'{county}'
    )
    #Transparent selectors across the chart. This indicates the X value
    selectors = alt.Chart().mark_point().encode(
        x=dato,
        opacity = alt.value(0),
    ).add_selection(
        nearest
    )
    #Points on the line
    points = chart.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0)),
    )

    #draw text labels near points that are highlighted
    text = chart.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'Kumulativt antall:Q', alt.value(' '))
    )
    rules = alt.Chart().mark_rule(color='gray').encode(
        x=dato
    ).transform_filter(
        nearest
    )
    stockChart = alt.layer(chart, selectors, points, rules, text,
    ).properties(
        width=600, height=300
    ).interactive()

    return stockChart

def plot_both(county = 'alle_fylker', start = False, end = False, range='day'):
    data = fetch_data(county, start, end, range)
    if range == 'day':
        dato = 'Prøvetakingsdato:T'
    else:
        dato = 'Dato:T'

    cum = 'Kumulativt antall:Q'
    new = 'Nye tilfeller:Q'
    nearest = alt.selection(type='single', nearest = True, on='mouseover',
                            fields = ['Prøvetakingsdato'])

    base = alt.Chart(data).encode(
        x=dato,
        tooltip=[
        alt.Tooltip(dato, title='dato'),
        alt.Tooltip(new, title='nye tilfeller'),
        alt.Tooltip(cum, title='kumulative tilfeller'),
        ]
    ).mark_bar().encode(
        y=new
    )
    line = base.mark_line(color='red').encode(y=cum, tooltip=[cum])
    final= alt.layer(base, line).resolve_scale(
        y='independent'
    ).interactive()

    return final



def norway_plot():
    """
    Generates an altair plot of norway (from the github link) with mouseover
    that displays number of incidents in the county
    returns:
        fig (altair fig):
    """
    data = {"Category": ["Oslo", "Viken", "Vestland", "Rogaland", "Innlandet", "Trøndelag", "Agder",
                        "Vestfold og Telemark", "Troms og Finnmark", "Møre og Romsdal", "Nordland"],
            "incidents": [870.5, 410.1, 413.8, 204, 263.3, 182.4, 201.5, 142.1, 204.7, 151.2, 119]}
    df = pd.DataFrame.from_dict(data)
    counties = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/norway/norway-new-counties.json", 'Fylker')

    nearest = alt.selection(type="single", on="mouseover", fields=["properties.navn"], empty="none")

    fig = alt.Chart(counties).mark_geoshape().encode(
        tooltip=[
            alt.Tooltip("properties.navn:N", title='County'),
            alt.Tooltip("incidents:Q", title="Cases per 100k capita"),
        ],
        color=alt.Color("incidents:Q", scale=alt.Scale(scheme="reds"),
                        legend=alt.Legend(title="Cases per 100k capita")),
        stroke=alt.condition(nearest, alt.value("gray"), alt.value(None)),
        opacity=alt.condition(nearest, alt.value(1), alt.value(0.8)),

    ).transform_lookup(
        lookup="properties.navn",
        from_ = alt.LookupData(df, "Category", ["incidents"]),
    ).properties(
        width=500,
        height=600,
        title="Number of cases per 100k in every county",
    ).add_selection(
        nearest
    )
    return fig


#app functions and calls

@app.route("/")
def base():
    return render_template('web_base.html')

@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/norway_plot")
def plot_norway():
    fig = norway_plot()

    tmp = tempfile.NamedTemporaryFile(suffix=".html")
    fig.save(tmp.name)

    with open(tmp.name) as file:
        return file.read()

@app.route('/set_values', methods=['POST'])
def set_values():
    county = request.form["fylke"]
    type = request.form['plot_type']
    range = request.form['range']

    return render_template('web_base.html', county=county, type=type, range=range)

@app.route('/figplot')
def figplot():
    county = request.args.get('county')
    type = request.args.get('type')
    range = request.args.get('range')
    tmp = None


    if type == 'cum':
        fig = plot_cumulative_cases(county, range=range)
        tmp = tempfile.NamedTemporaryFile(suffix='.json')
        fig.save(tmp.name)
    elif type == 'daily_cases':
        fig = plot_reported_cases(county, range=range)
        tmp = tempfile.NamedTemporaryFile(suffix='.json')
        fig.save(tmp.name)
    elif type =='both':
        fig = plot_both(county, range=range)
        tmp = tempfile.NamedTemporaryFile(suffix='.json')
        fig.save(tmp.name)


    with open(tmp.name) as file:
        return file.read()


if __name__ == "__main__":
    # fig = plot_reported_cases(range='week', end = pd.to_datetime('2020-10-10'))
    # fig.show()
    # fig = plot_cumulative_cases('alle_fylker', range='week')
    # fig = plot_both(range='week')
    app.run()
    fig.show()

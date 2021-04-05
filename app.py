import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash_canvas
from dash_canvas import DashCanvas

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_daq as daq

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}], suppress_callback_exceptions=True
                )

server = app.server

filename = 'https://www.pngitem.com/pimgs/m/608-6085257_classic-eggman-sonic-characters-hd-png-download.png'
canvas_width = 300

# Dataset Processing 1 figura


path = '/Users/Daniel/Google Drive/NOVA IMS - Postgraduation in Data Science and Advanced Analytics/Data Visualization/Dash/'
df = pd.read_csv("Evolution_Videogames.csv", sep=";")
df.rename(columns={"x": "run"}, inplace=True)

# dataset processing 2 figura

path = '/Users/Daniel/Google Drive/NOVA IMS - Postgraduation in Data Science and Advanced Analytics/Data Visualization/Dash/'


###DATA PREPROCESSING###

#df = pd.read_csv(path +"Dash1_test.csv",sep=";")
#df.rename(columns={"x":"run"}, inplace=True)
#df_consoles = pd.read_csv(path +"Consoles_Timeline.csv", sep=";")



df_consoles = pd.read_csv('vgsales_2019.csv',sep=",")
df_consoles = df_consoles[['Name', 'Year', 'Publisher', 'Platform', 'Developer', 'Genre', 'Critic_Score']]
#all data from 2020 is wrong, i'm eliminating them here
np.where(df_consoles['Year'] == 2020.0, df_consoles['Year'], 1976)
#same with data <1977
df_consoles = df_consoles[df_consoles['Year']>=1977]
#merges global sales and total shipped, it's the same thing and they complement each other
#df_consoles['Global_Sales'].update(df_consoles['Total_Shipped'])
#del df_consoles['Total_Shipped']
df_consoles.rename(columns= {'Critic_Score': 'Score'}, inplace = True) #renames column


#data para a 3 figura
df1 = pd.read_csv('use_on_racing.csv')

dict_keys = list(range(1977, 2021))

years = list((range(1977, 2021)))

n_frame = {}

# set base case
dataframe = pd.DataFrame(columns=df1.columns)

for y, d in zip(years, dict_keys):
    # get list of games published in year
    dataframe = dataframe.append(df1[(df1['Year'] == y)])
    dataframe = dataframe.nlargest(n=15, columns=['Total'])
    dataframe = dataframe.sort_values(by=['Total'], ascending='False')

    n_frame[d] = dataframe

#print(n_frame)

color_box = '#F2D0A4'
back_color = '#545E75'
# ------------------------------------------------------------------------------

#figura 1 construção grafico


# Base plot
fig = go.Figure(
    layout=go.Layout(
        updatemenus=[dict(type="buttons", direction="right", x=1, y=1.16), ],
        xaxis=dict(range=[1970, 2022],
                   autorange=False, tickwidth=2,
                   title_text="Year"),
        yaxis=dict(range=[1, 1],
                   autorange=False, ),
        title={'text': "Check some facts about video games that will make you feel nostalgic & old #SorryNotSorry",
               'font': {'color': '#FFFFFF'}},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    ))

# Add traces
init = 1
y = 1

fig.add_trace(
    go.Scatter(x=df.Year[:init],
               y=df.Released[:init],
               name="A",
               visible=True,
               hovertext=df['Fact'],
               hoverlabel=dict(namelength=0),
               hovertemplate='%{hovertext}<br>Year: %{x:} ',
               mode='lines+markers',
               line=dict(color='darkcyan', width=18),
               marker=dict(symbol="circle",
                           color='khaki', size=14,
                           line=dict(color='khaki', width=4),
                           )))

##### ANOTATIONS
fig.add_annotation(
    x=1972,
    y=y,
    xref="x",
    yref="y",
    text="First Video Game!",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=30,
    ay=-90,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#ff7f0e",
    opacity=0.8
)

##### ANOTATION Pac-Man
fig.add_annotation(
    x=1980,
    y=y,
    xref="x",
    yref="y",
    text="Pac-Man",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-10,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#00afb9",
    opacity=0.8
)

##### ANOTATION Mario

fig.add_annotation(
    x=1983,
    y=y,
    xref="x",
    yref="y",
    text="Mario Bros.",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-30,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#90be6d",
    opacity=0.8
)

##### ANOTATION Tetris

fig.add_annotation(
    x=1984,
    y=y,
    xref="x",
    yref="y",
    text="Tetris",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=40,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="Gold",
    opacity=0.8
)

##### ANOTATION Gameboy

fig.add_annotation(
    x=1989,
    y=y,
    xref="x",
    yref="y",
    text="GameBoy",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=30,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="Crimson",
    opacity=0.8
)

##### ANOTATION Playstation

fig.add_annotation(
    x=1995,
    y=y,
    xref="x",
    yref="y",
    text="Playstation",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-50,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#7209b7",
    opacity=0.8
)

##### ANOTATION Pokemon

fig.add_annotation(
    x=1996,
    y=y,
    xref="x",
    yref="y",
    text="Pokémon",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="DodgerBlue",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2003,
    y=y,
    xref="x",
    yref="y",
    text="Steam",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="slategray",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2006,
    y=y,
    xref="x",
    yref="y",
    text="Wii",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-30,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="orange",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2010,
    y=y,
    xref="x",
    yref="y",
    text="Minecraft",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="sienna",
    opacity=0.8
)

##### ANOTATION Switch

fig.add_annotation(
    x=2016,
    y=y,
    xref="x",
    yref="y",
    text="Switch",
    showarrow=True,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="hotpink",
    opacity=0.8
)

# Animation
fig.update(frames=[
    go.Frame(
        data=
        go.Scatter(x=df.Year[:k], y=df.Released[:k]), ) for k in range(init, len(df) + 1)])

# hide y ticks!
fig.update_layout(

    xaxis=dict(
        # autorange=True,
        showgrid=False,
        tickmode="array",
        tickvals=[i for i in range(1970, 2021, 5)],
        # ticks=range(1970,2020,5),
        # showticklabels=False
    ),

    yaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False
    )
)

# Buttons
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="START!",
                     method="animate",
                     args=[None, {"frame": {"duration": 300, "redraw": True},
                                  "fromcurrent": False,
                                  "transition": {"duration": 1000},
                                  "mode": "line+markers"}]),
                dict(label="FULL",
                     method="animate",
                     args=[None, {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate", "transition": {"duration": 0}}])

            ]))])
####
fig_layout_defaults = dict(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)', )



# figura 3 construção gráfico

# -------------------------------------------
fig_2 = go.Figure(
    data=[go.Bar(
        x=n_frame[1977]['Total'],
        y=n_frame[1977]['Name'], orientation='h',
        text=n_frame[1977]['Name'],
        textposition='auto', textfont = dict(family="Play", size = 18),
        width=0.9, marker=dict(color =n_frame[1977]['Color'])
    )
    ],

    layout=go.Layout(
        font=dict( family="Play", size=18),
        xaxis=dict(range=[0, max(n_frame[1977]['Total']) + 1], autorange=False,
                   title=dict(text='Global Sales (Millions of Units)', font=dict(family="Play", size=18))),
        yaxis=dict(range=[-0.5, len(n_frame[1977]['Name'])], autorange=False, visible=False, showticklabels=False),
        title=dict(text='', #Top 15 Global Video Game Sales (Millions of Units) - Launched up to 1977',
                   font=dict(family="Play", size=28),
                   x=0.5, xanchor='center')
        ,

        # transparent color
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        # Add button

        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          # https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
                          args=[None,
                                {"frame": {"duration": 1000, "redraw": True},
                                 "transition": {"duration": 250,
                                                "easing": "linear"}}]
                          ),
                     dict(label='Full',
                          method='animate',
                          args=[None, {'frame': {'duration': 0, 'redraw': False},
                                       'mode': 'immediate',
                                       'transition': {'duration': 0}}]
                          ),
                     dict()]
        )]),
    frames=[
        go.Frame(
            layout=go.Layout(
                xaxis=dict(range=[0, max(value['Total'] + 1)], autorange=False),
                yaxis=dict(range=[-0.5, len(value)], autorange=False, visible=False, showticklabels=False),
                title=dict(text='Top 15 ' + str(key),
                           font=dict(family="Play", size=28))
            ),
            data=[
                go.Bar(x=value['Total'], y=value['Name'],
                       orientation='h', text=value['Name'],
                       textposition='auto', textfont= dict(family="Play", size = 18),
                       marker=dict(color =value['Color'])
                       )]
        )
        for key, value in n_frame.items()
    ]

)
# -------------------------------------------
# ------------------------------------------------------------------------------
# App layout

# figura 1

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'backgroundColor': back_color})

page_1_layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.Button(dcc.Link('Go to credits', href='/page-2')),

                          html.H1("Timeline of Video Games", style={'text-align': 'center', 'color': "#FFFFFF"}),
                          ])
                )]),

    #### GRAPH
    dbc.Row([
        dbc.Col([dcc.Graph(id='my_line_chart', figure=fig)],
                style={'width': "30", "margin": "20px", "background-color": color_box, 'border-style': "solid",
                       "display": "incline-block"}, width={'size': 8, 'offset': 0, 'order': 1}),

        dbc.Col([html.P('Choose a year:Choose a year:Choose a year:Choose a year:Choose a year:Choose a year:Choose '
                        'a year:Choose a year:Choose a year:Choose a year:Choose a year:Choose a year:Choose a year:Choose '
                        'a year:Choose a year:Choose a year:Choose a year:', style={'color': "#FFFFFF"})
                 ], style={'width': "30", "margin": "20px", "background-color": color_box , 'border-style': "solid",
                           "display": "incline-block"}, width={'size': 3, 'offset': 0, 'order': 2})

    ], no_gutters=True, justify='start'),






## figura 2
# App layout

    dbc.Row([
        dbc.Col([html.H1("Trip Down Memory Lane", style={'text-align': 'center', 'color': "#FFFFFF"}),

                 ])]),

    ###YEAR SLIDER
    dbc.Row([
        dbc.Col([html.Div(["Filter by Year(s): ",
                           dcc.RangeSlider(id='my_slider', min=min(df_consoles['Year']), max=max(df_consoles['Year']),
                                           step=1,

                                           value=[int(min(df_consoles['Year'])), int(max(df_consoles['Year']))],
                                           marks={i: {'label': str(i)} for i in list(int(i) for i in list(
                                               x for x in set(df_consoles['Year'].to_list()) if x == x))},
                                           included=True),
                           ], style={'color': "#FFFFFF"}),
                 # , style={"display": "grid", "grid-template-columns": "10% 50% 100%"}), #play with slider length
                 ])
    ]),

    html.Br(),

    ###INPUT BOX
    dbc.Row([
        dbc.Col([html.Div(["Find Your Favorite VideoGame: ",
                           dcc.Input(id='game_input', value='', type='text', placeholder='Insert Video Game...',
                                     size='30'), ], style={'color': "#FFFFFF"}),

                 html.Br(),

                 ##### TABLE
                 html.Div(

                     dash_table.DataTable(
                         id='table',
                         columns=[{"name": i, "id": i} for i in df_consoles.columns],
                         # fixed dimensions in each column (optimized to maximize width of column name)
                         style_cell_conditional=[
                             {'if': {'column_id': 'Year'},
                              'width': '40px'},
                             {'if': {'column_id': 'Platform'},
                              'width': '70px'},
                             {'if': {'column_id': 'Genre'},
                              'width': '90px'},
                             {'if': {'column_id': 'Publisher'},
                              'width': '80px'},
                             {'if': {'column_id': 'Name'},
                              'width': '280px'},
                             {'if': {'column_id': 'Score'},
                              'width': '40px'},
                         ],
                         data=df_consoles.to_dict('records'),
                         fixed_columns={'headers': True, 'data': 1},
                         fixed_rows={'headers': True},
                         style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'maxWidth': 0,
                                     ## esconde cels que tenham muito texto
                                     'backgroundColor': 'rgb(50, 50, 50)', 'fontWeight': 'bold', 'color': 'white'},
                         # tooltip_data=[
                         # {"Console": {'value': 'The shipment is {}'.format(
                         # '![Markdown Logo is here.](https://media.giphy.com/media/1xjX6EOQZnS5ouhU5k/giphy.gif)'
                         # if row['Console']==['DVD Kids']
                         # else '![Markdown Logo is here.](https://media.giphy.com/media/7SIdExk63rTPXhbbbt/giphy.gif)'),
                         # 'type': 'markdown'}       }
                         # for row in df_consoles.to_dict('records')],

                         css=[{
                             'selector': '.dash-table-tooltip',
                             'rule': 'background-color: gray; font-family: monospace'}],  ### cor da legenda adicional
                         tooltip_delay=0,
                         tooltip_duration=None,
                         style_table={'minWidth': '80%'},  ### dimensão da tabela
                         style_header={'backgroundColor': 'rgb(50, 50, 50)', 'fontWeight': 'bold', 'color': 'yellow'},
                         ##header
                         style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(115, 119, 120)'}]
                         ### linhas listradas
                     )
                 )], style={'width': "30", "margin": "20px", "background-color": color_box, 'border-style': "solid",
                            "display": "incline-block"}, width={'size': 8, 'offset': 0, 'order': 1}),

        dbc.Col([html.Div(children=[
            html.Iframe(
                id='movie_player',
                src="https://giphy.com/embed/x2woMnCz4W0Vy",
                width="100%",
                height="600",

            ),
        ])

        ], style={'width': "30", "margin": "20px", "background-color": color_box, 'border-style': "solid",
                  "display": "incline-block"}, width={'size': 3, 'offset': 0, 'order': 2})

    ]),


  #figura 3 layout
    dbc.Row([
        dbc.Col(html.Div([html.H1("Top 15 Global Sales (Millions of Units) - Games Launched up to 1977", style={'text-align': 'center','color':"#FFFFFF"}),
                          ])
                )]),



#### GRAPH
    dbc.Row([
        dbc.Col([dcc.Graph(id='my_line_chart', figure=fig_2)],style={'width': "100","margin": "20px","background-color": color_box,'border-style':"solid","display":"incline-block"},width={'size':11, 'offset':0, 'order':1}),


    ], no_gutters=True, justify='start')



], fluid=True,
    style={'backgroundColor': back_color})



# segunda pagina layout

page_2_layout = html.Div([
    html.H1('Credits',style={'color': "#FFFFFF"}),
    html.Div([
        DashCanvas(
            id='canvas-color',
            width=canvas_width,
            filename=filename,
            hide_buttons=['line', 'zoom', 'pan'],
        )
    ], className="six columns"),
    html.Div([
        html.H6(children=['Brush width'],style={'color': "#FFFFFF"}),
        dcc.Slider(
            id='bg-width-slider',
            min=2,
            max=40,
            step=1,
            value=5
        ),
        daq.ColorPicker(
            id='color-picker',
            label='Brush color',
            value=dict(hex='#119DFF')
        ),
    ], className="three columns"),
    html.Div(id='page-2-content'),
    html.Br(),
    html.Button(dcc.Link('Go back to home', href='/'))
])

####################################################
# callbacks para a tab

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return page_1_layout
    # You could also return a 404 "URL not found" page here
 # callbacks para a pintura
@app.callback(Output('canvas-color', 'lineColor'),
              Input('color-picker', 'value'))
def update_canvas_linewidth(value):
    if isinstance(value, dict):
        return value['hex']
    else:
        return value


@app.callback(Output('canvas-color', 'lineWidth'),
              Input('bg-width-slider', 'value'))
def update_canvas_linewidth(value):
    return value


# figura 2 callbacks
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output("table", "data"),
    Input("game_input", "value"),
    Input("my_slider", "value")
)
def update_table(game_input, my_slider):
    # not necessary anymore coz slide bar has always input!
    # if not game_input:
    # raise PreventUpdate

    if game_input:
        data = df_consoles[df_consoles['Name'].str.contains(game_input, na=False, case=False)]
        if my_slider:
            data = data[(data['Year'] >= my_slider[0]) & (data['Year'] <= my_slider[1])]

    if my_slider:
        data = df_consoles[(df_consoles['Year'] >= my_slider[0]) & (df_consoles['Year'] <= my_slider[1])]
        if my_slider:
            data = data[data['Name'].str.contains(game_input, na=False, case=False)]

    return data.to_dict("records")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

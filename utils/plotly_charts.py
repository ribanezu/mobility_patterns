import plotly.graph_objects as go

def animated_unique_ids_area(df_resampled):
    # Crear frames para la animación
    frames = [
        go.Frame(
            data=[
                go.Scatter(
                    x=df_resampled.index[:k],
                    y=df_resampled.values[:k],
                    mode='lines',
                    line=dict(color='#DBB07B'),
                    fill='tozeroy',
                    fillcolor='rgba(128, 128, 128, 0.4)'
                )
            ]
        )
        for k in range(1, len(df_resampled) + 1)
    ]

    # Crear figura con traza inicial vacía
    fig = go.Figure(
        data=[
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                line=dict(color='#DBB07B'),
                fill='tozeroy',
                fillcolor='rgba(219, 176, 123, 0)',
                name='Active trips'
            )
        ],
        layout=go.Layout(
            xaxis=dict(title='Time'),
            yaxis=dict(title='Active trips'),
            template='plotly_white',
            margin=dict(t=80, r=20, b=40, l=50),
            height=500,
            updatemenus=[
                dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(
                            label="   Show daily profile...   ",
                            method="animate",
                            args=[
                                None,
                                dict(
                                    frame=dict(duration=50, redraw=True),
                                    fromcurrent=True,
                                    mode='immediate'
                                )
                            ]
                        )
                    ],
                    direction="left",
                    pad={"r": 50, "t": 50},
                    x=0.5,
                    xanchor="center",
                    y=1.25,
                    yanchor="top",
                    font=dict(size=24, color='white'),
                    bgcolor='#2E373F',
                    bordercolor='#2E373F',
                    borderwidth=1
                )
            ]
        ),
        frames=frames
    )

    return fig


import plotly.graph_objects as go

def animated_activities_area(df_resampled):
    colors = {
        'Home': '#DBB07B',
        'Work': '#2C89A0',
        'Secondary': '#A75D5D'
    }

    # Crear frames para la animación
    frames = []
    for k in range(1, len(df_resampled) + 1):
        frame_data = []
        for category in df_resampled.columns:
            frame_data.append(
                go.Scatter(
                    x=df_resampled.index[:k],
                    y=df_resampled[category].values[:k],
                    mode='lines',
                    name=category,
                    stackgroup='one',  # <--- Apilado
                    line=dict(color=colors[category]),
                    fill='tonexty',
                    fillcolor=colors[category].replace(")", ", 0.3)").replace("rgb", "rgba")
                )
            )
        frames.append(go.Frame(data=frame_data))

    # Trazas iniciales vacías
    data = []
    for category in df_resampled.columns:
        data.append(
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name=category,
                stackgroup='one',  # <--- Apilado
                line=dict(color=colors[category]),
                fill='tonexty',
                fillcolor=colors[category].replace(")", ", 0.0)").replace("rgb", "rgba")
            )
        )

    fig = go.Figure(
        data=data,
        layout=go.Layout(
            xaxis=dict(title='Time'),
            yaxis=dict(title='Active activities'),
            template='plotly_white',
            margin=dict(t=80, r=20, b=40, l=50),
            height=500,
            updatemenus=[
                dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(
                            label="   Show activities profile...   ",
                            method="animate",
                            args=[
                                None,
                                dict(
                                    frame=dict(duration=50, redraw=True),
                                    fromcurrent=True,
                                    mode='immediate'
                                )
                            ]
                        )
                    ],
                    direction="left",
                    pad={"r": 50, "t": 50},
                    x=0.5,
                    xanchor="center",
                    y=1.25,
                    yanchor="top",
                    font=dict(size=24, color='white'),
                    bgcolor='#2E373F',
                    bordercolor='#2E373F',
                    borderwidth=1
                )
            ]
        ),
        frames=frames
    )

    return fig


def animated_mode_area(df_resampled):
    colors = {
        'Car': '#DBB07B',
        'Bus': '#2C89A0',
        'Subway': '#A75D5D',
        'Tram': '#2C89A0',
        'Walk': '#2E373F',
        'Others': '#2C89A0'
    }


    # Crear frames para la animación
    frames = []
    for k in range(1, len(df_resampled) + 1):
        frame_data = []
        for category in df_resampled.columns:
            frame_data.append(
                go.Scatter(
                    x=df_resampled.index[:k],
                    y=df_resampled[category].values[:k],
                    mode='lines',
                    name=category,
                    stackgroup='one',  # <--- Apilado
                    line=dict(color=colors[category]),
                    fill='tonexty',
                    fillcolor=colors[category].replace(")", ", 0.3)").replace("rgb", "rgba")
                )
            )
        frames.append(go.Frame(data=frame_data))

    # Trazas iniciales vacías
    data = []
    for category in df_resampled.columns:
        data.append(
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name=category,
                stackgroup='one',  # <--- Apilado
                line=dict(color=colors[category]),
                fill='tonexty',
                fillcolor=colors[category].replace(")", ", 0.0)").replace("rgb", "rgba")
            )
        )

    fig = go.Figure(
        data=data,
        layout=go.Layout(
            xaxis=dict(title='Time'),
            yaxis=dict(title='Trips by mode'),
            template='plotly_white',
            margin=dict(t=80, r=20, b=40, l=50),
            height=500,
            updatemenus=[
                dict(
                    type="buttons",
                    showactive=False,
                    buttons=[
                        dict(
                            label="   Show model share profile...   ",
                            method="animate",
                            args=[
                                None,
                                dict(
                                    frame=dict(duration=50, redraw=True),
                                    fromcurrent=True,
                                    mode='immediate'
                                )
                            ]
                        )
                    ],
                    direction="left",
                    pad={"r": 50, "t": 50},
                    x=0.5,
                    xanchor="center",
                    y=1.25,
                    yanchor="top",
                    font=dict(size=24, color='white'),
                    bgcolor='#2E373F',
                    bordercolor='#2E373F',
                    borderwidth=1
                )
            ]
        ),
        frames=frames
    )

    return fig
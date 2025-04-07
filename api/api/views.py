from django.http import JsonResponse
import plotly.graph_objects as go

def graph(request):

    # Dados das linhas
    corporate_di = [1, 2.4, 3, 7, 5, 8, 9, 9, 9, 9, 9, 9]
    engie_brasil = [1, 2, 4, 6, 8, 8, 8, 8, 8, 8, 8, 8]
    duration_anos = list(range(11))  # de 0 a 10

    # Criando o gráfico
    fig = go.Figure()

    # Linhas
    fig.add_trace(go.Scatter(x=duration_anos, y=corporate_di, mode='lines', name='Corporate DI' , line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=duration_anos, y=engie_brasil, mode='lines', name='Engie Brasil', line=dict(color='orange')))

    # Pontos de dispersão
    scatter_points = [
        {'x': 1.3, 'y': 3, 'name': 'ENGIA0' , 'color': '#4c00ff'},
        {'x': 2.6, 'y': 4, 'name': 'ENGIA1' , 'color': '#750086'},
        {'x': 3.7, 'y': 5, 'name': 'ENGIA2' , 'color': '#e13a00'},
        {'x': 4.8, 'y': 2, 'name': 'ENGIB2' , 'color': '#933526'},
        {'x': 7.9, 'y': 7, 'name': 'ENGIC3' , 'color': '#000000'},
    ]

    for point in scatter_points:
        fig.add_trace(go.Scatter(
            x=[point['x']],
            y=[point['y']],
            mode='markers+text',
            text=[point['name']],
            textposition="top center",
            name=point['name'],
            marker=dict(size=10 ,  color=point['color'])
        ))

    # Box plots
    box_data = [
        {'x': 1.5, 'y': [1.5, 2.1, 2.4, 2.2, 1.9], 'name': 'ENGIA0' , 'color': '#4c00ff'},
        {'x': 2.7, 'y': [2.5, 2.8, 3.0, 2.7, 2.9], 'name': 'ENGIA1' , 'color': '#750086'},
        {'x': 3.0, 'y': [3.5, 3.2, 3.7, 3.8, 3.6], 'name': 'ENGIA2' , 'color': '#e13a00'},
        {'x': 4.6, 'y': [2.8, 3.3, 3.0, 3.5, 3.2], 'name': 'ENGIB2' , 'color': '#933526'},
        {'x': 7.9, 'y': [2.8, 3.3, 3.0, 3.5, 4.5], 'name': 'ENGIC3' , 'color': '#000000'},
    ]

    for box in box_data:
        fig.add_trace(go.Box(
            x=[box['x']] * len(box['y']),
            y=box['y'],
            name=box['name'],
            boxpoints= False , 
            hoverinfo='name+y',
            width=0.035,
            marker_color=box['color'],
            line=dict(color=box['color'])
        ))

    # Layout
    fig.update_layout(
        title='',
        xaxis_title='Duration Anos',
        yaxis_title='Spreads a.a.',
        template='plotly_white'
    )

    fig.show()
    return fig.to_html()
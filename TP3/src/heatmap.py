'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template
import plotly.graph_objects as go

def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    # include hover template
    # set dragmode = False

    years = list(data.keys())
    neighborhoods = list(data[years[0]].keys())
    neighborhoods.reverse()
    z_matrix = [[data[year][neighborhood] for year in years] for neighborhood in neighborhoods]


    heatmap_trace = go.Heatmap(
        x=years,
        y=neighborhoods,
        z=z_matrix,
    )
    fig = go.Figure(data=heatmap_trace)
    fig.update_coloraxes(colorbar_title='Trees')
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Neighborhood',
        xaxis=dict(
            tickvals=years,
            ticktext=years,
            tickangle = -45,
            tickmode='linear',
        )
    )

    # fig = px.imshow(data,
    #             color_continuous_scale='Bluyl',
    #             labels={'x': 'Year', 'y': 'Neighborhood', 'color': 'Trees'},
    #             )
    #
    # fig.update_layout(dragmode=False)
    # #               xaxis = dict(
    # #                   tickmode = 'linear',
    # #                   tickangle=-45,
    # #              ))
    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())

    return fig

'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px
import hover_template as hover
import pandas as pd



def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base

    trace = px.choropleth_mapbox(
        locations=locations,
        geojson=montreal_data,
        color=z_vals,
        color_continuous_scale=colorscale,
        featureidkey='properties.NOM',
        # color_discrete_map={1: colorscale[0]},
        opacity=0.2).update_traces(showlegend=False,
                                   hovertemplate=hover.map_base_hover_template() )
    fig.add_trace(trace.data[0])
    fig.update_layout(coloraxis_showscale=False)

    # fig = px.choropleth_mapbox(
    #     locations=locations,
    #     geojson=montreal_data,
    #     color=z_vals,
    #     color_continuous_scale=colorscale,
    #     featureidkey='properties.NOM',
    #     zoom=10,
    #     center={'lat': 45.5, 'lon': -73.6},
    #     opacity=0.2,
    # ).update_traces(showlegend=False)
    #
    # # fig.update_layout(mapbox_style='carto-positron')

    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    # TODO : Add the scatter markers to the map base
    street_df['lon'] = street_df['geometry.coordinates'].apply(lambda x: x[0])
    street_df['lat'] = street_df['geometry.coordinates'].apply(lambda x: x[1])
    name = street_df["properties.TYPE_SITE_INTERVENTION"]
    hovertemplates = name.apply(hover.map_marker_hover_template)

    trace = px.scatter_mapbox(street_df, lon='lon', lat='lat',
                              zoom=-10,
                              color="properties.TYPE_SITE_INTERVENTION",
                              color_discrete_map={},
                              ).update_traces(marker=dict(size=20),
                                hovertemplate=hovertemplates)

    fig.update_layout(
        legend=dict(
            bgcolor='rgba(0, 0, 0, 0)', 
            itemsizing='constant'
        ),
        hovermode='closest'
    )

    for t in trace.data:
        fig.add_trace(t)
    fig.update_traces()    
    return fig

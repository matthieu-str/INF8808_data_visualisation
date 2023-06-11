'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    style['visibility'] = 'hidden' # Hide the panel
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    if style['visibility'] == 'hidden':
        style['visibility'] = 'hidden'
        
    # Keep the panel visible if it's already displayed
    else:
        style['visibility'] = 'visible'
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
   
    # Get the marker information 
    marker_info = figure['data'][curve]['customdata'][point]
    
    # Extraction of the relevant data from marker_info
    name = marker_info[4]   #NOM_PROJET
    mode = marker_info[16]  #MODE_IMPLANTATION
    theme = marker_info[23] #OBJECTIF_THEMATIQUE
    

    # Update the panel with the extracted data
    title = html.Div(html.H3(name), id='marker-title', 
                     style={'color': figure['data'][curve]['marker']['color'],
                            'padding': '0',
                            'marginTop': '-30px'
                            }
                     )  
   
    mode = html.Div(html.P(f"{mode}"), 
                    id='mode', 
                    style={'padding': '0','marginTop': '-20px'}
                    )  

    # Create a list of thématiques 
    if theme is not None:
        theme_list = [html.Li(theme_item) for theme_item in theme.split('\n')]
        thematique = 'Thématique:'
    else:
        theme_list = []
        thematique = 'Thématique: Aucune' # Displayed when there is no thématique
        
    theme = html.Div([html.P(thematique, ),html.Ul(theme_list)], 
                     id='theme',
                     style={'padding': '0','marginTop': '-20px'}
                     ) 
 
    # Display the new panel
    style['visibility'] = 'visible'
    style['height'] = 'min-content'
    style['background-color'] = 'transparent'
    style['display'] = 'block'
    
    return title, mode, theme, style

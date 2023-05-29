'''
    Contains the template to use in the data visualization.
'''
import plotly.graph_objects as go
import plotly.io as pio


THEME = {
    'background_color': '#ffffff',
    'font_family': 'Roboto',
    'accent_font_family': 'Roboto Slab',
    'dark_color': '#2A2B2E',
    'pale_color': '#DFD9E2',
    'line_chart_color': 'black',
    'label_font_size': 14,
    'label_background_color': '#ffffff',
    'colorscale': 'Bluyl'
}



def create_custom_theme():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary, using the dark
        color.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Sets the line chart's line color to the one
        designated in the THEME dictionary. Also sets
        the color scale to be used by the heatmap
        to the one in the THEME dictionary.

        Specifies the x-axis ticks are tilted 45
        degrees to the right.
    '''
    # TODO : Generate template described above

    template = go.layout.Template()

    # Set font family and color
    template.layout.font.family = THEME['font_family']
    template.layout.font.color = THEME['dark_color']
    
    
    # Set background color
    template.layout.plot_bgcolor = THEME['background_color']
    template.layout.paper_bgcolor = THEME['background_color']

    # Set hover label background color and font size
    template.layout.hoverlabel.bgcolor = THEME['label_background_color']
    template.layout.hoverlabel.font.size = THEME['label_font_size']

    # Set hover label font color
    template.layout.hoverlabel.font.color = THEME['dark_color']

    # Set hover mode to 'closest'
    template.layout.hovermode = 'closest'

    # Set line chart line color
    #template.layout.line.color = THEME['line_chart_color']

    # Set heatmap color scale
    # template.data.heatmap = [go.Heatmap(colorscale = THEME['colorscale'])]

    # Set x-axis tick angle
    template.layout.xaxis.tickangle = -45
    

    # Add the template to pio's templates
    pio.templates['custom_template'] = template


def set_default_theme():
    '''
        Sets the default theme to be a combination of the
        'plotly_white' theme and our custom theme.
    '''
    # TODO : Set default theme
    pio.templates.default = 'plotly_white+custom_template'

'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''

    label_font_style = "font-family: 'Roboto Slab'; font-weight: bold; font-size: 12px;"
    value_font_style = "font-family: 'Roboto'; font-size: 12px; font-weight: normal;"

    hover_template = (
        f"<b><span style='{label_font_style}'>Neighborhood:</span></b> %{{y}}<br>"
        f"<b><span style='{label_font_style}'>Year:</span></b> %{{x}}</b><br>"
        f"<b><span style='{label_font_style}'>Trees planted:</span></b> <span style='{value_font_style}'>%{{z}}</span><br>"
        "<extra></extra>"
    )
    return hover_template

    # TODO : Define and return the hover template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''

    label_font_style = "font-family: 'Roboto Slab'; font-weight: bold; font-size: 12px;"
    value_font_style = "font-family: 'Roboto'; font-size: 12px; font-weight: normal;"

    hover_template = (
        f"<b><span style='{label_font_style}'>Date:</span></b> %{{x}}<br>"
        f"<b><span style='{label_font_style}'>Trees:</span></b> %{{y}}</b><br>"
        "<extra></extra>"
    )
    return hover_template
    # TODO : Define and return the hover template


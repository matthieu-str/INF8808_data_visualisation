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
    # TODO : Define and return the hover template
    
    hover_template = "<b><span style='font-family: Roboto Slab;'>{label}</span></b>: <span style='font-family: Roboto;'>{value}</span>"
    
    return hover_template.format(label="Neighborhood", value="%{y}") + "<br>" + \
           hover_template.format(label="Year", value="%{x}") + "<br>" + \
           hover_template.format(label="Trees Planted", value="%{z}") + "<extra>""</extra>"


def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    
    hover_template = "<b><span style='font-family: Roboto Slab;'>{label}</span></b>: <span style='font-family: Roboto;'>{value}</span>"
    
    return hover_template.format(label="Date", value="%{x|%d %b}") + "<br>" + \
           hover_template.format(label="Trees", value="%{y}") + "<extra>""</extra>"
    


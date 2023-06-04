'''
    Contains some functions to preprocess the data used in the visualisation.
'''

import pandas as pd

def round_decimals(my_df):
    '''
        Rounds all the numbers in the dataframe to two decimal points

        args:
            my_df: The dataframe to preprocess
        returns:
            The dataframe with rounded numbers
    '''
    # TODO : Round the dataframe
    my_df.GDP = my_df.GDP.round(decimals=2)
    my_df.CO2 = my_df.CO2.round(decimals=2)
    return my_df


def get_range(col, df1, df2):
    '''
        An array containing the minimum and maximum values for the given
        column in the two dataframes.

        args:
            col: The name of the column for which we want the range
            df1: The first dataframe containing a column with the given name
            df2: The first dataframe containing a column with the given name
        returns:
            The minimum and maximum values across the two dataframes
    '''
    # TODO : Get the range from the dataframes
    minimum = min(df1[col].min(), df2[col].min())
    maximum = max(df1[col].max(), df2[col].max())
    return [minimum, maximum]


def combine_dfs(df1, df2):
    '''
        Combines the two dataframes, adding a column 'Year' with the
        value 2000 for the rows from the first dataframe and the value
        2015 for the rows from the second dataframe

        args:
            df1: The first dataframe to combine (2000)
            df2: The second dataframe, to be appended to the first (2015)
        returns:
            The dataframe containing both dataframes provided as arg.
            Each row of the resulting dataframe has a column 'Year'
            containing the value 2000 or 2015, depending on its
            original dataframe.
    '''
    # TODO : Combine the two dataframes
    df1['Year'] = df1.shape[0] * [2000]
    df2['Year'] = df2.shape[0] * [2015]
    df3 = pd.concat([df1, df2])
    df3.reset_index(inplace=True, drop=True)
    return df3


def sort_dy_by_yr_continent(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.
    '''
    # TODO : Sort the dataframe
    my_df = my_df.sort_values(by=["Year", "Continent"])
    my_df.reset_index(inplace=True, drop=True)
    return my_df

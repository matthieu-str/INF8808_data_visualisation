'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe.Date_Plantation = pd.to_datetime(dataframe.Date_Plantation)

    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    dataframe = dataframe[(dataframe.Date_Plantation.dt.year >= start) &
                          (dataframe.Date_Plantation.dt.year <= end)]

    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    # counts the number of trees per year and neighborhood name
    dataframe = dataframe.groupby(by=[dataframe.Date_Plantation.dt.year, "Arrond_Nom"]).count()
    # drops columns that are not useful
    dataframe.drop(columns=["Date_Plantation", "Longitude", "Latitude"], inplace=True)
    # rename the counting column to "Counts"
    dataframe.rename(columns={"Arrond": "Counts"}, inplace=True)
    # reset index
    dataframe.reset_index(drop=False, inplace=True)

    return dataframe


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    piv = pd.pivot_table(yearly_df,
                         values="Counts",
                         index=["Arrond_Nom"],
                         columns=["Date_Plantation"],
                         fill_value=0) # fills empty cells with 0

    return piv


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    dataframe = dataframe[(dataframe.Date_Plantation.dt.year == year) &
                          (dataframe.Arrond_Nom == arrond)].groupby(pd.Grouper(key="Date_Plantation")).count()
    dataframe.drop(columns=["Arrond_Nom", "Longitude", "Latitude"], inplace=True)
    dataframe.index = pd.DatetimeIndex(dataframe.index)
    idx = pd.date_range(f'01-01-{year}', f'12-31-{year}')
    dataframe = dataframe.reindex(idx, fill_value=0)
    dataframe.rename(columns={"index": "Date_Plantation", "Arrond": "Counts"}, inplace=True)
    dataframe.reset_index(drop=False, inplace=True)

    return dataframe

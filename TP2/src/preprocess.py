'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # Create a new dataframe with the count of lines per player
    df_count = my_df[['Act', 'Player', 'Scene']].groupby(['Act', 'Player']).count()
    df_count.reset_index(inplace=True, drop=False)
    df_count.rename(columns={'Scene': 'LineCount'}, inplace=True)

    # Create a new dataframe counting the total number of line per act
    df_count_act = df_count.groupby(['Act']).sum()
    df_count_act.reset_index(inplace=True, drop=False)

    # Add a new column computing the percentage of lines per player for each act
    df_count['LinePercent'] = df_count.apply(lambda x: 100 * x.LineCount / float(df_count_act[df_count_act.Act == x.Act].LineCount), axis=1)

    return df_count


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other players
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # List of the top 5 players
    top_5_players = list(my_df[['Player', 'LineCount']].groupby('Player').sum().sort_values('LineCount', ascending=False).head(5).index)
    # List of all players
    all_players = list(my_df.Player.unique())
    # List of players that are not in the top 5
    not_top_5_players = list(set(all_players) - set(top_5_players))
    # Converting the previous list into a pattern
    pattern_not_top_5_players = '|'.join(not_top_5_players)

    # Create a new dataframe counting the total number of line per act
    df_count_act = my_df.groupby(['Act']).sum()
    df_count_act.reset_index(inplace=True, drop=False)

    # For loop that computes the line count and percentage for the OTHER category
    res = []
    number_of_acts = my_df.Act.max()
    for i in range(1, number_of_acts + 1):
        act = i
        total_other = float(my_df['LineCount'][(my_df.Act == i) & (my_df.Player.str.contains(pattern_not_top_5_players))].sum())
        total_other_perc = 100 * total_other / float(df_count_act[df_count_act.Act == i].LineCount)
        res.append([act, "OTHER", total_other, total_other_perc])

    # Crate a dataframe based on the previous results
    df_other = pd.DataFrame(res, columns=['Act', 'Player', 'LineCount', 'LinePercent'])
    # Create a new dataframe where we drop the "not top 5 players" rows
    df_count_top_5 = my_df.drop(my_df[my_df.Player.str.contains(pattern_not_top_5_players)].index)
    # Concatenate the top 5 players dataframe and the "other" dataframe
    df_count_top_5 = pd.concat([df_count_top_5, df_other])

    return df_count_top_5


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    my_df.Player = my_df.Player.str.title()
    return my_df

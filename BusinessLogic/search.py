"""
Project name - Search records based on multiple columns at same time
Programming Language Research Project
CST8333-351- Assignment 04
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: This script allows users to search the records based on multiple columns at the same time.
The users can select columns (min 1 and max 3) to search records from Oracle DB. The users also can select
operators i.e. >, < or = to perform search based on their selected columns on the records stored in the DB.

"""

from Persistence import dataAccess
import pandas as pd
from BusinessLogic import oracleDBconnector
from Presentation import menu


def search_from_database(clm_list, vl_list, oprtr_list):
    """

    This function searches records stored in Oracle database as per user input.
    :param clm_list: A list containing column names.
    :param vl_list: A list containing values to be searched upon.
    :param oprtr_list: A list containing values for preferred operators.
    """
    oracleDBconnector.read_all_records_from_oracle()
    oracleDBconnector.df_ora.numconf = pd.to_numeric(oracleDBconnector.df_ora.numconf,
                                                     errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.numdeaths = pd.to_numeric(oracleDBconnector.df_ora.numdeaths,
                                                       errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.numtotal = pd.to_numeric(oracleDBconnector.df_ora.numtotal,
                                                      errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.numtoday = pd.to_numeric(oracleDBconnector.df_ora.numtoday,
                                                      errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.pruid = pd.to_numeric(oracleDBconnector.df_ora.pruid,
                                                   errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.numprob = pd.to_numeric(oracleDBconnector.df_ora.numprob,
                                                     errors='coerce').astype('Int64')
    oracleDBconnector.df_ora.ratetotal = pd.to_numeric(oracleDBconnector.df_ora.ratetotal,
                                                       errors='coerce').astype('float64')

    if len(clm_list) == 1:
        dataAccess.printName()
        print('Note >> eq: equal; gt: grater than; lt: less than')
        print('Search records from DB for '
              + clm_list[0] + ' ' + oprtr_list[0] + ' ' + str(vl_list[0]) + ' >>\n')
        if oprtr_list[0] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[(oracleDBconnector.df_ora[clm_list[0]] > vl_list[0])]
        elif oprtr_list[0] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[(oracleDBconnector.df_ora[clm_list[0]] < vl_list[0])]
        elif oprtr_list[0] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[(oracleDBconnector.df_ora[clm_list[0]] == vl_list[0])]

    elif len(clm_list) == 2:
        dataAccess.printName()
        print('Note >> eq: equal; gt: grater than; lt: less than')
        print('Search records from DB for ' + clm_list[0] + ' ' +
              oprtr_list[0] + ' ' + str(vl_list[0]) + ' AND ' + clm_list[1] + ' ' + oprtr_list[1]
              + ' ' + str(vl_list[1]) + ' >>\n')
        if oprtr_list[0] == 'gt' and oprtr_list[1] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1])]

    elif len(clm_list) == 3:
        dataAccess.printName()
        print('Note >> eq: equal; gt: grater than; lt: less than')
        print('Search records from DB for '
              + clm_list[0] + ' ' + oprtr_list[0] + ' ' + str(vl_list[0]) + ' AND '
              + clm_list[1] + ' ' + oprtr_list[1] + ' ' + str(vl_list[1]) + ' AND '
              + clm_list[2] + ' ' + oprtr_list[2] + ' ' + str(vl_list[2]) + ' >>\n')
        if oprtr_list[0] == 'gt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'gt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] > vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'eq' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] == vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'gt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] > vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'eq' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] == vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'gt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] > vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'eq':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] == vl_list[2])]
        elif oprtr_list[0] == 'lt' and oprtr_list[1] == 'lt' and oprtr_list[2] == 'lt':
            rslt_df = oracleDBconnector.df_ora.loc[
                (oracleDBconnector.df_ora[clm_list[0]] < vl_list[0]) &
                (oracleDBconnector.df_ora[clm_list[1]] < vl_list[1]) &
                (oracleDBconnector.df_ora[clm_list[2]] < vl_list[2])]
    if rslt_df.empty:
        print('Data not match. Try again.')
    else:
        print(rslt_df.to_string(index=False))

    menu.search_list.clear()
    menu.search_values.clear()
    menu.operator_list.clear()
    menu.validate_response()

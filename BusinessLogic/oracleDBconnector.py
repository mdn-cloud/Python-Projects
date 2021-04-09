"""
Project name - Search records based on multiple columns at same time
Programming Language Research Project
CST8333-351- Assignment 04
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: This Script will connect the Oracle database and create table where I will update, insert, delete data
from the dataset.

"""
import pandas as pd
from Data.datesetPath import DatasetPath
from Persistence import dataAccess
from Presentation import menu
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CLOB

'''These variables can be accessed by any class or any method in the class by just writing the variable name.'''
table_name = 'canadacovid19'

'''The variable called engine creates a Dialect object tailored towards Oracle Database.'''
engine = create_engine('oracle+cx_oracle://mdebnath:mdebnathpwd@localhost:1521/?service_name=orcl',
                       max_identifier_length=128)

''' the conn variable is to Open the engine connection'''
conn = engine.connect()

'''the variable calles meta assigned to MetaData() that will hold the table called canadacovid19'''
meta = MetaData()
df_ora = []
# df_one = ""

'''canadacovid19 table structure'''
covid = Table(
    'canadacovid19', meta,
    Column('index', Integer),
    Column('pruid', CLOB),
    Column('prname', CLOB),
    Column('prnameFR', CLOB),
    Column('sdate', CLOB),
    Column('numconf', CLOB),
    Column('numprob', CLOB),
    Column('numdeaths', CLOB),
    Column('numtotal', CLOB),
    Column('numtoday', CLOB),
    Column('ratetotal', CLOB),
    Column('ratetotal', CLOB),
)


def insert_to_oracle():
    """

    This function is to inserts all 4632 records to Oracle database from list data structure
    that read these records initially from the given csv file.
    """

    from Persistence.dataAccess import read_dataset
    read_dataset(DatasetPath.covid19canada)
    pd_df = pd.DataFrame(dataAccess.records)
    pd_df.to_sql(table_name, engine, if_exists='replace', index=True, chunksize=100)


def add_a_record_to_oracle(new_record):
    """

    This function appends a new record to Oracle database from user input.
    :param new_record: Data of the new record given by the user.
    :type new_record: dataframe
    """

    new_df = pd.DataFrame(new_record, index=[get_last_index_from_oracle() + 1])
    new_df.to_sql(table_name, engine, if_exists='append', index=True)
    print("\nThe record has been created and stored to Oracle DB.\n")
    print(new_df)


def get_last_index_from_oracle():
    """

    This function returns the last index value from Oracle database.
    :returns last_record_index: last index value in the database
    :rtype: int
    """

    read_all_records_from_oracle()
    sort_df_ora = df_ora.sort_values(by=['index'])
    last_record_index = sort_df_ora["index"].iloc[-1]
    return last_record_index


def read_all_records_from_oracle():
    """

    This function will read all records from oracle database and saves to a list data structure.
    """
    global df_ora
    df_ora = pd.read_sql('select * from ' + table_name, engine)


def read_one_record_from_oracle(selected_index):
    """

    The function will use to reads one record from Oracle DB and saves to a Pandas dataframe.
    :param selected_index: Index of a saved record in DB.
    :type selected_index: int
    """

    global df_one
    df_one = pd.read_sql('select * from ' + table_name + ' covid where covid."index" = ' + str(selected_index), engine)
    if df_one.empty:
        print('Result from Oracle DB search >>\n')
        print('The requested record with index# ' + str(selected_index) + ' not found in the DB!')
        menu.validate_response()
    else:
        print("\nRecord with index# " + str(selected_index) + "\n")
        print(df_one.to_string(index=False))


def count_records_number_from_oracle():
    """

    This function will count and return the number of saved records in Oracle DB.
    :returns record_count: number of records saved in the DB
    :rtype: int
    """

    read_all_records_from_oracle()
    record_count = len(df_ora)
    return record_count


def delete_from_oracle(del_inx):
    """

    This function will delete a selected (given by the user) index of the record from Oracle BD
    :param del_inx: Index of a saved record in BD.
    :type del_inx: int
    """

    stmt = covid.delete().where(covid.c.index == del_inx)
    conn.execute(stmt)
    print('\nThe record with index number ' + str(del_inx) + ' has been successfully deleted from the DB.')


def update_a_record_to_oracle(id_update, name_update, nameFR_update, idate_update, numc_update, nump_update,
                              numd_update, numt_update, numtd_update, ratet_update, edited_record_index):
    """

    This Function take user input and update a record to Oracle DB
    :param id_update: For update id
    :param name_update: For update name
    :param nameFR_update: For update name in French
    :param idate_update: For update date
    :param numc_update: For update numconf
    :param nump_update: For update numprob
    :param numd_update: For update numdeaths
    :param numt_update: For update numtotal
    :param numtd_update: For update numtoday
    :param ratet_update: For update ratetotal
    :param edited_record_index: The index number of the record to be updated.

    """

    stmt = covid.update().values({covid.c.pruid: id_update, covid.c.prname: name_update,
                                  covid.c.prnameFR: nameFR_update, covid.c.sdate: idate_update,
                                  covid.c.numconf: numc_update, covid.c.numprob: nump_update,
                                  covid.c.numdeaths: numd_update, covid.c.numtotal: numt_update,
                                  covid.c.numtoday: numtd_update,
                                  covid.c.ratetotal: ratet_update}).where(covid.c.index == edited_record_index)
    conn.execute(stmt)
    print('\nUpdate and save successfully to Oracle Database as:')
    read_one_record_from_oracle(edited_record_index)
    menu.validate_response()

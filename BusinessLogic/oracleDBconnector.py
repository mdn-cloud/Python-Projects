import pandas as pd
from Data.datesetPath import DatasetPath
from Persistence import dataAccess
from Presentation import menu
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CLOB

'''These variables can be accessed by any class or any method in the class by just writing the variable name.'''
table_name = 'canadacovid19'

'''The engine creates a Dialect object tailored towards Oracle Database.'''
engine = create_engine('oracle+cx_oracle://mdebnath:mdebnathpwd@localhost:1521/?service_name=orcl',
                       max_identifier_length=128)

'''Open engine connection'''
conn = engine.connect()

'''MetaData object that will hold this table'''
meta = MetaData()

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

    This function inserts all 34458 records to Oracle database from list data structure
    that read these records initially from the given csv file.
    """

    from Persistence.dataAccess import read_dataset
    read_dataset(DatasetPath.covid19_new)
    pd_df = pd.DataFrame(dataAccess.records)
    pd_df.to_sql(table_name, engine, if_exists='replace', index=True, chunksize=100)


def add_a_record_to_oracle(new_record_to_add):
    """

    This function appends a new record to Oracle database as per user input.
    :param new_record_to_add: Data of the new record.
    :type new_record_to_add: dataframe
    """

    new_df = pd.DataFrame(new_record_to_add, index=[get_last_index_from_oracle()+1])
    new_df.to_sql(table_name, engine, if_exists='append', index=True)
    print("\nFollowing record has been created and stored to Oracle Database.\n")
    print(new_df)


def get_last_index_from_oracle():
    """

    This function returns the last index value from the saved
    records in the Oracle database.
    :returns last_record_index: last index value from the saved records in the database
    :rtype: int
    """

    read_all_records_from_oracle()
    sort_df_ora = df_ora.sort_values(by=['index'])
    last_record_index = sort_df_ora["index"].iloc[-1]
    return last_record_index


def read_all_records_from_oracle():
    """

    This function reads records from oracle database and saves to a list data structure.
    """
    global df_ora
    df_ora = pd.read_sql('select * from ' + table_name, engine)


def read_one_record_from_oracle(selected_index):
    """

    This function reads one record from Oracle database and
    saves to a Pandas dataframe.
    :param selected_index: Index of a saved record in Oracle database.
    :type selected_index: int
    """

    global df_one
    df_one = pd.read_sql('select * from ' + table_name + ' covid where covid."index" = ' + str(selected_index),
                         engine)
    if df_one.empty:
        print('Result from Oracle Database search >>\n')
        print('The requested record with index# ' + str(selected_index) + ' not found in Oracle Database!')
        menu.validate_response()
    else:
        print("\nRecord with index# " + str(selected_index) + "\n")
        print(df_one.to_string(index=False))


def count_records_number_from_oracle():
    """

    This function counts and returns the number of records that
    are saved in Oracle database.
    :returns record_count: number of records saved in the database
    :rtype: int
    """

    read_all_records_from_oracle()
    record_count = len(df_ora)
    return record_count


def delete_from_oracle(del_index):
    """

    This function deletes a record from Oracle database with
    a specific index# as per user input.
    :param del_index: Index of a saved record in Oracle database.
    :type del_index: int
    """

    stmt = covid.delete().where(covid.c.index == del_index)
    conn.execute(stmt)
    print('\nThe record with index# ' + str(del_index) + ' has been successfully deleted from Oracle Database.')


def update_a_record_to_oracle(id_update, name_update, nameFR_update, idate_update, numc_update, nump_update,
                              numd_update, numt_update, numtd_update, ratet_update, edited_record_index):
    """

    This function updates an existing record to Oracle database from user input.
    :param id_update: Updated id.
    :type id_update: String
    :param idate_update: Updated date.
    :type idate_update: String
    :param cases_update: Updated number of cases.
    :type cases_update: int
    :param deaths_update: Updated number of deaths.
    :type deaths_update: int
    :param name_fr_update: Updated name in French.
    :type name_fr_update: String
    :param name_en_update: Updated name in English.
    :type name_en_update: String
    :param edited_record_index: The index number of the record to be updated.
    :type edited_record_index: int
    """

    stmt = covid.update().values({covid.c.pruid: id_update, covid.c.prname: name_update,
                                  covid.c.prnameFR: nameFR_update, covid.c.sdate: idate_update,
                                  covid.c.numconf: numc_update, covid.c.numprob: nump_update,
                                  covid.c.numdeaths: numd_update, covid.c.numtotal: numt_update,
                                  covid.c.numtoday: numtd_update,
                                  covid.c.ratetotal: ratet_update}).where(covid.c.index == edited_record_index)
    conn.execute(stmt)
    print('\nThe record has been updated and saved to Oracle Database as follows:')
    read_one_record_from_oracle(edited_record_index)
    menu.validate_response()
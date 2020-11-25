# test_mpi_writers.py

from utils.db import get_db, init_mongo
from utils.models import NoSQLSerializer
from utils.generators import gen_mpi_insert

from .global_test_setup import testlogger

from mpi.writers import write_mpi_data

import pandas as pd

import pytest



@pytest.fixture
def test_data():
    query = f"SELECT * FROM mpi_vectors_test"
    return gen_mpi_insert(
        pd.read_sql_query(query, get_db())
    )



def test_nosql_insert_writer(test_data):
    testlogger.info('Starting Test Write_Insert', __name__)
    dat = []
    row = next(test_data)
    dat.append(row)

    write_mpi_data(dat, 'nosql')


def test_nosql_update_writer(test_data):
    testlogger.info('Starting Test Write_Update', __name__)
    dat = []
    for row in test_data:
        dat.append(row)

    write_mpi_data(dat, dbtype='nosql', update=True)
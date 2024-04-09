import psycopg2
from sqlalchemy import create_engine



def get_db_engine(loc):
    try:
        if loc == "loc_b":
            local_db = 'postgres:0000@localhost:5432/postgres'
            query = 'postgresql+psycopg2://{}'.format(local_db)
            engine = create_engine(query)
            return engine
    except Exception as e:
        return False

def get_db_connector(loc, schema):
    if loc == 'loc_b':
        db_connector = get_db_engine(loc)
    return db_connector

def execute_query(loc, db_connector, query):
    try:
        conn = db_connector.raw_connection()
        cur = conn.cursor()
        try:
            cur.execute(query)
            status = True
        except Exception as e:
            print("Local DB connection error: ", loc, e)
            status = False
        else:
            conn.commit()
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print("DB connection error: ", loc, e)
        status = False
    return status

def create_schema(loc, schema):
    query = f'CREATE SCHEMA IF NOT EXISTS {schema};'
    db_connector = get_db_connector(loc, schema)
    execute_query(loc, db_connector, query)
    return None


create_schema('loc_b','alignment_tool')
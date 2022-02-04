
from sqlalchemy import create_engine
import createtable_db, insert_db, delete_db, update_db
# import select_db, alias_db

engine = create_engine('sqlite:///college.db', echo = True)  



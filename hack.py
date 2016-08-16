import sys
import subprocess

def get_output():
    s2_out = subprocess.check_output([sys.executable, "test.py", "34"])
    print s2_out
    pass
get_output()

engine = sqlalchemy.create_engine('sqlite:///auth.db', encoding='utf-8')
engine.execute('CREATE TABLE users (user text, password text)')
engine.execute('INSERT INTO %s VALUES (?, ?)' % table, [
    ['name1', 'pwd1'],
    ['name2', 'pwd2']
])

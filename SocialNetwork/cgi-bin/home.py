#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import base
from model import User

base.startPage()


def homePage(result):
    if isinstance(result, str):
        base.plainHeader()
        print(f'''
            <h1>{result}</h1>
        ''')
    elif isinstance(result, User):
        base.header(result.email)
        print(f'''
            <h1>Welcome {result.name}</h1>
        ''')
    else:
        base.header(result[1])
        print(f'''
            <h1>Welcome {result[0]}</h1>
        ''')
    base.footer()

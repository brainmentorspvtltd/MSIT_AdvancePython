#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import base


def homePage(result):
    base.header()
    if isinstance(result, str):
        print(f'''
            <h1>{result}</h1>
        ''')
    else:
        print(f'''
            <h1>Welcome {result[0]}</h1>
        ''')
    base.footer()

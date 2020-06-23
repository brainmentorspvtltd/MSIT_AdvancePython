#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import base


def homePage(result):
    base.header()
    if isinstance(result, str):
        print(f'''
        <div class="container">
            <h1>{result}</h1>
        </div>
        ''')
    else:
        print(f'''
        <div class="container">
            <h2>Welcome {result[0]}</h2>
        </div>
        ''')
    base.footer()

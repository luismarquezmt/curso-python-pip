import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def getList():
    return [1, 2, 3]


@app.get('/perras')
def getList():
    return { 'perras':'perrosas'}
  
@app.get('/htmlsoso',response_class=HTMLResponse)
async def getList():
    return  """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


def run():
    store.getCategories()


if __name__ == "__main__":
    run()

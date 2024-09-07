# banks/views.py
from django.http import HttpResponse

def home(request):
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
            }

            h1 {
                font-size: 3em;
                color: #333;
            }

            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                font-size: 1.2em;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to our page</h1>
        <button onclick="window.location.href='/gql/'">Visit for GQL Testing</button>
    </body>
    </html>
    '''
    return HttpResponse(html_content)

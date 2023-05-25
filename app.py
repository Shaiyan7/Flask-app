from flask import Flask, render_template

app = Flask(__name__)

blogs = [
    {
        'title': 'Introduction to Flask',
        'content': 'This blog provides an introduction to Flask and its basic features.Flask is an API of Python that allows us to build up web-applications. It is a collection of modules and libraries that helps the developer to write applications without writing the low-level codes such as protocols, thread management, etc.'
    },
    {
        'title': 'Creating Routes in Flask',
        'content': 'App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler. '
    },
    {
        'title': 'Working with Templates in Flask',
        'content': 'In Flask, you can use the Jinja templating language to render HTML templates. A template is a file that can contain both fixed and dynamic content. When a user requests something from your application (such as an index page, or a login page), Jinja allows you to respond with an HTML template where you can use many features that are not available in standard HTML, such as variables, if statements, for loops, filters, and template inheritance. These features allow you to efficiently write easy-to-maintain HTML pages.'
    },
    {
        'title': 'Handling Forms in Flask',
        'content': '<form> is an HTML element to collect input data containing interactive controls. It provides facilities to input text, number, values, email, password, and control fields such as checkboxes, radio buttons, submit buttons, etc. '
    }
]

@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)

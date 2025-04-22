from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Serve files from the "secret" folder
@app.route('/secret/<filename>')
def secret_file(filename):
    secret_folder = os.path.join(os.getcwd(), 'secret')  # Get the path to the "secret" folder
    
    # Check if the file exists in the "secret" folder
    if os.path.isfile(os.path.join(secret_folder, filename)):
        return send_from_directory(secret_folder, filename)
    else:
        # If the file doesn't exist, show a 404 error
        abort(404)

# Serve robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory(os.getcwd(), 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)

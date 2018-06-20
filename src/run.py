"""
Main module for flask app.
"""
from creat_app import create_app

if __name__ == '__main__':
    app = create_app(__name__)
    app.run(debug=True, host='0.0.0.0', port=5000)

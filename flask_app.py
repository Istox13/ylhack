from database import *

@app.route('/')
def main_page():
    pass

if __name__ == "__main__":
    app.run('localhost', port=5000, debug=True)
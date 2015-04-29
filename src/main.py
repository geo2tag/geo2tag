from flask import Flask, current_app
from read_queries import read_queries
from write_queries import write_queries

app = Flask(__name__)
app.register_blueprint(read_queries)
app.register_blueprint(write_queries)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

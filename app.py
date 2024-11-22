from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    # Load the data
    df = pd.read_csv('Tiger_Migration_Data_Adjusted.csv')

    # Path to the map HTML file
    map_path = 'static/Tiger_Migration_Map.html'

    return render_template('index.html', map_path=map_path,
                           df=df.to_html(classes='table table-striped table-bordered table-hover', index=False))


if __name__ == "__main__":
    app.run(debug=True)

from flask import render_template

import config, logging
from models import Fruit

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    fruits = Fruit.query.all()
    return render_template("home.html", fruits=fruits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, log_level=True)
    

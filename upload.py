from flask import abort, make_response, request

#from config import db
#from models import Fruit, fruits_schema, fruit_schema
from werkzeug.utils import secure_filename
import os

def upload():
    if 'image' in request.files:
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join("/var/www/product-catalog/static/images",filename))
        return 'File uploaded successfully'

    return 201


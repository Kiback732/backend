from flask import request, jsonify, abort, send_from_directory
from werkzeug.utils import secure_filename
from api import api, db, ma, log
from api.models import Advertisement, AdvertisementSchema
from .utils import create_new_folder, allowed_image

import os
import json

adv_schema = AdvertisementSchema()
advs_schema = AdvertisementSchema(many=True)

@api.route('/')
def hello():
    return jsonify('Hello World!')

@api.route('/api/advertisement', methods=['GET'])
def get_all_ad():
    ad = Advertisement.query.all()
    result = advs_schema.dump(ad)
    return jsonify(result)

@api.route('/api/advertisement/<int:id>', methods=['GET'])
def get_ad_detail(id):
    ad = Advertisement.query.get(id)
    return adv_schema.jsonify(ad)

@api.route('/api/advertisement', methods=['POST'])
def create_ad():
    if request.form.get('title'):
        title = request.form.get('title')
    else:
        msg = 'title required'
        log.error(msg)
        return jsonify(message=msg), 400

    if request.form.get('description'):
        description = request.form.get('description')
    else:
        msg = 'description required'
        log.error(msg)
        return jsonify(message=msg), 400

    if request.files:
        img = request.files['image']

        img_name = secure_filename(img.filename)
        if img_name == "":
            msg = 'filename required'
            log.error(msg)
            return jsonify(message=msg), 400

        if allowed_image(img_name):
            create_new_folder(api.config['UPLOAD_FOLDER'])
            saved_path = os.path.join(api.config['UPLOAD_FOLDER'], img_name)
            img.save(saved_path)
            img_db_name = f'upload/{img_name}'
        else:
            msg = 'not allowed image format'
            log.error(msg)
            return jsonify(message=msg), 400
    else:
        msg = 'image required'
        log.error(msg)
        return jsonify(message=msg), 400

    ad = Advertisement(title=title, description=description, image=img_db_name)
    db.session.add(ad)
    db.session.commit()

    return adv_schema.jsonify(ad)

@api.route('/api/advertisement/<int:id>', methods=['DELETE'])
def remove_ad(id):
    ad = Advertisement.query.get(id)
    db.session.delete(ad)
    db.session.commit()
    return adv_schema.jsonify(ad)

@api.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@api.route('/upload/<path:path>', methods=['GET'])
def send_images(path):
    return send_from_directory(api.config['UPLOAD_FOLDER'], path)

@api.route('/api/healthz', methods=['GET'])
def healthcheck():
    response_code = 503
    response_message = 'Fail'

    try:
        with db.engine.connect() as connection:
            connection.execute('SELECT 1;')
            state = True
    except Exception as e:
        state = False
        message = str(e)
        log.error(e)

    if state:
        response_code = 200
        response_message = 'Ok'

    return jsonify({'healthy': response_message}), response_code

from flask import render_template, Flask, g, jsonify
from db import Database

app = Flask(__name__)

DATABASE_PATH = './dev/furlenco.db'


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/beds')
def beds_template():
    beds = get_db().get_beds()
    return render_template('products/beds/beds.html', beds=beds)


@app.route('/bed')
def bed_template():
    return render_template('products/beds/bed.html')


@app.route('/chairs')
def chairs_template():
    chairs = get_db().get_chairs()
    return render_template('products/chairs/chairs.html', chairs=chairs)


@app.route('/chair')
def chair_template():
    return render_template('products/chairs/chair.html')


@app.route('/sofas')
def sofas_template():
    sofas = get_db().get_sofas()
    return render_template('products/sofas/sofas.html', sofas=sofas)


@app.route('/sofa')
def sofa_template():
    return render_template('products/sofas/sofa.html')


@app.route('/wardrobes')
def wardrobes_template():
    wardrobes = get_db().get_wardrobes()
    return render_template('products/wardrobes/wardrobes.html', wardrobes=wardrobes)


@app.route('/wardrobe')
def wardrobe_template():
    return render_template('products/wardrobes/wardrobe.html')


@app.route('/tables_desks')
def tables_desks_template():
    desks = get_db().get_desks()
    return render_template('products/desks/tables_desks.html', desks=desks)


@app.route('/desk')
def table_desk_template():
    return render_template('products/desks/table_desk.html')


@app.route('/outdoor')
def outdoors_template():
    outdoors = get_db().get_outdoors()
    return render_template('products/outdoor/outdoor.html', outdoors=outdoors)


@app.route('/outdoors')
def outdoor_template():
    return render_template('products/outdoor/outdoors.html')


@app.route('/test')
def test_template():
    return render_template('test.html')


@app.route('/api/get_beds', methods=['GET'])
def api_get_beds():
    # n = request.args.get('n', default=6)
    beds = get_db().get_beds()
    return jsonify(beds)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = Database(DATABASE_PATH)
    return db


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/api/get_bed/<bid>', methods=['GET'])
def api_get_bed(bid):
    # n = request.args.get('n', default=6)
    bed = get_db().get_bed(bid)
    return jsonify(bed)


@app.route('/api/get_chair/<chid>', methods=['GET'])
def api_get_chair(chid):
    # n = request.args.get('n', default=6)
    chair = get_db().get_chair(chid)
    return jsonify(chair)


@app.route('/api/get_sofa/<sid>', methods=['GET'])
def api_get_sofa(sid):
    # n = request.args.get('n', default=6)
    sofa = get_db().get_sofa(sid)
    return jsonify(sofa)


@app.route('/api/get_wardrobe/<wid>', methods=['GET'])
def api_get_wardrobe(wid):
    # n = request.args.get('n', default=6)
    wardrobe = get_db().get_wardrobe(wid)
    return jsonify(wardrobe)


@app.route('/api/get_desk/<tid>', methods=['GET'])
def api_get_desk(tid):
    # n = request.args.get('n', default=6)
    desk = get_db().get_desk(tid)
    return jsonify(desk)


@app.route('/api/get_outdoor/<oid>', methods=['GET'])
def api_get_outdoor(oid):
    # n = request.args.get('n', default=6)
    outdoor = get_db().get_outdoor(oid)
    return jsonify(outdoor)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

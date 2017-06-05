from bottle import route, run, template, HTTPResponse, request
from manager import Manager
import json

@route('/')
def index():
    return '<h1>artists search engine</h1> you can filter by "name", "aliase_name", "tag", and "limit"<br>For example, http://localhost:8080/artists?name=Queen&limit=2'

@route('/artists')
def index():
    name = request.query.get('name')
    aliase_name = request.query.get('aliase_name')
    tag = request.query.get('tag')
    limit = request.query.get('limit')

    manager = Manager()
    artists_list = manager.get_artists(name=name, aliase_name=aliase_name, tag=tag, limit=limit)
    artists_json = json.dumps(artists_list)

    r = HTTPResponse(status=200, body=artists_json)
    r.set_header('Content-Type', 'application/json')
    return r

if __name__ == '__main__':
    run(host='localhost', port=8080)

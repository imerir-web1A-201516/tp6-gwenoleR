# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import json, os, psycopg2, urlparse
from db import Db # voyez db.py

app = Flask(__name__)
app.debug = True

##################################################################

@app.route('/debug/db/reset')
def route_dbinit():
  """Cette route sert à initialiser (ou nettoyer) la base de données."""
  db = Db()
  db.executeFile("database_reset.sql")
  db.close()
  return "Done."

#-----------------------------------------------------------------

@app.route('/prets', methods=['GET'])
def prets_fetchall():
  db = Db()
  result = db.select("SELECT * FROM prets WHERE statut='prete'")
  db.close()
  
  resp = make_response(json.dumps(result))
  resp.mimetype = 'application/json'
  return resp

#-----------------------------------------------------------------

@app.route('/prets', methods=['POST'])
def pret_add():
  try :
    data = request.get_json()
    db = Db()
    result = db.select("INSERT INTO prets (qui, quoi, statut) VALUES (%(qui)s,%(quoi)s, %(statut)s) RETURNING id",{
      'qui' : data['qui'],
      'quoi' : data['quoi'],
      'statut' : data['statut']
    })
    
    
    resp = make_response('', 201)
    resp.mimetype = 'application/json'
    resp.headers['Location'] = "/prets/%d" % result[0]['id']
    db.close()
    return resp
  except:
    resp = make_response('', 400)
    return resp

#-----------------------------------------------------------------

@app.route('/prets/<int:id>', methods=['GET'])
def prets_fetchone(id):
  db = Db()
  result = db.select("SELECT * FROM prets WHERE id=%(id)s",{
    'id' : id
  })
  db.close()
    
  if len(result) != 1:
    return make_response("Not found", 404)
    
  resp = make_response(json.dumps(result),200)
  resp.mimetype = 'application/json'
  return resp
  
#-----------------------------------------------------------------

@app.route('/prets/<int:id>', methods=['PUT'])
def prets_changeone(id):
  try :
    data = request.get_json()
    db = Db()
    result = db.execute("UPDATE prets SET qui = %(qui)s, quoi = %(quoi)s, statut = %(statut)s WHERE id=%(id)s",{
      'qui' : data['qui'],
      'quoi' : data['quoi'],
      'statut' : data['statut'],
      'id' : id
    })
    
    
    resp = make_response('', 204)
    db.close()
    return resp
  except:
    resp = make_response('', 400)
    return resp
  
#-----------------------------------------------------------------

if __name__ == "__main__":
  app.run()

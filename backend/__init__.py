from flask import Flask, render_template
from flask_cors import CORS
import sqlite3

dbpath = '/var/www/itsp_tcb/backend/data.db'
emmap = ['anger', 'fear', 'happy', 'sad', 'neutral']
app = Flask(__name__, template_folder='.')
CORS(app)

#@app.route('/')
#def index():
#	return render_template('index1.html')

@app.route('/resetdb', methods=['POST'])
def resetdb():
	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()
	cur.execute('delete from emotion_count')
	cur.execute('insert into emotion_count values (0,0,0,0,0)')
	conn.commit()
	conn.close()
	return ('', 204)


@app.route('/getall')
def getall():
	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()
	res = cur.execute('select * from emotion_count').fetchone()
	conn.close()
	return {'anger': res[0], 'fear': res[1], 'happy': res[2], 'sad': res[3], 'neutral': res[4]}


@app.route('/inc/<em>', methods=['POST'])
def inc(em):
	em = int(em)

	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()
	cur.execute('update emotion_count set %s = %s + 1' % (emmap[em], emmap[em]))
	conn.commit()
	return ('', 204)


@app.route('/dec/<em>', methods=['POST'])
def dec(em):
	em = int(em)
	
	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()
	cur.execute('update emotion_count set %s = %s - 1' % (emmap[em], emmap[em]))
	conn.commit()
	return ('', 204)

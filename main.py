import os,datetime
from pytz import timezone
from datetime import date
from time import mktime

from flask import Flask, render_template, make_response, abort, request
app = Flask(__name__)

def create_ET_header():
	info = os.fstat(os.open( "./templates/index.html", os.O_RDWR|os.O_CREAT))
	cur_time = datetime.datetime.now(tz=timezone("GMT"))
	microsec = datetime.datetime.now(tz=timezone("GMT")).strftime("%f")
	return '"'+str(hex(info.st_ino))[2:]+'-'+hex(info.st_size)[2:]+'-'+(hex(int(mktime(cur_time.timetuple()) * 1000000) + int(microsec))[2:])+'"'

def decode_answer(hex_ans):
	ans_list = [ hex_ans[i:i+2] for i in range(0, len(hex_ans), 2) ]
	decoded_list = [ chr(int(i,16)) for i in ans_list ]
	return ''.join(decoded_list)

message = 'will be loaded from message.txt'
hex_answer=''
cur_bit = -1
ET_header = create_ET_header()

@app.route('/')
def root():
	return make_response(render_template('index.html')) 

@app.route('/sock')
def main():
	global cur_bit, ET_header
	
	if cur_bit < len(message) - 1:
		cur_bit = cur_bit + 1
	else:
		abort(404)
	
	response = make_response(render_template('sock.html') ) 
	if message[cur_bit] == '1':
		ET_header = create_ET_header()
	response.headers['ETag'] = ET_header;
	
	return response

@app.route('/ans')
def get_answer():
	global hex_answer

	answer = request.headers['If-Range'][1:-1]
	hex_answer += answer
	
	if len(answer) < 32:
		answer = decode_answer( hex_answer )
		print answer
		fname  = 'answers/'+datetime.datetime.now(tz=timezone("GMT")).strftime("message from %d.%m.%y %H:%M:%S")
		open(fname, 'w+').write( answer )
		hex_answer = ''
	
	return "Got it!"

@app.route('/start')
def init():
	global message,cur_bit
	message = open("message.txt").read()
	cur_bit = 0
	ET_header = create_ET_header()
	return "New message started"

if __name__=='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)

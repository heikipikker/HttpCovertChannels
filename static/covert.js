function sendRequest(url, mode){
 var xhr=new XMLHttpRequest();
 xhr.open('GET',url,mode);
 xhr.send();
}


function getHeader(url, mode){
 var xhr=new XMLHttpRequest();
 xhr.open('GET', url, mode);
 xhr.send();
 if (xhr.status != 200){
  throw	"message_end"
 }
 return xhr.getResponseHeader('ETag');
}

function start(){
 sendRequest('start', false);
}

function get_data(){
	var header=getHeader('sock', false);
	var interval=setInterval(function()
	{
		try{
			var newHeader=getHeader('sock'); 
		}
		catch(e){ 
			clearInterval(interval);
			console.log(message);
			return;
			}
		if (newHeader!==header)
		    {
		     console.log('1');
		     message=message+'1';
		     header=newHeader;
		    }
		else
		    {
		     console.log('0');
		      message=message+'0';
		    }
	},100,header,message);
}


var message='';
function get_message() {
	setTimeout(start,500);
	setTimeout(get_data,500);
}


function encode_data (str) {
	var result="";
	for(i=0;i<str.length;++i) {
		result+=str.charCodeAt(i).toString(16);
	}
	return result;
}

function send_piece(data){
	if (data!==''){
		var xhr = new XMLHttpRequest();
		xhr.open('GET','/ans', false);
		xhr.setRequestHeader('If-Range','"'+ data + '"');
		xhr.send();
	}
}


function send_answer(str) {
	var encodedData = encode_data(str);

//	console.log(encodedData);
//	console.log("encodedData length: " + encodedData.length);

	var max_segment_length = 32;
	var n_pieces = Math.floor( encodedData.length / max_segment_length);
	for (i=0;i<=n_pieces;i++){
		t=max_segment_length*i;
		send_piece(encodedData.substring(t,t+max_segment_length));
	}
}

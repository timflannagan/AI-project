let {PythonShell} = require('python-shell');

const FACEBOOK_ACCESS_TOKEN = 'EAAFK6Y86ZASMBAHPUdFBPjVmjQ6Ja2gHi8dQ5oJ7HIIZCDCE5JrGz1ZCVMNOVNSprEPZANOkJ2NeKYZALeXkqqCL5909b2esU3C6OcmLTJTMNy1Vdzj9udDf1Y0jZCDnaF6Kwls6of24KZAOq7jTNpyZBVxcOvjBOqh8t4dBPlCTWgZDZD';
const request = require('request');

const sendTextMessage = (senderId, text) => {

	request({
	url: 'https://graph.facebook.com/v2.6/me/messages',
	qs: {access_token: FACEBOOK_ACCESS_TOKEN},
	method: 'POST',
	json: {

	recipient: {id: senderId},
	message: {text},
	}
	});
};

module.exports = (event) => {
	const senderId = event.sender.id;
	const message = event.message.text; 

	//specify options to run Python Script
	let options = {
		mode: 'text',
		pythonPath: '/usr/bin/python',
		pythonOptions: ['-u'],
		scriptPath: './helpers',
		args:[message]
	};
	PythonShell.run('main.py', options, function(err, results){
			
		//create a file and write the response
		var fs = require("fs");
		fs.writeFile('response.txt', results, function(err){
			if(err){
				return console.error(err);
			}
		})	
	});

	//read the response
	var fs = require("fs");
	fs.readFile('response.txt',function(err, data) {
		if(err){
			return console.error(err);
		}
	//send response
	sendTextMessage(senderId, data.toString());
	});

	//delete file
	fs.unlink('response.txt', function(err)
	{
		if(err){
			return console.error(err);
		}
	});
};

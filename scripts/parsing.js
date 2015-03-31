var PythonShell = require('python-shell')
module.exports.execute = function(string_to_parse){

	var options = {
	  mode: 'text',
	  pythonPath: 'python',
	  pythonOptions: ['-u'],
	  scriptPath: ".\\scripts\\python\\",
	  args: [string_to_parse]
	};


	PythonShell.run('parse.py', options, function (err, results) {
	  if (err) throw err;
	  // results is an array consisting of messages collected during execution 
	  console.log('results: %j', results);
	});
}
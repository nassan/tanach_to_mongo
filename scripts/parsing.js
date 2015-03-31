var PythonShell = require('python-shell')
var path = require('path')

module.exports.execute = function(string_to_parse){

	var options = {
	  mode: 'text',
	  pythonPath: 'python',
	  pythonOptions: ['-u'],
	  scriptPath: path.normalize("./scripts/python"),
	  args: [string_to_parse]
	};


	PythonShell.run('parse.py', options, function (err, results) {
	  if (err) throw err;
	  // results is an array consisting of messages collected during execution 
	  for (var i = 0; i < results.length; i++) {
	  	console.log(results[i] + "\n")
	  };
	});
}
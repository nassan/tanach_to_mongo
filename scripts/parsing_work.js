// Includes
var cheerio = require('cheerio')
var S = require('string')

// Function definitions

module.exports.loadForParsing = function(perek_string){
	var chrio = cheerio.load(perek_string)
	getPerekMetaData(chrio)
}

var getPerekMetaData = function(chrio){
	
	var meta = {
		sefer_title : null,
		perek_letter : null,
		perek_index : null
	}

	var both_string = chrio("body").find("h1")
	var both_array = both_string.split("פרק")
	console.log(both_array)
}
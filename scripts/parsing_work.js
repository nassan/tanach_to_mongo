// Includes
var Iconv = require('iconv').Iconv;
var cheerio = require('cheerio')
var S = require('string')
var fs = require('fs')
// Function definitions

var getPerekMetaData = function(chrio){
	
	var meta = {
		sefer_title : null,
		perek_letter : null,
		perek_index : null
	}

	var both_string = chrio("body").find("h1")
	var both_string_test = both_string.text()
	console.trace()
	// var both_array = both_string.split("פרק")
	// fs.writeFileSync("test.html", both_string)
	// console.log(both_array)
}

var decode =function (content) {
  var iconv = new Iconv('CP1255', 'UTF-8//TRANSLIT//IGNORE');
  var buffer = iconv.convert(content);
  return buffer.toString('utf8');
}

module.exports.loadForParsing = function(perek_string){
	var chrio = cheerio.load(decode(perek_string))
	getPerekMetaData(chrio)
}
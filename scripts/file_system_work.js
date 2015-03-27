// Incudes
var fs = require('fs')
var S = require('string')
var parse = require('./parsing_work')

var directory_path = "tanach\\x\\"


var filterFileNames = function(list){
	var filtered_list = []

	// For loop to null out the 
	for (var i = 0; i < list.length; i++) {
		var str = S(list[i])
		if (str.length > 8 && 
			str.endsWith('.htm') && 
			containsANumber(str))
			{
				filtered_list.push(list[i])
			}
	}

	// Begin opening the files
	openFiles(filtered_list)

}

var openFiles = function(list){
	// for (var i = 0; i < list.length; i++) {
	for (var i = 0; i < 1; i++) {
		readPerekLevelFile(directory_path + list[i])
	}
}

var listDirectoryCB = function(err, files){
	if(err){console.log(err)}

	filterFileNames(files)	
}

var listDirectory = function(dir_path){
	fs.readdir(dir_path, listDirectoryCB)
}

var readPerekLevelFile = function(file_path){
	var options = {
		flags : 'r',
		encoding : 'utf8'
	}

	// fs.createReadStream(file_path, options)
	
	fs.readFile(file_path, options, readPerekLevelFileCB)
}

var readPerekLevelFileCB = function(err, data){
	if(err) throw err;

	parse.loadForParsing(data)

}

var containsANumber = function(Str){
	if (Str.contains('1') ||
		Str.contains('2') ||
		Str.contains('3') ||
		Str.contains('4') ||
		Str.contains('4') ||
		Str.contains('5') ||
		Str.contains('6') ||
		Str.contains('7') ||
		Str.contains('8') ||
		Str.contains('9') ||
		Str.contains('0')) 
		{
			return true
		}
	return false
}

listDirectory(directory_path)
var EventEmitter = require('events').EventEmitter
var Parsing = require('./parsing')
var emitter = new EventEmitter()

// Listeners
emitter.on('ready_to_parse', function(string_to_parse){
	Parsing.execute(string_to_parse)
})
module.exports.emitter = emitter
var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var Pasuk  = new Schema({
	sefer_title : String,
	perek_letter : String,
	perek_index : Number,
	pasuk_letter : String,
	pasuk_index : Number,
	pasuk_text :String
})

Pasuk.methods.pretty = function(){
	return this.pasuk_index.toString() + ' ' + this.pasuk_text.toString()
}

module.exports = Pasuk


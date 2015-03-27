// Includes
var mongoose = require('mongoose')
var pasukSchema = require('./schema')

// Initial declarations
var db = mongoose.connection
var url = 'mongodb://localhost:27017/myproject';

//function definitions
onOpen = function(cb){
	console.log("Succesfully connected")

	// Create mongoose model from Schema
	var Pasuk = mongoose.model('Pasuk', pasukSchema)

	// var test_pasuk = new Pasuk({pasuk_index : 77, pasuk_text : 'שדגכעיחלך'})
	// console.log(test_pasuk.pretty())
	db.close()
}

// db event subscriptions
db.on('error', console.error.bind(console,'connection error:'))
db.once('open', onOpen)





// code execution
mongoose.connect(url) 

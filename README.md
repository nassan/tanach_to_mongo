# Tanach to Mongo
An attempt to get Tanach into a MongoDB database

MongoDb documents are a Pasuk schema, structured as follows:

```JavaScript
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
```

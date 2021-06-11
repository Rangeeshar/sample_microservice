// server.js

// call the packages we need
var express    = require('express');        // call express
var app        = express();                 // define our app using express
const crypto = require("crypto");

var port = process.env.PORT || 8080; // get port

global.api_keys = {};
// our route
app.get('/api/generate_id', function(req, res) {
    if (req.query.user){
        const id = crypto.randomBytes(16).toString("hex");
        global.api_keys[id] = req.query.user;
        res.json({ message: "here is your random id "+req.query.user, success:true, data:{api_key:id}}); 
    }
        res.json({ message: "username required", success:false, data:{}}); 
});

app.get("/api/validate", function(req, res) {
    if (global.api_keys[req.query.api_key]){
       res.json({message: "valid user", success:true, data:{}}) 
    }
    res.json({message: "invalid user"})
})

// run server
app.listen(port);
console.log('Magic happens on port ' + port)

// exiting gracefully
process.on('SIGINT', () => {
    console.log('Process terminated')
    process.exit(0);
})
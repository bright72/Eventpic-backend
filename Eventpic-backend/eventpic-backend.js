const express = require('express');  
var request = require('request');  
const app = express(); 
const port = 9000;

app.get("/", (req, res) => res.send("Welcome to Java!"));  
app.get("/testapi", (req, res) => res.send("Work")); 
app.get("/emailbakcend", (req, res) => {
  var data = {
    "email": "haritsuttisaksri@gmail.com",
    "img": ["dsd01","dsd02"]
}

request(res.send(data)

)

}); 
// app.post("/user", (req,res) => {
//     console.log(req.body.email);
//     res.send('haha');
//     });
    
app.listen(port, () => console.log(`Example app listening on port ${port}!`));  
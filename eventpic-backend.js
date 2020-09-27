const express = require('express');  
var request = require('request');  
const app = express(); 
const port = 9000;

app.get("/", (req, res) => res.send("API Work")); 
app.get("/emailbackend", (req, res) => {
  var data = {
    "email": "harit.s@mail.kmutt.ac.th",
    "img": ["img01","img02","img03","img04"]
}

request(res.send(data)

)

}); 
// app.post("/user", (req,res) => {
//     console.log(req.body.email);
//     res.send('haha');
//     });
    
app.listen(port, () => console.log(`Example app listening on port ${port}!`));  
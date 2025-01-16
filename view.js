const myhttp = require("http")
const myExpression = require("express")

const app = myExpression()

app.listen(5000, () => console.log("my node code runs on 5k"))
app.get("/", (req, res) => {
res.send("<h1>Today is a beautiful day.<br/> Go with the flow.</h1>")
})
app.get("/books",(req, res) => {
    res.send("<h1>List of books are available.</h1>")
})
app.get("/tasks",(req, res) => {
    res.sendFile(__dirname + "\\index.html")
})

// myhttp.createServer(function(request, respond) {
//     // console.log(request)
//     if(request.url == "/"){
//         respond.write("<h1>Today is a beautiful day.<br/> Go with the glow.</h1>")
//     }
//     else if (request.url == "/books") {
//         respond.write("<h1>List of books are available.</h1>")
//     }
// }).listen(5000)
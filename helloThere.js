const Ejes = require("ejs")
const Express = require("express")
const MongooDb = require("mongodb")

const app = Express()

app.use(Express.urlencoded())
app.set("view engine", Ejes)


async function makeCollection() {
    const connection = await MongooDb.MongoClient.connect("mongodb://localhost:27017")
    const databases = connection.db("persondatabase")
    return databases
}

app.get("/", async function(req, res) {
    res.send("<h1>Welcome to Person Data Base</h1><a href='/add'>Add People</a><br/><br/><a href='/show'>Show List</a>")
})

app.get("/add", function (req,res) {
    res.render("addPerson.ejs")
})
//  viewPerson.ejs

app.get("/food/display", async function (req,res) {
    //const output = await deb.collection("personcollection").findOne({foodcost: "55"})
    //console.log(output)
    res.send("Successfully read data")

    const deb = await makeCollection()
    // const output = await deb.collection("foodscollection").findOne({foodname: "Veg Pizza"})
    const output = await deb.collection("foodscollection").findOne({foodcost: "55"})
    console.log(output)
    // res.send("Successfully read data")
    res.render("viewFoods.ejs", {foodData : output})

})

app.post("/collections", async function (req,res) {
    console.log(req.body)

    const enteredName = req.body.foodname
    const enteredCost = req.body.foodcost
    const deb = await makeCollection()
    deb.collection("foodscollection").insertOne({foodname: enteredName, foodcost: enteredCost})
    // deb.collection("foodscollection").insertMany([{foodname: "Veg Burger", foodcost: "200"}, {foodname: "Chole Bature", foodcost: "85"}])
    // res.redirect("/")
    res.send("<h2>Food data successfully being inserted</h2>")

})

app.put("/food/updates", async function(req, res) {
       const deb = await makeCollection()

await deb.collection("foodscollection").updateOne(
        { foodname: "Chickoo shakes", foodcost: "65" }, 
        { $set: { foodname: "Chocolate Milkshake", foodcost: "70" }}
    );
    res.send("Updated Successfully");

});

app.delete("/food/delete", async function(req, res) {
          const deb = await makeCollection()

await deb.collection("foodscollection").deleteOne({foodcost: "105"})
    res.send("Deleted Successfully")

})

app.listen(5000, () => console.log("This server shall run on port 5k"))


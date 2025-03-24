const self = require("fs")

self.writeFile("hey.txt", "Hello World!.", function (error) {
    if (error) {
        console.log("Couldnt do so!. SORRY")
    }
    else{
        console.log("Congrats, Data got printed!.")
    }
})
console.log("Happy birthday Mother Earth")
// initially file was not created, but got created after running the above code. TYSM Node js.
// the above one is asynchronous, Now we will see the synchronous ones.
const doin = self.writeFileSync("hey.txt", "Hey, hello World!. Hola Amigos.")
console.log(doin)

// asynchronous readings
self.readFile("hey.txt", "utf-8", function (error, output) {
    if (error) {
        console.log("Couldnt do so!. SORRY")
    }
    else{
        console.log(output)
    }
})
console.log("Happiest Biirthdayyy!!.... Mother Earth")

// synchronous readings
const doin = self.readFileSync("hey.txt", "utf-8")
console.log(doin)
console.log("Hey, Good afternoon!.")
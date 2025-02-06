const fs = require("fs")

fs.appendFile("Notes.txt", "\n\nWhen a function is defined inside a class then it is called Method.\n The method is accessible to data that is contained within the class.\n" , function(err) {
    if (err) {
        throw err
    } else {
        console.log("Its Successfully done")
    }
})

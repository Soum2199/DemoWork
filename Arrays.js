//some rare JS practice

let arr = [3,2,6,4, 1,5];
console.log(arr)
arr.sort()
console.log(arr)
arr.shift()
console.log(arr)
arr.unshift(7)
console.log(arr)
arr.push(8)
console.log(arr)
console.log("---------------------------------")
let myArr = [10, 20.0, "Hey", true, new Date()]
console.log(myArr)

nameArr = ["Khushi", "Raha", "Himali", "Saba", "Emily", "Kaya", "Abhi"];
console.log(nameArr);
console.log(nameArr.length)
console.log(nameArr[0])
nameArr.push("Doonuts");
console.log(nameArr)

console.log("using map method")
nameArr.map((s) => console.log(s))
console.log("\nUsing for each loop")
nameArr.forEach((w) => console.log(w))
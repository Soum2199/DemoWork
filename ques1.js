let arr1 = [1,2,3,4]
let arr2 = [6,7,8,9]

arr2.reverse()
console.log(arr2)
console.log("--===------===--===-------===--")

const user = []

for(let i=0; i<arr2.length; i++){
    user.push([arr2[i], arr1[i]])
}
console.log(user)
console.log(user.flat(4))
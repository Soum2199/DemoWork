// wap to reverse the array using javascript
let arr = [1,2,4,8]
let n = arr.length;
console.log(n)

for (let i=0; i<n/2; i++){
    let temp = arr[n-i-1];
    arr[n-i-1] = arr[i];
    arr[i] = temp;
}
// return temp;
console.log(arr)

let a = [1, 2, 3, 4, 5];


// let start = 0;
// let end = a.length-1;
// let temp = a[start];
// a[start] = a[end];
// a[end] = temp;

// console.log(a)
// o/p: [ 5, 2, 3, 4, 1 ]

// let start = 0;
// let end = a.length-1;
// let temp = a[start++];
// a[start++] = a[end--];
// a[end--] = temp;

// console.log(a)
// [ 1, 5, 3, 1, 5 ]

// let start = 0;
// let end = a.length-1;
// let temp = a[start]++;
// a[start]++ = a[end]--;
// a[end]-- = temp;

// console.log(a)  //error
// console.log(temp)


// let start = 0;
// let end = a.length-1;
// let temp = a[start++];
// a[start++] = a[end++];
// a[end++] = temp;

// console.log(a)  //error
// [ 1, 5, 3, 4, 5, 1 ]


// let start = 0;
// let end = a.length-1;
// let temp = a[start++];
// a[start++] = a[end--];
// a[end--] = temp;

// console.log(a)  //error
// [ 1, 5, 3, 1, 5 ]

// let start = 0;
// let end = a.length-1;
// let temp = a[start--];
// a[start--] = a[end++];
// a[end++] = temp;

// console.log(a)  //error
//  [ 1, 2, 3, 4, 5, 1, '-1': 5 ]

// let start = 0;
// let end = a.length-1;
// let temp = a[start];
// a[start++] = a[end];
// a[end++] = temp;

// console.log(a)  //error
//  [ 5, 2, 3, 4, 1 ]

let n = a.length
let temp = 0
// for(let i=0; i< n; i++){
for(let i=0; i< n/2; i++){
    temp = a[i]
    a[i] = a[n-i-1]
    a[n-i-1] = temp
}
console.log(a)

// Time complexity: O(n)
// Space complexity: O(1)

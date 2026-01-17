// let ra = ["good", "morning", "guys", "how", "are", "udoin"];
let ra = [1,2,4,8, 16, 32]
let n = ra.length-1
for (let i=0; i<n/2; i++){
    let temp = ra[n-i]
    ra[n-i] = ra[i]
    ra[i] = temp;
}

console.log(ra);
// output:  [ 32, 16, 8, 4, 2, 1 ]  not  [ 32, 2, 4, 8, 16, 1 ]

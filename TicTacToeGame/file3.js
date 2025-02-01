// const myBox = document.querySelectorAll(".box")
// const result = document.querySelector("#results")
// const resetBtn = document.querySelector("#reset")
// const msg = document.querySelector("#message")
// const h1 = document.querySelector("h1")
// let isWinner = false;
// let currPlay = "X"

// msg.textContent = `turn for ${currPlay}`
// myBox.forEach(function (i) {
//     i.addEventListener("click", function (params) {
//         console.log(params)
//         console.log(params.target.id)
//         // console.log(params.target.innerText)
//         // console.log(params.target.innerHTML)
//         console.log(params.target.textContent)
//         const boxId = params.target.id;
//         i.innerText = currPlay;
//         arr[boxId] = currPlay;
//         console.log(arr)
//         checkWinner()
//         swapPlayers();
//     })
// })

// function swapPlayers() {
//     if (currPlay == "X") {
//         currPlay = "O"
//     } else {
//         currPlay = "X"
//     }
//     // msg.textContent = `turn for ${currPlay}`
//     if (isWinner == false) {
//         msg.textContent = `turn for ${currPlay}`
//     }
//     else{
//         // msg.textContent = ""
//         msg.hidden = true
//     }
// }

// const arr = Array(9).fill(null);
// console.log(arr)

// function checkWinner() {
//     if ((arr[0] == arr[1] && arr[1] == arr[2] && arr[0] != null) ||
//     (arr[3] == arr[4] && arr[4] == arr[5] && arr[3] != null) ||
//     (arr[6] == arr[7] && arr[7] == arr[8] && arr[6] != null) || 
//     (arr[0] == arr[3] && arr[3] == arr[6] && arr[0] != null) ||
//     (arr[1] == arr[4] && arr[4] == arr[7] && arr[1] != null) ||
//     (arr[2] == arr[5] && arr[5] == arr[8] && arr[2] != null) ||
//     (arr[0] == arr[4] && arr[4] == arr[8] && arr[0] != null) ||
//     (arr[2] == arr[4] && arr[4] == arr[6] && arr[2] != null) ) {
//         result.innerText = `${currPlay} is the Winner!.`;
//         console.log("the winner is : " + currPlay)
//         msg.hidden = true;
//         h1.hidden = true;
//         isWinner = true
        
//     }
//     else{
//         // result.textContent = "It is a Draw"
//         isWinner = false;
//         const output = arr.every(function(i)
//         {
//             if(i != null)  
//             {
//                 console.log(i)
//                 return i
//             }      
//         })
//         if(output == true)
//         {
//             // myH3.textContent = "Game is Drawn!"
//             result.textContent = "It is a Draw"
//             msg.hidden = true;
//             h1.hidden = true;
//         }
//     }
// }

// resetBtn.addEventListener("click", function () {
  
//     currPlay = "X"
//     msg.textContent = `turn for ${currPlay}`
//     arr.fill(null);
//     console.log(arr)
//     msg.hidden = false;
//     h1.hidden = false;
//     isWinner = false
//     // result.hidden = true
//     result.textContent = ""
//     myBox.forEach(function (i) {
//         i.textContent = ""
//     })
// })

const myBox = document.querySelectorAll(".box");
const result = document.querySelector("#results");
const resetBtn = document.querySelector("#reset");
const msg = document.querySelector("#message");
const h1 = document.querySelector("h1");
let isWinner = false;
let currPlay = "X";

msg.textContent = `turn for ${currPlay}`;
myBox.forEach(function (i) {
    i.addEventListener("click", function (params) {
        if (isWinner || i.innerText !== "") return; // Prevent further clicks if there's a winner or box is already filled

        const boxId = params.target.id;
        i.innerText = currPlay;
        arr[boxId] = currPlay;
        checkWinner();
        swapPlayers();
    });
});

function swapPlayers() {
    if (!isWinner) {
        currPlay = (currPlay === "X" ? "O" : "X");
        msg.textContent = `turn for ${currPlay}`;
    } else {
        msg.hidden = true;
    }
}

const arr = Array(9).fill(null);

function checkWinner() {
    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for (const combination of winningCombinations) {
        const [a, b, c] = combination;
        if (arr[a] === arr[b] && arr[b] === arr[c] && arr[a] != null) {
            result.innerText = `${currPlay} is the Winner!`;
            highlightWinningBoxes(combination);
            msg.hidden = true;
            h1.hidden = true;
            isWinner = true;
            return;
        }
    }

    if (arr.every(i => i != null)) {
        result.textContent = "It is a Draw";
        msg.hidden = true;
        h1.hidden = true;
    }
}

function highlightWinningBoxes(combination) {
    combination.forEach(index => {
        console.log(myBox[index])
        myBox[index].style.backgroundColor = "#6495ed"; // Change to your desired highlight color
    });
    console.log("----------------")
}
// console.log("----------------")

resetBtn.addEventListener("click", function () {
    currPlay = "X";
    msg.textContent = `turn for ${currPlay}`;
    arr.fill(null);
    msg.hidden = false;
    h1.hidden = false;
    isWinner = false;
    result.textContent = "";
    myBox.forEach(function (i) {
        i.textContent = "";
        i.style.backgroundColor = ""; // Reset background color
    });
});

//  https://youtu.be/vpRkAoCqX30?si=YB2op4aY-t9EpwMD
//params.target.id, innerText, innerHTML
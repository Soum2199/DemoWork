
const h6 = document.querySelector("h6")
h6.addEventListener("click", function () {
  document.body.classList.toggle("darky")
  h6.classList.toggle("darky")
})

const turns = document.getElementById('turns')
const box = document.querySelectorAll(".box")
let currentPlayer = "X";
// const h3 = document.querySelector("h3")
const status = document.getElementById("status")
const reseti = document.getElementById('reseti')

let arr = Array(9).fill(null)
let winnerStatus = false

// status
turns.innerHTML = `${currentPlayer}s turn`

box.forEach(function(i){
      i.addEventListener("click", function (event) {
      console.log("hi"); console.log(event);
      console.log(event.target.id);
      console.log(event.srcElement.id);
      const numb = Number(event.srcElement.id)
      console.log(numb)
  //     i.innerText = currentPlayer;
  //     TicTacsCheckWin()
  // if(!winnerStatus)  {swapPlayers()}  
  
  if (!arr[numb] && !winnerStatus) {
  i.innerText = currentPlayer;
  arr[numb] = currentPlayer; // <<< THIS IS MISSING
  TicTacsCheckWin();
  // swapPlayers();
}
  swapPlayers();
    })
    // swapPlayers()
})


function TicTacsCheckWin() {
    
    let airy  =  (arr[0] != null && arr[0] == arr[1] && arr[1] == arr[2]) || 
    (arr[3] != null && arr[3] == arr[4] && arr[4] == arr[5]) || 
    (arr[6] != null && arr[6] == arr[7] && arr[7] == arr[8]) ||
    (arr[0] != null && arr[0] == arr[3] && arr[3] == arr[6]) ||
    (arr[1] != null && arr[1] == arr[4] && arr[4] == arr[7]) ||
    (arr[2] != null && arr[2] == arr[5] && arr[5] == arr[8]) ||
    (arr[0] != null && arr[0] == arr[4] && arr[4] == arr[8]) ||
    (arr[2] != null && arr[2] == arr[4] && arr[4] == arr[6]);
    console.log(airy)
    if (airy === true) {
      ///a winner status
      turns.innerHTML = ""
      winnerStatus = true
      status.innerHTML = `${currentPlayer} is a winner`;
    }
    else{
      // check for tie
      winnerStatus = false
      const res = arr.every(function(i){
        if(i != null){
          return i;
        }
      })
      if (res == true) {
        status.innerText = "Game is a draw";
        turns.innerHTML = ""
      }
    }
}

function swapPlayers(){
  currentPlayer = currentPlayer === "X" ? "O" : "X";
  // turns.innerHTML = `${currentPlayer}s turn`;
  if (winnerStatus == false) {
    turns.innerHTML = `${currentPlayer}s turn`;
  }
}


reseti.addEventListener("click", function () {
  
  currentPlayer = "X"
  turns.innerHTML = `${currentPlayer}'s turn`
  status.innerHTML = ''
      box.forEach(function(i)
    {
        i.textContent = ""
    })
  arr.fill(null);
  winnerStatus = false;

})

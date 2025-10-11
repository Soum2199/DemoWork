function showTime() {
const tam = document.getElementById('currentTime')
tam.innerHTML = new Date().toString();
}

//toUTCString for displaying GMT times

showTime();

setInterval(function () {
 showTime();
}, 1000);
// const sel = document.getElementById("sel")
const iconic = document.getElementById("iconic")
iconic.addEventListener("click", function () {
  document.body.classList.toggle("dark")
  iconic.classList.toggle("dark")
})

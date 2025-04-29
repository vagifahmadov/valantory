// timer
function back_page(){
    window.location.href="/"
}
var seconds = 0;
function countdown() {
    seconds = 29;
    function tick() {
      var counter = document.getElementById("countdown");
      seconds--;
      counter.innerHTML ="0:" + (seconds < 10 ? "0" : "") + String(seconds);
      if (seconds > 0) {
        setTimeout(tick, 1000);
        if (seconds < 10){
            counter.classList.add("blink_timeout");
            counter.style.color = '#ce4975';
        }else{
            counter.classList.remove("blink_timeout");
            counter.style.color = '#042B8C';
        }
        // console.log(`time is:`+seconds);
      } else {
        document.getElementById("countdown").innerHTML = "0:00";
        // back_page();
      }
    }
    tick();
  }

countdown();


  
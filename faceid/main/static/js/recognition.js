// timer
function back_page(){
    window.location.href="/"
}

function countdown() {
    var seconds = 29;
    function tick() {
      var counter = document.getElementById("countdown");
      seconds--;
      counter.innerHTML ="0:" + (seconds < 10 ? "0" : "") + String(seconds);
      if (seconds > 0) {
        setTimeout(tick, 1000);
        if (seconds < 10){
            counter.classList.add("blink_timeout");
            counter.style.color = '#ce4975';
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
// swiftalert
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger"
    },
    buttonsStyling: false
  });
  swalWithBootstrapButtons.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Yes, delete it!",
    cancelButtonText: "No, cancel!",
    reverseButtons: true
  }).then((result) => {
    if (result.isConfirmed) {
      swalWithBootstrapButtons.fire({
        title: "Deleted!",
        text: "Your file has been deleted.",
        icon: "success"
      });
    } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
    ) {
      swalWithBootstrapButtons.fire({
        title: "Cancelled",
        text: "Your imaginary file is safe :)",
        icon: "error"
      });
    }
  });
  
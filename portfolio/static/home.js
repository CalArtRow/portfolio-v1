// This code was incorporated from w3schools online 'how to' documentation 
// accessed 03-01-2022 
// https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
// Open and close the sidebar when the hamburger menu is clicked

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}
  
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
// end of referenced code

// Setup the IntersectionObserver to add the "show" class to h2 and .reveal elements when they are scrolled into view

window.addEventListener('DOMContentLoaded', setup); 

function setup() {
    const options = {
        rootMargin: '0px 0px -100px 0px'
    }

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('show');
                observer.unobserve(entry.target);
            } else {
                return; 
            }
        })
    }, options);

    const h2 = document.querySelectorAll('h2');
    h2.forEach(head => observer.observe(head));

    const appear = document.querySelectorAll('.reveal');
    appear.forEach( reveal => observer.observe(reveal));

}

// Validate the contact form before submitting

document.getElementById("contact-form").addEventListener("submit", function(e) {
  e.preventDefault();

  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;

  if (email === "" || message === "") {
    alert("Please fill out all fields!");
  } else {
    //submit the form
    this.submit();
  }
});


// Confirm before deleting

function checkDelete() {
  return confirm('Are you sure you want to Delete?');
}

// This code was adapted from Bootstraps Online Modal Documentation 
// accessed 18-01-2022 
// https://getbootstrap.com/docs/4.1/components/modal/ 

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

$('#closemodal').click(function() {
  $('#modalwindow').modal('hide');
});

// end of referenced code


function showModal(expId, role){
  var description = document.getElementById("expId" + expId).value;
  var role = document.getElementById("expRole" + expId).value;
  var modalBody = document.getElementById("modal-body");
  modalBody.innerHTML = description;
  document.querySelector("#exampleModalCenter .modal-title").innerHTML = role;
}

hiddenInput = document.getElementById("hiddenInput").value
if (hiddenInput != "empty") {
    document.getElementById("dateinput").value = hiddenInput
}

function pasarDia(day = "Fecha") {
    document.getElementById("dateinput").value = day;
    document.getElementById("hiddenInput").value = day;
    modalDays.style.display = "none";
    $('#disponibilidad').submit();
}

function pasarHora(hour = "00:00") {
    document.getElementById("timeinput").value = hour;
    modalHours.style.display = "none";
    //$('#disponibilidad').submit()
}


//************************modal 1 +++++++++++++++++++++++++++++++++ */
// Get the modal
var modalDays = document.getElementById("modalDays");

// Get the button that opens the modal
var inputDays = document.getElementById("input1");

// Get the <span> element that closes the modal
var spanDays = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
inputDays.onclick = function() {
    modalDays.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
spanDays.onclick = function() {
    modalDays.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modalDays) {
        modalDays.style.display = "none";
    }
}

//************************modal 2 +++++++++++++++++++++++++++++++++ */
var modalHours = document.getElementById("modalHours");

// Get the button that opens the modal
var inputHours = document.getElementById("input2");

// Get the <span> element that closes the modal
var spanHours = document.getElementsByClassName("close")[1];

// When the user clicks the button, open the modal 
inputHours.onclick = function() {
    modalHours.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
spanHours.onclick = function() {
    modalHours.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modalHours) {
        modalHours.style.display = "none";
    }
}
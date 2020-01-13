var close_btn = document.getElementById('close');
var book_btn = document.getElementById('btn');
var slot1 = document.getElementById('slot1');
var slot2 = document.getElementById('slot2');
var minus = document.getElementById('minus');
var form = document.getElementsByTagName('form')[0];
var ticketvalue = document.getElementById('ticketvalue');
var plus = document.getElementById('plus');
var price = document.getElementById('price');
var slot1_value = document.getElementById('slot1value');
var slot2_value = document.getElementById('slot2value');
var overlay = document.getElementsByClassName('overlay')[0];

var selected = 0;
var ticketno = 0;

var slot = document.getElementById('slot');
var tickets = document.getElementById('tickets');

book_btn.onclick = function () {
    overlay.style.display = "block";
}

close_btn.onclick = function () {
    overlay.style.display = "none";
}

slot1.onclick = function () {
    if (selected != 0) {
        selected.style.display = "none";
        slot2.classList.remove('selected');
    }
    form.style.display = "block";
    slot1.classList.add('selected');
    selected = slot1_value;
    slot.value = 1;
    slot1_value.style.display = "block";
}

slot2.onclick = function () {
    if (selected != 0) {
        selected.style.display = "none";
        slot1.classList.remove('selected');
    }
    form.style.display = "block";
    slot2.classList.add('selected');
    selected = slot2_value;
    slot.value = 2;
    slot2_value.style.display = "block";
}

minus.onclick = function () {
    if (ticketno == 0) { }
    else {
        ticketno = ticketno - 1;
        ticketvalue.innerHTML = ticketno;
        tickets.value = ticketno;
        price.innerHTML = ticketno * 100;
    }
}

plus.onclick = function () {
    if (ticketno > 50) { }
    else {
        ticketno = ticketno + 1;
        ticketvalue.innerHTML = ticketno;
        tickets.value = ticketno;
        price.innerHTML = ticketno * 100;
    }
}

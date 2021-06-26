var indx = 0
var slides = document.getElementsByClassName('slide')
var btns = document.getElementsByClassName('slider_btn')
var back = document.getElementById('back')
var forward = document.getElementById('forward')
btns[0].style.color = 'rgba(196, 196, 196, 1)'
slider(indx)

function next() {
    if (indx < slides.length-1) {
        indx++
        btns[0].style.color = 'white'
        let src = back.getAttribute('white');
        back.setAttribute("src", src);
    }
    if (indx == slides.length-1) {
        btns[1].style.color = 'rgba(196, 196, 196, 1)'
        let src = forward.getAttribute('grey');
        forward.setAttribute("src", src);
    }
    slider(indx)
}

function prev() {
    if (indx > 0) {
        indx--
        btns[1].style.color = 'white'
        let src = forward.getAttribute('white');
        forward.setAttribute("src", src);
    }
    if (indx == 0) {
        btns[0].style.color = 'rgba(196, 196, 196, 1)'
        let src = back.getAttribute('grey');
        back.setAttribute("src", src);
    }
    slider(indx)
}

function slider() {
    for(let i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none'
    }
    slides[indx].style.display = 'block'
}
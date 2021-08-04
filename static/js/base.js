// displays active location in navbars
$(document).ready(function () {
    var scriptElement = $('#baseScript')[0];
    var path = scriptElement.getAttribute('data-path');
    $('a[href="'+path+'"]').addClass("active");
});

// update the year of the copyright automatically
document.querySelector('#copyright-year').innerText = new Date().getFullYear();
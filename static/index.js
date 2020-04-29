var width = $("#game").width();
var height = $("#game").height();

var start = $("#object").position();

setInterval(function() {
    var newTop = (Math.random()*height) + start.top;
    var newLeft = (Math.random()*width) + start.left/2;

    $("#object").offset({
        top: newTop,
        left: newLeft
    })
}, 1000);
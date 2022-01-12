//scroll top button
const header = $("#header");
const btnTop = $(".btnTop");
$(window).on("scroll", function () {
    //console.log($(window).scrollTop());
    //console.log($(document).height());
    const st = $(window).scrollTop();
    if (st > 0) {
        header.addClass("scroll");
        btnTop.addClass("on");
    } else {
        header.removeClass("scroll");
        btnTop.removeClass("on");
    }
    //console.log("document===", $(document).hegiht());
});

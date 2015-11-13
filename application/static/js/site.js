/*
 *
 */
var tmpl_win_line = function (data) {
    var win = data.win;
    var num_class = new Array(21);  // use index 1-20
    var tmpl = '<tr>';
    // data seq
    tmpl += '<td class="win-seq">' + data.seq + '</td>';
    // top3 win
    for (var i = 0; i < 3; i++) {
        tmpl += '<td class="col-win-head">' + win[i] + '</td>';
        num_class[win[i]] = 'win-head';
    }
    // last5 win
    for (var i = 3; i < 8; i++) {
        num_class[win[i]] = 'win-tail';
    }
    for (var i = 1; i < 21; i++) {
        if (num_class[i]) {
            tmpl += '<td class="' + num_class[i] + '">' + i + '</td>';
        } else {
            tmpl += '<td></td>';
        }
    }
    tmpl += '</tr>'
    return tmpl;
};


var show_live_win = function (obj) {
    $.getJSON('/api/live-win/34', function (json) {
        json.forEach(function (item) {
            $(obj).append(tmpl_win_line(item));
        });
    });
};


$(document).ready(function () {
    $('.win-table').each(function (idx, ele) {
        show_live_win(ele);
    });
});

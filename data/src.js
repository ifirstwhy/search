
function getQueryString(key) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (pair[0] === key) {
            return decodeURIComponent(pair[1]);
        }
    }
}

function encodeCP949(s) {
    var buf = '';
    for (var i = 0, len = s.length; i < len; i++) {
        buf += charTable[s[i]];
    }
    return buf;
}

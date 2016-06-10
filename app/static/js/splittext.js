/*!
 * VERSION: 0.3.5
 * DATE: 2016-05-24
 * UPDATES AND DOCS AT: http://greensock.com
 *
 * This is a special version that is only to be used on certain sites like codepen.io. It will redirect to a page on GreenSock.com if you try using it on a different domain. Please sign up for Club GreenSock to get the fully-functional version at https://greensock.com/club/
 *
 * @license Copyright (c) 2008-2015, GreenSock. All rights reserved.
 * SplitText is a Club GreenSock membership benefit; You must have a valid membership to use
 * this code without violating the terms of use. Visit http://greensock.com/club/ to sign up or get more details.
 * For licensing details, see http://greensock.com/licensing/
 *
 * @author: Jack Doyle, jack@greensock.com
 */
var _gsScope = "undefined" != typeof module && module.exports && "undefined" != typeof global ? global : this || window;
! function(a) {
    "use strict";
    var b = a.GreenSockGlobals || a,
        c = function(a) {
            var e, c = a.split("."),
                d = b;
            for (e = 0; e < c.length; e++) d[c[e]] = d = d[c[e]] || {};
            return d
        },
        d = c("com.greensock.utils"),
        e = function(a) {
            var b = a.nodeType,
                c = "";
            if (1 === b || 9 === b || 11 === b) {
                if ("string" == typeof a.textContent) return a.textContent;
                for (a = a.firstChild; a; a = a.nextSibling) c += e(a)
            } else if (3 === b || 4 === b) return a.nodeValue;
            return c
        },
        f = document,
        g = f.defaultView ? f.defaultView.getComputedStyle : function() {},
        h = /([A-Z])/g,
        i = "",
        j = "SplitText",
        k = String.fromCharCode(103, 114, 101, 101, 110, 115, 111, 99, 107, 46, 99, 111, 109),
        l = String.fromCharCode(47, 114, 101, 113, 117, 105, 114, 101, 115, 45, 109, 101, 109, 98, 101, 114, 115, 104, 105, 112, 47),
        m = function(b) {
            for (var c = -1 !== (a ? a.location.href : "").indexOf(String.fromCharCode(103, 114, 101, 101, 110, 115, 111, 99, 107)) && -1 !== b.indexOf(String.fromCharCode(108, 111, 99, 97, 108, 104, 111, 115, 116)), d = [k, String.fromCharCode(99, 111, 100, 101, 112, 101, 110, 46, 105, 111), String.fromCharCode(99, 111, 100, 101, 112, 101, 110, 46, 100, 101, 118), String.fromCharCode(99, 115, 115, 45, 116, 114, 105, 99, 107, 115, 46, 99, 111, 109), String.fromCharCode(99, 100, 112, 110, 46, 105, 111), String.fromCharCode(103, 97, 110, 110, 111, 110, 46, 116, 118), String.fromCharCode(99, 111, 100, 101, 99, 97, 110, 121, 111, 110, 46, 110, 101, 116), String.fromCharCode(116, 104, 101, 109, 101, 102, 111, 114, 101, 115, 116, 46, 110, 101, 116), String.fromCharCode(99, 101, 114, 101, 98, 114, 97, 120, 46, 99, 111, 46, 117, 107), String.fromCharCode(116, 121, 109, 112, 97, 110, 117, 115, 46, 110, 101, 116), String.fromCharCode(116, 119, 101, 101, 110, 109, 97, 120, 46, 99, 111, 109), String.fromCharCode(116, 119, 101, 101, 110, 108, 105, 116, 101, 46, 99, 111, 109), String.fromCharCode(112, 108, 110, 107, 114, 46, 99, 111), String.fromCharCode(104, 111, 116, 106, 97, 114, 46, 99, 111, 109), String.fromCharCode(106, 115, 102, 105, 100, 100, 108, 101, 46, 110, 101, 116)], e = d.length; --e > -1;)
                if (-1 !== b.indexOf(d[e])) return !0;
            return c && a && a.console && console.log(String.fromCharCode(87, 65, 82, 78, 73, 78, 71, 58, 32, 97, 32, 115, 112, 101, 99, 105, 97, 108, 32, 118, 101, 114, 115, 105, 111, 110, 32, 111, 102, 32) + j + String.fromCharCode(32, 105, 115, 32, 114, 117, 110, 110, 105, 110, 103, 32, 108, 111, 99, 97, 108, 108, 121, 44, 32, 98, 117, 116, 32, 105, 116, 32, 119, 105, 108, 108, 32, 110, 111, 116, 32, 119, 111, 114, 107, 32, 111, 110, 32, 97, 32, 108, 105, 118, 101, 32, 100, 111, 109, 97, 105, 110, 32, 98, 101, 99, 97, 117, 115, 101, 32, 105, 116, 32, 105, 115, 32, 97, 32, 109, 101, 109, 98, 101, 114, 115, 104, 105, 112, 32, 98, 101, 110, 101, 102, 105, 116, 32, 111, 102, 32, 67, 108, 117, 98, 32, 71, 114, 101, 101, 110, 83, 111, 99, 107, 46, 32, 80, 108, 101, 97, 115, 101, 32, 115, 105, 103, 110, 32, 117, 112, 32, 97, 116, 32, 104, 116, 116, 112, 58, 47, 47, 103, 114, 101, 101, 110, 115, 111, 99, 107, 46, 99, 111, 109, 47, 99, 108, 117, 98, 47, 32, 97, 110, 100, 32, 116, 104, 101, 110, 32, 100, 111, 119, 110, 108, 111, 97, 100, 32, 116, 104, 101, 32, 39, 114, 101, 97, 108, 39, 32, 118, 101, 114, 115, 105, 111, 110, 32, 102, 114, 111, 109, 32, 121, 111, 117, 114, 32, 71, 114, 101, 101, 110, 83, 111, 99, 107, 32, 97, 99, 99, 111, 117, 110, 116, 32, 119, 104, 105, 99, 104, 32, 104, 97, 115, 32, 110, 111, 32, 115, 117, 99, 104, 32, 108, 105, 109, 105, 116, 97, 116, 105, 111, 110, 115, 46, 32, 84, 104, 101, 32, 102, 105, 108, 101, 32, 121, 111, 117, 39, 114, 101, 32, 117, 115, 105, 110, 103, 32, 119, 97, 115, 32, 108, 105, 107, 101, 108, 121, 32, 100, 111, 119, 110, 108, 111, 97, 100, 101, 100, 32, 102, 114, 111, 109, 32, 101, 108, 115, 101, 119, 104, 101, 114, 101, 32, 111, 110, 32, 116, 104, 101, 32, 119, 101, 98, 32, 97, 110, 100, 32, 105, 115, 32, 114, 101, 115, 116, 114, 105, 99, 116, 101, 100, 32, 116, 111, 32, 108, 111, 99, 97, 108, 32, 117, 115, 101, 32, 111, 114, 32, 111, 110, 32, 115, 105, 116, 101, 115, 32, 108, 105, 107, 101, 32, 99, 111, 100, 101, 112, 101, 110, 46, 105, 111, 46)), c
        }(a ? a.location.host : ""),
        n = function(a, b, c, d) {
            var e;
            return (c = c || g(a, null)) ? (a = c.getPropertyValue(b.replace(h, "-$1").toLowerCase()), e = a || c.length ? a : c[b]) : a.currentStyle && (c = a.currentStyle, e = c[b]), d ? e : parseInt(e, 10) || 0
        },
        o = function(a) {
            return a.length && a[0] && (a[0].nodeType && a[0].style && !a.nodeType || a[0].length && a[0][0]) ? !0 : !1
        },
        p = function(a) {
            var d, e, f, b = [],
                c = a.length;
            for (d = 0; c > d; d++)
                if (e = a[d], o(e))
                    for (f = e.length, f = 0; f < e.length; f++) b.push(e[f]);
                else b.push(e);
            return b
        },
        q = /(?:\r|\n|\s\s|\t\t)/g,
        r = ")eefec303079ad17405c",
        s = /(?:<br>|<br\/>|<br \/>)/gi,
        t = f.all && !f.addEventListener,
        u = "<div style='position:relative;display:inline-block;" + (t ? "*display:inline;*zoom:1;'" : "'"),
        v = function(a) {
            a = a || "";
            var b = -1 !== a.indexOf("++"),
                c = 1;
            return b && (a = a.split("++").join("")),
                function() {
                    return u + (a ? " class='" + a + (b ? c++ : "") + "'>" : ">")
                }
        },
        w = d.SplitText = b.SplitText = function(b, c) {
            if ("string" == typeof b && (b = w.selector(b)), !b) throw "cannot split a null element.";
            return (this.elements = o(b) ? p(b) : [b], this.chars = [], this.words = [], this.lines = [], this._originals = [], this.vars = c || {}, void this.split(c))
        },
        x = function(a, b, c) {
            var d = a.nodeType;
            if (1 === d || 9 === d || 11 === d)
                for (a = a.firstChild; a; a = a.nextSibling) x(a, b, c);
            else(3 === d || 4 === d) && (a.nodeValue = a.nodeValue.split(b).join(c))
        },
        y = function(a, b) {
            for (var c = b.length; --c > -1;) a.push(b[c])
        },
        z = function(a, b, c, d, h) {
            s.test(a.innerHTML) && (a.innerHTML = a.innerHTML.replace(s, r));
            var Q, R, S, T, U, V, W, X, Y, Z, $, _, aa, ba, i = e(a),
                j = b.type || b.split || "chars,words,lines",
                k = -1 !== j.indexOf("lines") ? [] : null,
                l = -1 !== j.indexOf("words"),
                m = -1 !== j.indexOf("chars"),
                o = "absolute" === b.position || b.absolute === !0,
                p = o ? "&#173; " : " ",
                t = -999,
                u = g(a),
                w = n(a, "paddingLeft", u),
                z = n(a, "borderBottomWidth", u) + n(a, "borderTopWidth", u),
                A = n(a, "borderLeftWidth", u) + n(a, "borderRightWidth", u),
                B = n(a, "paddingTop", u) + n(a, "paddingBottom", u),
                C = n(a, "paddingLeft", u) + n(a, "paddingRight", u),
                D = n(a, "textAlign", u, !0),
                E = a.clientHeight,
                F = a.clientWidth,
                G = "</div>",
                H = v(b.wordsClass),
                I = v(b.charsClass),
                J = -1 !== (b.linesClass || "").indexOf("++"),
                K = b.linesClass,
                L = -1 !== i.indexOf("<"),
                M = !0,
                N = [],
                O = [],
                P = [];
            for (!b.reduceWhiteSpace != !1 && (i = i.replace(q, "")), J && (K = K.split("++").join("")), L && (i = i.split("<").join("{{LT}}")), Q = i.length, T = H(), U = 0; Q > U; U++)
                if (W = i.charAt(U), ")" === W && i.substr(U, 20) === r) T += (M ? G : "") + "<BR/>", M = !1, U !== Q - 20 && i.substr(U + 20, 20) !== r && (T += " " + H(), M = !0), U += 19;
                else if (" " === W && " " !== i.charAt(U - 1) && U !== Q - 1 && i.substr(U - 20, 20) !== r) {
                for (T += M ? G : "", M = !1;
                    " " === i.charAt(U + 1);) T += p, U++;
                (")" !== i.charAt(U + 1) || i.substr(U + 1, 20) !== r) && (T += p + H(), M = !0)
            } else "{" === W && "{{LT}}" === i.substr(U, 6) ? (T += m ? I() + "{{LT}}</div>" : "{{LT}}", U += 5) : T += m && " " !== W ? I() + W + "</div>" : W;
            for (a.innerHTML = T + (M ? G : ""), L && x(a, "{{LT}}", "<"), V = a.getElementsByTagName("*"), Q = V.length, X = [], U = 0; Q > U; U++) X[U] = V[U];
            if (k || o)
                for (U = 0; Q > U; U++) Y = X[U], S = Y.parentNode === a, (S || o || m && !l) && (Z = Y.offsetTop, k && S && Z !== t && "BR" !== Y.nodeName && (R = [], k.push(R), t = Z), o && (Y._x = Y.offsetLeft, Y._y = Z, Y._w = Y.offsetWidth, Y._h = Y.offsetHeight), k && (l !== S && m || (R.push(Y), Y._x -= w), S && U && (X[U - 1]._wordEnd = !0), "BR" === Y.nodeName && Y.nextSibling && "BR" === Y.nextSibling.nodeName && k.push([])));
            for (U = 0; Q > U; U++) Y = X[U], S = Y.parentNode === a, "BR" !== Y.nodeName ? (o && (_ = Y.style, l || S || (Y._x += Y.parentNode._x, Y._y += Y.parentNode._y), _.left = Y._x + "px", _.top = Y._y + "px", _.position = "absolute", _.display = "block", _.width = Y._w + 1 + "px", _.height = Y._h + "px"), l ? S && "" !== Y.innerHTML ? O.push(Y) : m && N.push(Y) : S ? (a.removeChild(Y), X.splice(U--, 1), Q--) : !S && m && (Z = !k && !o && Y.nextSibling, a.appendChild(Y), Z || a.appendChild(f.createTextNode(" ")), N.push(Y))) : k || o ? (a.removeChild(Y), X.splice(U--, 1), Q--) : l || a.appendChild(Y);
            if (k) {
                for (o && ($ = f.createElement("div"), a.appendChild($), aa = $.offsetWidth + "px", Z = $.offsetParent === a ? 0 : a.offsetLeft, a.removeChild($)), _ = a.style.cssText, a.style.cssText = "display:none;"; a.firstChild;) a.removeChild(a.firstChild);
                for (ba = !o || !l && !m, U = 0; U < k.length; U++) {
                    for (R = k[U], $ = f.createElement("div"), $.style.cssText = "display:block;text-align:" + D + ";position:" + (o ? "absolute;" : "relative;"), K && ($.className = K + (J ? U + 1 : "")), P.push($), Q = R.length, V = 0; Q > V; V++) "BR" !== R[V].nodeName && (Y = R[V], $.appendChild(Y), ba && (Y._wordEnd || l) && $.appendChild(f.createTextNode(" ")), o && (0 === V && ($.style.top = Y._y + "px", $.style.left = w + Z + "px"), Y.style.top = "0px", Z && (Y.style.left = Y._x - Z + "px")));
                    0 === Q && ($.innerHTML = "&nbsp;"), l || m || ($.innerHTML = e($).split(String.fromCharCode(160)).join(" ")), o && ($.style.width = aa, $.style.height = Y._h + "px"), a.appendChild($)
                }
                a.style.cssText = _
            }
            o && (E > a.clientHeight && (a.style.height = E - B + "px", a.clientHeight < E && (a.style.height = E + z + "px")), F > a.clientWidth && (a.style.width = F - C + "px", a.clientWidth < F && (a.style.width = F + A + "px"))), y(c, N), y(d, O), y(h, P)
        },
        A = w.prototype;
    A.split = function(a) {
        this.isSplit && this.revert(), this.vars = a || this.vars, this._originals.length = this.chars.length = this.words.length = this.lines.length = 0;
        for (var b = this.elements.length; --b > -1;) this._originals[b] = this.elements[b].innerHTML, z(this.elements[b], this.vars, this.chars, this.words, this.lines);
        return this.chars.reverse(), this.words.reverse(), this.lines.reverse(), this.isSplit = !0, this
    }, A.revert = function() {
        if (!this._originals) throw "revert() call wasn't scoped properly.";
        for (var a = this._originals.length; --a > -1;) this.elements[a].innerHTML = this._originals[a];
        return this.chars = [], this.words = [], this.lines = [], this.isSplit = !1, this
    }, w.selector = a.$ || a.jQuery || function(b) {
        var c = a.$ || a.jQuery;
        return c ? (w.selector = c, c(b)) : "undefined" == typeof document ? b : document.querySelectorAll ? document.querySelectorAll(b) : document.getElementById("#" === b.charAt(0) ? b.substr(1) : b)
    }, w.version = "0.3.5"
}(_gsScope),
function(a) {
    "use strict";
    var b = function() {
        return (_gsScope.GreenSockGlobals || _gsScope)[a]
    };
    "function" == typeof define && define.amd ? define([], b) : "undefined" != typeof module && module.exports && (module.exports = b())
}("SplitText");
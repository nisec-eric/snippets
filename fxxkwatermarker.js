// ==UserScript==
// @name         fxxk watermarker
// @namespace    http://tubb/
// @version      0.1
// @description  try to take over the world!
// @author       just a small bunny!
// @run-at       document-body
// @match        http*://club-dev.group.cpic.com/*
// @match        http*://club-dev.cpic.com.cn/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    document.body.addEventListener('beforescriptexecute',function(e){
        if(e.target.innerText.indexOf('watermark')!=-1){
            e.stopPropagation();
            e.preventDefault();
            console.log(e.target);
            console.log('fxxk watermark')
            //todo
        }
    })
})();

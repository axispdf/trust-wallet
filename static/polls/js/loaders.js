!function(){function e(){return{width:window.innerWidth*window.devicePixelRatio,height:window.innerHeight*window.devicePixelRatio}}function t(t){var n=e();t.width=n.width,t.height=n.height}function n(e){return e[Math.floor(Math.random()*e.length)]}function i(e){var t=e.split("."),n=t[0],i=t[1]-1,a=t[2].replace("****",(new Date).getFullYear());return new Date(a,i,n,0,0,0)}var a={morning:{interval:[7,11],title:"Доброе утро!",postfix:"morning"},day:{interval:[12,17],title:"Добрый день!",postfix:"day"},evening:{interval:[18,22],title:"Добрый вечер!",postfix:"evening"}},o={birthday:"С Днём Рождения!","new-year":"С Новым годом!",none:""},r=200;window.getLoader=function(s,l,d,c){var p=Object.keys(s),u=null,v=function(){var e=new Date;return e.setHours(0),e.setMinutes(0),e.setSeconds(0),e.setMilliseconds(0),e}().getTime(),f=[],g=[],w=[],h=document.querySelector(".scaffold__entry"),m=function(){var e=(new Date).getHours(),t="Доброй ночи!",n="night";return Object.keys(a).forEach(function(i){var o=a[i].interval,r=a[i].title,s=a[i].postfix,l=o[0],d=o[1];e>=l&&e<=d&&(t=r,n=s)}),{greeting:t,dayTime:n}}(),y=m.greeting,x=m.dayTime;p.forEach(function(e){var t=s[e],n=t.options;if(n)var a=n.start,o=n.end,r=n.birthDay;if(a&&o){var l=i(a).getTime(),d=i(o).getTime();v>=l&&v<=d&&g.push(t)}else r?f.push(t):w.push(t)});var M,T,S=d&&i(d).getTime()===v&&f.length,b=(u=S?s[n(f).value]:g.length?s[n(g).value]:s[n(w).value]).value,L=u.options[x],R=(c||l)+"/loaders/"+(L?b+"-"+L:b)+".json",z=new XMLHttpRequest;if(z.open("GET",R,!1),z.send(),u&&z.status===r){var A=document.createElement("canvas");t(A),h.appendChild(A);var C=A.getContext("2d"),D=lottie.loadAnimation({renderer:"canvas",loop:!1,autoplay:!1,animationData:JSON.parse(z.responseText),rendererSettings:{context:C,preserveAspectRatio:"xMidYMax slice"}});if(window.OffscreenCanvas){var E=document.createElement("canvas");t(E),E.style.position="absolute",E.style.top="0",E.style.left="0",h.appendChild(E);var O=(M=new URL(l+"/js/lottie.js",window.location).href,T="importScripts('"+M+"');",URL.createObjectURL(new Blob([T]))),j=new Worker(O),H=E.transferControlToOffscreen();j.postMessage({canvas:H,animationData:JSON.parse(z.responseText),drawSize:e(),params:{loop:!1,autoplay:!0,rendererSettings:{preserveAspectRatio:"xMidYMax slice"}}},[H]),lottie.resizeAnimation=function(){j.postMessage({drawSize:e()})}}else lottie.resizeAnimation=function(){t(A),lottie.resize()},D.goToAndStop(D.totalFrames,!0);window.addEventListener("resize",lottie.resizeAnimation);var k=u.options&&u.options.greeting,U=document.createElement("p");U.textContent=k?o[k]:y,U.classList.add("greet"),S&&U.classList.add("birthday"),h.appendChild(U)}}}();
// yomi

let output = "";
$(".font-color01").each(function (i, e) {
  if (!!e.innerText) {
    output += e.innerText += "\n";
  }
});
copy(output);

// yoji jukugo
let output = "";
$("[value=正解表示→]").each(function (i, e) {
  $(e).click();
});
$(".yoji5-answer01").each(function (i, e) {
  if (!!e.innerText) {
    output += e.innerText += "\n";
  }
});
copy(output);

currentLoc = window.location.href.split(
  "https://kanken.jitenon.jp/mondai5/yoji"
);
nextPage = parseInt(currentLoc[1].substring(0, 2));
nextPage += 1;

if (nextPage < 10) {
  nextPage = `0${nextPage}`;
}

window.location = `https://kanken.jitenon.jp/mondai5/yoji${nextPage}.html`;

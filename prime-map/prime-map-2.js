var theMaxN = 2;
var thePrimes = [2];
var theCurrentN = 0;
var theCurrentPrimes = [];
var theSelectedPrimes = [];

updateDisplay = function() {
  adjustPrimes();
  showPrimeMap();
  adjustPrimeDisplay();
}      

primesBelowN = function(N) {
  if (N < 2) return [];
  if (N > theMaxN) {
    for (var val = theMaxN+1; val <= N; val++) {
      var isPrime = true;
      thePrimes.every((p) =>{
        if (val%p == 0) {isPrime = false;}
        return isPrime;
      });
      if (isPrime) thePrimes.push(val);
    }
  }
  return thePrimes.filter(p => p <= N);
}

adjustPrimes = function(){
  var maxCurrentPrime = Math.max(...theCurrentPrimes)||0;
  theCurrentN = parseInt($("#base").val(),10);
  theCurrentPrimes = primesBelowN(theCurrentN)
  $("#multiplier").attr("max", theCurrentN+1);
  $(theSelectedPrimes).filter(!theCurrentPrimes.includes($(this))).remove();
  $(".prime-selector").filter(function(idx, it){return !theCurrentPrimes.includes(parseInt(it.value,10))}).remove();
  $("button.prime-selector").filter(function(idx,it){return !theCurrentPrimes.includes(parseInt(it.value,10))}).remove();
  theCurrentPrimes.forEach((p)=>{
    if (p > maxCurrentPrime) {
      $("#primeSelectors").append(`<input type="button" class="prime-selector" value="${p}" onclick="togglePrimeSelection(this.value);$('#multiplier').focus();"/>`);
    }
  });
}

togglePrimeSelection = function(p) {
  var idx = theSelectedPrimes.indexOf(p);
  if (idx > -1) {
    theSelectedPrimes.splice(idx, 1);
  } else {
    theSelectedPrimes.push(p);
  }
  adjustPrimeDisplay();
}

adjustPrimeDisplay = function() {
  $(".prime-selector").filter(function(idx, it){
      return (theSelectedPrimes.includes(it.value) || theSelectedPrimes.includes(parseInt(it.value, 10)))
  }).addClass("prime-selected");
  $(".prime-selector").filter(function(idx, it){
      return !(theSelectedPrimes.includes(it.value) || theSelectedPrimes.includes(parseInt(it.value, 10)))
  }).removeClass("prime-selected");
  theCurrentPrimes
  $("text.prime-selector").filter(function(idx, it){
      return (theSelectedPrimes.includes($(it).attr("value")) || theSelectedPrimes.includes(parseInt($(it).attr("value"), 10)));
  }).addClass("prime-selected");
  $("text.prime-selector").filter(function(idx, it){
      return !(theSelectedPrimes.includes($(it).attr("value")) || theSelectedPrimes.includes(parseInt($(it).attr("value"), 10)));
  }).removeClass("prime-selected");

  var pi = 1;
  var selectedPrimeClasses = []; 
  theSelectedPrimes.forEach((p)=>{
    pi *= p;
    selectedPrimeClasses.push(".p"+p);
  });
  $("rect.active").attr("data-level", "2");
  if (theSelectedPrimes.length > 0) {
    var colSelector = "g"+selectedPrimeClasses.join("");
    var cellSelector = selectedPrimeClasses.join(",");
    var $qualifingColumns = $(colSelector);
    var expected = Math.floor(theCurrentN/pi);
    var actual = $qualifingColumns.length;

    $qualifingColumns.children(cellSelector).filter(".active").attr("data-level", "4");

    $("#expected").text(expected);
    $("#actual").text(actual);
  } else {
    $("#expected").text("0");
    $("#actual").text("0");
  }
  $("#qualifer").text(actual > expected);
  $("#qualifer").attr("qualifies", actual > expected);
}

showPrimeMap = function(){
  var N = theCurrentN; //parseInt($("#base").val(),10);
  var k = parseInt($("#multiplier").val(),10);
  var primes = theCurrentPrimes; //primesBelowN(N);
  var columns = [];
  var labels = [];
  theCurrentPrimes.forEach((p, pos) => {
    labels.push(
        `<text x="5" y="${10+15*pos}" class="small prime-selector" value=${p} onclick="togglePrimeSelection('${p}');">${p}</text>`
    );
  });
  labels.splice(0, 0, `<g transform="translate(0, 0)">`);
  labels.push("</g>");
  columns.push(labels.join(""));
  
  for (var idx = 0; idx < N; idx++) {
    var val = k*N+1+idx
    var primeDivisors = [];
    var column = [];
    theCurrentPrimes.forEach((p, pos) => {
      if (val%p == 0) {
        primeDivisors.push("p"+p);
      }        
      column.push(
          `<rect width="11" height="11" x="16" y="${15*pos}" class="${val%p==0?"p"+p+" active ":""}ContributionCalendar-day" rx="2" ry="2" data-level="${val%p==0?2:0}"></rect>`
      );
    });
    column.splice(0, 0, `<g transform="translate(${16*(1+idx)}, 0)" class="${primeDivisors.join(" ")}">`);
    column.push("</g>");
    columns.push(column.join(""));        
  }
  var htmlStr = `<svg onclick="togglePrimeSelection(theCurrentPrimes[Math.floor(event.offsetY/15)]);" width="${22*N}" height="${15*theCurrentPrimes.length}" class="js-calendar-graph-svg">` + columns.join("") + "</g></svg>";
  $("#mapContainer").empty().append(htmlStr);
}

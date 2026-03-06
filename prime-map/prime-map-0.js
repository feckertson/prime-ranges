primesBelowN = function(N) {
  if (N < 2) return [];
  var primes = [];
  for (var val = 2; val <= N; val++) {
    var isPrime = true;
    primes.every((p) =>{
      if (val%p == 0) {isPrime = false;}
      return isPrime;
    });
    if (isPrime) primes.push(val);
  }
  return primes;
}

toggleP = function(p){
  var sel = ".p"+p;
  $(`.prime-selector[value=${p}]`).toggleClass("prime-selected"); 
  var selectedPrimes = []; 
  var val = 1;
  $(".prime-selector.prime-selected").each(function(){
    selectedPrimes.push(".p"+$(this).val());
    val*=$(this).val();
  });
  $("rect.active").attr("data-level", "2");
  var colSelector = "g"+selectedPrimes.join("");
  var cellSelector = selectedPrimes.join(",");
  if (selectedPrimes.length > 0) {
    $(colSelector).children(cellSelector).filter(".active").attr("data-level", "4");
  }
  var expected = Math.floor(parseInt($("#base").val(),10)/val);
  var actual = $(colSelector).length;
  $("#expected").text(expected);
  $("#actual").text(actual);
  $("#qualifer").text(actual > expected);
  $("#qualifer").attr("qualifies", actual > expected);
}

listPrimes = function() {
  var N = parseInt($("#base").val(),10);
  $("#multiplier").attr("max", N+1);
  var primes = primesBelowN(N);
  var htmlStr = "<div>";
  primes.forEach((p)=>{
    htmlStr += `<input type="button" class="prime-selector" value="${p}" onclick="toggleP(${p})"/>`;
  });
  htmlStr += "</div>";
  $("#primes").empty().append(htmlStr);
}

showPrimeMap = function(){
  var N = parseInt($("#base").val(),10);
  var k = parseInt($("#multiplier").val(),10);
  var primes = primesBelowN(N);
  var columns = [];

  var labels = [];
  primes.forEach((p, pos) => {
    labels.push(
        `<text x="5" y="${8+15*pos}" class="small">${p}</text>`
    );
  });
  labels.splice(0, 0, `<g transform="translate(0, 0)">`);
  labels.push("</g>");
  columns.push(labels.join(""));
  
  for (var idx = 0; idx < N; idx++) {
    var val = k*N+1+idx
    var primeDivisors = [];
    var column = [];
    primes.forEach((p, pos) => {
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
  var htmlStr = `<svg width="${22*N}" height="${15*primes.length}" class="js-calendar-graph-svg">` + columns.join("") + "</g></svg>";
  $("#mapContainer").empty().append(htmlStr);
}

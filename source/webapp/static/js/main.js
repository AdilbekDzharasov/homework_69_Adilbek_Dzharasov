function successResult(data) {
  const answer = `<span style="color:green">${data.answer}</span>`;
  $('.result').append(answer);
};

function errorResult(data) {
    text = JSON.parse(data.responseText);
    const answer = `<span style="color:red">${text.error}</span>`;
    $('.result').append(answer);
};

function calculator(urlMethod) {
  A = document.getElementById('first_number');
  B = document.getElementById('second_number');
  $.ajax({
    url: urlMethod,
    method: 'post',
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({"A":A.value, "B":B.value}),
    success: successResult,
    error: errorResult
  });
};

function add() {
    calculator ("http://localhost:8000/api/add/")
};

function subtract() {
    calculator ("http://localhost:8000/api/subtract/")
};

function multiply() {
    calculator ("http://localhost:8000/api/multiply/")
};

function divide() {
    calculator ("http://localhost:8000/api/divide/")
};


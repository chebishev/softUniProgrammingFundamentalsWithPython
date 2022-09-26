//function types:
function sum2(a, b) {
    return a + b;
}

let sum = function (a, b) {
    return a + b;
}

//arrow
let sum1 = (a, b) => a + b;
let result = sum(5, 10);
let result1 = sum1(5, 10);
let result2 = sum2(5, 10);
console.log(result);

let result = calculate(sum, 5, 10);


function calculate(operation, firstArgument, secondArgiment) {
    let operationResult = operation(firstArgument, secondArgiment);
    return operationResult;
}

console.log(result);
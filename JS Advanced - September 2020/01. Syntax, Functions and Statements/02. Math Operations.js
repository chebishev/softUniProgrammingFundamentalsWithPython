function mathOperations(firstOperand, secondOperand, operationsSign) {
    let operation = null;
    switch (operationsSign) {
        case '+': operation = (a, b) => a + b;
            break;

        case '-': operation = (a, b) => a - b;
            break;

        case '*': operation = (a, b) => a * b;
            break;

        case '/': operation = (a, b) => a / b;
            break;
        case '**': operation = (a, b) => a ** b;
            break;
        case '%': operation = (a, b) => a % b;
            break;

    }
    let result = operation(firstOperand, secondOperand);
    console.log(result);
}
mathOperations(5, 6, '+');
mathOperations(3, 5.5, '*');
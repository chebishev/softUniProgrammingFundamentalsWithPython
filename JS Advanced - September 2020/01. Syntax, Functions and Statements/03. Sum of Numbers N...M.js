function sumOfNumbersNtoM(firstElement, secondElement) {
    let firstNumber = Number(firstElement);
    let secondNumber = Number(secondElement);
    let result = 0;
    for (let i = firstNumber; i <= secondNumber; i++) {
        result += i;
    }
    console.log(result);
}
sumOfNumbersNtoM('1', '5');
sumOfNumbersNtoM('-8', '20');
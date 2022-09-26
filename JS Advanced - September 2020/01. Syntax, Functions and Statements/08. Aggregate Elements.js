function aggregateElements(numbers) {

    const sum = function (numbers) {
        let result = 0;

        for (let number of numbers) {
            result += number;

        }
        return result;
    };


    const sumInverted = numbers => {
        let result = 0;

        for (const number of numbers) {
            result += 1 / number;
        }
        return result;
    };

    const concat = numbers => numbers.join('');


    console.log(sum(numbers));
    console.log(sumInverted(numbers));
    console.log(concat(numbers));

}
aggregateElements([1, 2, 3]);
aggregateElements([2, 4, 8, 16]);
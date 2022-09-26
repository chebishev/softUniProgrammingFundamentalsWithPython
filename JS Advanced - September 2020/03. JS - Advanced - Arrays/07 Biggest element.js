function biggestElement(matrix) {
    let maxNumber = Number.MIN_SAFE_INTEGER;

    matrix.forEach(row => {
        let currentMax = Number.MIN_SAFE_INTEGER;

        row.forEach(num => {
            if (currentMax < num) {
                currentMax = num;
            }
        });

        if (maxNumber < currentMax) {
            maxNumber = currentMax;
        }
    });

    console.log(maxNumber);
}
biggestElement([[20, 50, 10],
[8, 33, 145]]);
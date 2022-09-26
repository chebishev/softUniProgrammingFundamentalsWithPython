function squareOfStars(size = 5) {

    for (let i = 0; i < size; i++) {
        let row = '';
        for (let j = 0; j < size; j++) {
            row += '* ';
        }

        console.log(row);
    }

}
squareOfStars(1);
squareOfStars(2);
squareOfStars(5);
squareOfStars();

function squareOfStars2(size = 5) {

    for (let i = 0; i < size; i++) {
        let row = '*'.repeat(size).split('').join(' ');

        console.log(row);
    }

}
squareOfStars2(1);
squareOfStars2(2);
squareOfStars2(5);
squareOfStars2();
function circleArea(element) {

    let elementType = typeof element;

    if (elementType == 'number') {
        let circleArea = Math.PI * (element ** 2);
        console.log(circleArea.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${elementType}.`);
    }
}
circleArea(5);
circleArea('name');
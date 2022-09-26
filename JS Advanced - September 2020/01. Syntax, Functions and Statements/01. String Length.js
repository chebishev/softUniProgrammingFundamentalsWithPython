function stringLength(first, second, third) {

    let sum = 0;
    let average = 0;
    sum += first.length;
    sum += second.length;
    sum += third.length;
    average = Math.floor(sum / 3);
    console.log(sum);
    console.log(average);

}
stringLength('chocolate', 'ice cream', 'cake');
stringLength('pasta', '5', '22.3');
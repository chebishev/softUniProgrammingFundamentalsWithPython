//original sorting
let numbers = [6, 3, 7, 4, 5, 10];
// console.log(numbers.sort());

//working sorting
function compareNumbers(a, b) {
    return a - b;
}
numbers.sort(compareNumbers);
console.log(numbers);


let names = ['gosho', 'pesho', 'mitko', 'grigor', 'stamat'];
names.sort(function (a, b) {
    return a.localeCompare(b);
});

//short version:
//names.sort((a, b) => a.localCompare(b));
console.log(names);
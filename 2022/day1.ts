import { readFileSync } from 'fs';

const file: string = readFileSync('./day1', 'utf-8');
const items = file.split('\r\n');
const elfs = [];

let cur = []
for(let i in items) {
    const item = items[i];
    if(item == '') {
        elfs.push(cur);
        cur = [];
    }else {
        cur.push(parseInt(item));
    }
}

const a = elfs.map(e => e.reduce((partialSum, a) => partialSum + a, 0));


console.log('part1: ', a.sort((a, b) => a - b).slice(-1)[0]);
const b = a.sort((a, b) => a - b).slice(-3)[0] + a.sort((a, b) => a - b).slice(-3)[1] + a.sort((a, b) => a - b).slice(-3)[2]
console.log('part2: ', b);


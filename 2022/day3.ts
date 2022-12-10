import {readFileSync} from "fs";
import _ from "lodash";

const file: string = readFileSync('./day3', 'utf-8');

const bags = file.trim().split('\r\n').map(bag => [bag.slice(0, bag.length/2).split(''), bag.slice(bag.length/2).split('')]);

let score = 0;
bags.forEach(b => {
    const intersect = _.intersection(b[0], b[1]);

    const charv = intersect[0].charCodeAt(0);
    let lscore: number = 0;
    if(charv < 97) { // uppercase
        lscore = charv - 64 + 26;
    }else {
        lscore = charv - 96;
    }
    score += lscore;
});


let bags2 = file.trim().split('\r\n')
let c = _.chunk(bags, 3).map(a => a.map(b => b.split('')));

let score2 = 0;
c.forEach(([a, b, c]) => {
    const intersect = _.intersection(a, b, c);

    const charv = intersect[0].charCodeAt(0);
    let lscore: number = 0;
    if(charv < 97) { // uppercase
        lscore = charv - 64 + 26;
    }else {
        lscore = charv - 96;
    }
    score2 += lscore;
})

console.log('part2: ', score2);


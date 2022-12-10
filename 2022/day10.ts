import {readFileSync} from "fs";
import {range, sum} from "lodash";


const file: string = readFileSync('./day10', 'utf-8');

interface Instruction {
    code: string;
    value: number | null;
}

const instructions = file.trim().split('\r\n').map(a => {
    const parts = a.split(' ');
    return {
        code: parts[0],
        value: parts.length > 1 ? parseInt(parts[1]) : null
    } as Instruction;
})

let value = 1;
let cycle = 0;

const t = [20, 60, 100, 140, 180, 220];
const v: number[] = [];

const screen = range(0, 6).map(_ => range(0, 40).map(_ => 0));


function tick(cycle: number, value: number, l2: number | null = null) {
    if(t.includes(cycle)) {
        v.push(l2 ? l2 : value);
    }

    const screenY = Math.floor(cycle / 40);
    const screenX = cycle - screenY * 40;

    if(Math.abs(screenX - value) <= 1) {
        screen[screenY][screenX] = 1;
    }
}

instructions.forEach(i => {
    if(i.code == 'noop') {
        cycle += 1;
        tick(cycle, value);

    }else if (i.code == 'addx') {
        cycle += 1;
        tick(cycle, value);
        cycle += 1;

        const l2 = value;
        value += i.value!;
        tick(cycle, value, l2);
    }else {
        throw new Error("Unknown code");
    }
})

console.log('part1: ', sum(v.map((v, i) => t[i] * v)));

console.log('part2:');
screen.forEach(l => {
    console.log(l.map(i => i == 1 ? '#' : '.').join(''));
})

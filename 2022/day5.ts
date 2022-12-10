import {readFileSync} from "fs";
import {range, intersection, isNaN} from "lodash";

const file: string = readFileSync('./day5', 'utf-8');

const input = file.trimEnd().split('\r\n');
const piecesTotal: string[][] = [];
let crateCount = 0;
input.every(i => {
    if(i.startsWith(' 1')) {
        return false;
    }

    // @ts-ignore
    const pieces = i.match(/.{1,4}/g).map(p => p.replace('[', '').replace(']', '').trim());
    piecesTotal.push(pieces);
    return true;
});

const stacks: string[][] = [];
for(let i in range(0, piecesTotal[0].length)) {
    stacks.push([]);
}
piecesTotal.reverse().forEach(pieces => {
    pieces.forEach((v, i) => {
       if(v) {
           stacks[i].push(v);
       }
    });
});

const moves = input.map(i => {
    return i.match(/move (\d+) from (\d+) to (\d+)/);
}).filter(m => m && m.length > 0).map(m => {
    // @ts-ignore
    return {
        // @ts-ignore
        count: parseInt(m[1]),
        // @ts-ignore
        from: parseInt(m[2]),
        // @ts-ignore
        to: parseInt(m[3])
    }
});

[1, 2].forEach(part => {
    const stacksCopy: typeof stacks = JSON.parse(JSON.stringify(stacks));

    moves.forEach(m => {
        const f = stacksCopy[m.from-1];
        const craneItems = [];
        for(let i in range(0, m.count)) {
            craneItems.push(f.pop());
        }
        if(part == 2) {
            craneItems.reverse();
        }

        const t = stacksCopy[m.to-1];

        // @ts-ignore
        t.push(...craneItems);
    })

    const result = stacksCopy.map(s => s.at(-1)).join('');
    console.log(`part${part}: `, result);
});






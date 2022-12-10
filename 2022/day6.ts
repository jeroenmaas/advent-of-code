import {readFileSync} from "fs";
import {range, intersection, isNaN} from "lodash";

const file: string = readFileSync('./day6', 'utf-8');


const lines = file.trim().split('\r\n');

[1, 2].forEach(part => {
    lines.forEach(l => {
        for (var i = 0; i != l.length; i++) {
            const length = part == 1 ? 4 : 14;

            const items = l.slice(i, i + length);
            if (new Set(items.split('')).size == length) {
                console.log(`part ${part}:` + (i + length));
                break;
            }
        }
    });
});

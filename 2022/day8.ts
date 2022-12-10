import {readFileSync} from "fs";
import {range, intersection, isNaN, forEach, sum, zip} from "lodash";
import path = require("node:path");


const file: string = readFileSync('./day8', 'utf-8');

let treeMap = file.trim().split('\r\n').map(l => l.split('').map(li => parseInt(li)));
let visibleMap = treeMap.map(m => m.map(mi => 0));

const ySize = treeMap.length;
const xSize = treeMap[0].length;

function rotate(a: number[][]): number[][] {
    return a[0].map((col, c) => a.map((row, r) => a[r][c]).reverse())
}

range(0, 4).forEach(i => {
    for (let y = 0; y !== ySize; y++) {
        let currentValue = null;

        for (let x = 0; x !== xSize; x++) {
            const treeHeight = treeMap[y][x];
            if (currentValue == null || treeHeight > currentValue) {
                visibleMap[y][x] = 1;
            }

            if (currentValue === null || treeHeight > currentValue) {
                currentValue = treeHeight;
            }
        }
    }

    treeMap = rotate(treeMap);
    visibleMap = rotate(visibleMap);
})

console.log('part1: ', sum(visibleMap.map(l => sum(l))))

interface Coordinate {
    x: number;
    y: number;
}

// height or taller than the tree under consideration
let possibleTreehouses: Coordinate[] = [];

for (let y = 0; y !== ySize; y++) {
    for (let x = 0; x !== xSize; x++) {
        possibleTreehouses.push({
            x: x,
            y: y
        });
    }
}

function isValidCoordinate(x: number, y: number): boolean {
    if (x < 0 || x >= xSize) {
        return false;
    }
    if (y < 0 || y >= ySize) {
        return false;
    }

    return true;
}

let bestScore: number | null = null;
possibleTreehouses.map(c => {
    const directions = [[0, -1], [-1, 0], [1, 0], [0, 1]];
    const treeHouseHeight = treeMap[c.y][c.x];
    const heights = directions.map(d => {
            let checking = [c.x, c.y]
            let visibleTrees = 0;
            while(true) {
                checking[0] += d[0]
                checking[1] += d[1]
                if(!isValidCoordinate(checking[0], checking[1])) {
                    break;
                }
                const losHeight = treeMap[checking[1]][checking[0]];

                visibleTrees += 1;
                if(losHeight >= treeHouseHeight) {
                    break;
                }
            }
            return visibleTrees;
        }
    )

    const score = heights.reduce((a, b)=> a*b, 1);
    if(!bestScore || score > bestScore) {
        bestScore = score;
    }
});

console.log('part2: ', bestScore);

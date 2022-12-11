import {readFileSync} from "fs";
import {range} from "lodash";

const file: string = readFileSync('./day11', 'utf-8');

interface Monkey {
    items: number[];
    operation: {
        operator: string;
        value: number | string;
    }
    testDivisible: number;
    onTrue: number;
    onFalse: number;
}

const monkeys = file.trim().split('\r\n\r\n').map(content => {
    const lines = content.split('\r\n');


    const operation = lines[2].replace('Operation: new = old ', '').trim().split(' ');

    return {
        items: lines[1].replace('Starting items: ', '').trim().split(', ').map(i => parseInt(i)),
        operation: {
            operator: operation[0],
            value: operation[1] != 'old' ? parseInt(operation[1]) : 'old',
        },
        testDivisible: parseInt(lines[3].replace('Test: divisible by ', '').trim()),
        onTrue: parseInt(lines[4].replace('If true: throw to monkey ', '').trim()),
        onFalse: parseInt(lines[5].replace('If false: throw to monkey ', '').trim()),
    } as Monkey;
});

function deepcopy<T>(a: T): T {
    return JSON.parse(JSON.stringify(a));
}

[[1, 20], [2, 10000]].forEach(([part, iterations]) => {
    const partMonkeys = deepcopy(monkeys);
    const inspectionCountByMonkey = partMonkeys.map(_ => 0);
    const monkeySum = partMonkeys.map(m => m.testDivisible).reduce((a, b)=> a*b, 1);

    range(0, iterations).forEach(_ => {

        partMonkeys.forEach((m, mIndex) => {
            while(m.items.length > 0) {
                let item = m.items.shift()!;
                inspectionCountByMonkey[mIndex] += 1;

                if(m.operation.operator == '*') {
                    if (typeof m.operation.value === "string") {
                        item *= item;
                    }else {
                        item *= m.operation.value;
                    }
                }else if (m.operation.operator == '+') {
                    if (typeof m.operation.value === "string") {
                        item += item;
                    }else {
                        item += m.operation.value;
                    }
                }else {
                    throw new Error("Unknown operator");
                }

                if(part == 1) {
                    item = Math.floor(item / 3);
                }else {
                    item = item - Math.floor(item / monkeySum) * monkeySum;
                }

                const isDivideable = (item / m.testDivisible) % 1 == 0;
                partMonkeys[isDivideable ? m.onTrue : m.onFalse].items.push(item);
            }

        })
    });


    const score = inspectionCountByMonkey.sort((a, b) => b - a).slice(0, 2).reduce((a, b)=> a*b, 1);
    console.log(`part${part}: `, score);
})





import {readFileSync} from "fs";
import {range, sum} from "lodash";
import {WeightedGraph} from "./utils/dijkstra";

const file: string = readFileSync('./day16', 'utf-8');

interface Valve {
    name: string;
    rate: number;
    tunnels: string[];
}

function deepcopy<T>(a: T): T {
    return JSON.parse(JSON.stringify(a));
}

const valves = file.trim().split('\r\n').map(line => {
    line = line.replace('Valve ', '')
    const name = line.slice(0, 2);
    line = line.substring(7).replace('flow rate=', '');

    const rate = parseInt(line.split(';')[0]);
    const tunnels = line.split(';')[1].replace(' tunnels lead to valves ', '').replace(' tunnel leads to valve ', '').split(',').map(t => t.trim())

    return {
        name,
        rate,
        tunnels
    } as Valve;
});

const valuesByName: {[key: string]: Valve} = {};
valves.forEach(v => valuesByName[v.name] = v);

console.log(valves);

interface Option {
    currentPos: string;
    value: number;
    openValves: string[];
}

let options: Option[] = [{
    currentPos: 'AA',
    value: 0,
    openValves: []
}];


function hasOpenValveOrChildWithClosedValve(valve: Valve, checkedRoutes: string[], openValves: string[]): boolean {
    if(openValves.indexOf(valve.name) == -1 && valve.rate > 0) {
        return true;
    }

    for(var i = 0; i !== valve.tunnels.length; i++) {
        const tunnelValve = valuesByName[valve.tunnels[i]];

        // We've already looked this way
        if(checkedRoutes.indexOf(valve.name) !== -1) {
            continue;
        }

        if(hasOpenValveOrChildWithClosedValve(tunnelValve, [...checkedRoutes, valve.name], openValves)) {
            return true;
        }
    }

    return false;
}

// Should probably not do this turn style but option style.
// aka look what possible strategies are there to move and take those moves.

// Could also reduce amount of options by looking if we could still beat best option.
// Get distance to best option. e.g. 4. This would mean we could open 2 valves at most. If best 2 don't provide higher pressure than current best score no need to continue.

var graph = new WeightedGraph();
valves.forEach(v => graph.addVertex(v.name));
valves.forEach(v => {
    v.tunnels.forEach(t => graph.addEdge(v.name, t, 1));
})

const routeCache: {[key: string]: number} = {};

function getDistance(a: string, b: string): number {
    const cacheKey = [a, b].join('_');
    if(!routeCache[cacheKey]) {
        routeCache[cacheKey] = graph.Dijkstra(a, b).length;
    }
    return routeCache[cacheKey];
}

let turn = 0;
while(turn < 30) {
    console.log('turn: ', turn);
    console.log('option length: ', options.length);

    const bestOption = options.reduce(function(prev, current) {
        return (prev.value > current.value) ? prev : current
    });
    const bestOptionPressure = sum(bestOption.openValves.map(o => valuesByName[o].rate));

    options = options.filter(o => {
        const valueDiff = bestOption.value - o.value;
        const pressDiff = bestOptionPressure - sum(o.openValves.map(ov => valuesByName[ov].rate)); // postive if bestOption is better
        const distance = getDistance(bestOption.currentPos, o.currentPos);

        const openableValues = Math.floor(distance / 2);
        const remainingTurns = 30 - turn;


        const reachableValves = valves.filter(v => {
            return getDistance(o.currentPos, v.name) <= distance;
        })

        const maxAdditionalPressure = sum(reachableValves.filter(v => o.openValves.indexOf(v.name) == -1).map(v => v.rate).sort((a, b) => a - b).slice(-openableValues));
        const c = pressDiff - maxAdditionalPressure; // c should become negative.
        // We're never going to beat best score. No need to continue looking
        if(valueDiff > -c * remainingTurns) {
            return false;
        }

        return true;
    });

    console.log('filtered option length: ', options.length);

    const setTest = new Set<string>([]);

    options.forEach(o => setTest.add([o.currentPos, ...o.openValves.sort()].join('_')));
    console.log('unique option length: ', setTest.size);

    let newOptions: Option[] = [];
    options.forEach(o => {
        const valve = valuesByName[o.currentPos];
        const startOptions = newOptions.length;

        if(valve.rate > 0 && o.openValves.indexOf(o.currentPos) == -1) {
            const newOption = deepcopy(o);
            newOption.value += sum(newOption.openValves.map(o => valuesByName[o].rate));
            newOption.openValves.push(o.currentPos);
            // TODO: Calculate value update
            newOptions.push(newOption);
        }

        valve.tunnels.forEach(t => {
            // Check if there is a route in this tunnel that actually opens a valve.

            const tunnelValve = valuesByName[t];
            if(hasOpenValveOrChildWithClosedValve(tunnelValve, [], o.openValves)) {
                const newOption = deepcopy(o);
                newOption.value += sum(newOption.openValves.map(o => valuesByName[o].rate));
                newOption.currentPos = t;
                // TODO: Calculate value update
                newOptions.push(newOption);
            }
        });

        // Opening a valve or moving to a new tunnel was not an option so just doing nothing remains.
        if(startOptions == newOptions.length) {
            const newOption = deepcopy(o);
            newOption.value += sum(newOption.openValves.map(o => valuesByName[o].rate));
            newOptions.push(newOption);
        }
    });

    options = newOptions;

    // console.log('count without open valve ', options.filter(o => o.openValves.length == 0).length);
    turn++;
}

const bestOption = options.reduce(function(prev, current) {
    return (prev.value > current.value) ? prev : current
});
console.log(bestOption);
// console.log(options);

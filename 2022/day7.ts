import {readFileSync} from "fs";
import {range, intersection, isNaN, forEach, sum} from "lodash";
import path = require("node:path");


const file: string = readFileSync('./day7', 'utf-8');

const lines = file.trim().split('\r\n');
lines.shift();



interface Command {
    command: String;
    output: String[];
}

const commands: Command[] = [];
let currentCommand: Command | null = null;
lines.forEach(l => {
    if(l.startsWith('$')) {
        if(currentCommand) {
            commands.push(currentCommand);
        }
        currentCommand = {
            command: l.slice(2),
            output: []
        }
    }else {
        currentCommand!.output.push(l)
    }
})
commands.push(currentCommand!);

let currentDir = '/'
const filesystem: { [key: string]: number | null} = {'\\': null}

commands.forEach(c => {
    if(c.command == 'cd ..') {
        currentDir = path.join(currentDir, '../')
    }else if (c.command == 'ls') {
        c.output.forEach(o => {
            const [sizeOrDir, dirOrFilename] = o.split(' ')
            if(sizeOrDir == 'dir') {
                filesystem[path.join(currentDir, dirOrFilename + '/')] = null;
            }else {
                filesystem[path.join(currentDir, dirOrFilename)] = parseInt(sizeOrDir);
            }
        })

    }else if (c.command.startsWith('cd')) {
        currentDir = path.join(currentDir, c.command.slice(3) + '/')
    }else {
        throw Error("Unknown command: " + c.command);
    }
});

interface FolderWithSize {
    path: string;
    size: number;
}

const paths = Object.keys(filesystem);
const folders = paths.filter(path => path.endsWith('\\'));
const folderInfos = folders.map(folderPath => {
    return {
        path: folderPath,
        size: sum(paths.filter(p => p.startsWith(folderPath) && !p.endsWith('\\')).map(p => filesystem[p]))
    } as FolderWithSize;
})

console.log('part1: ', sum(folderInfos.filter(f => f.size <= 100000).map(f => f.size)))

const filesystemSize = 70000000; // 7
const spaceNeeded = 30000000; // 3
const currentUsedSpace = sum(paths.filter(p => !p.endsWith('\\')).map(p => filesystem[p])); // 5
const spaceNeededToClean = spaceNeeded + currentUsedSpace - filesystemSize;

folderInfos.sort((a, b) => {
    return a.size - b.size;
});
folderInfos.every(fi => {
    if(fi.size >= spaceNeededToClean) {
        console.log('part2: ', fi.size);
        return false;
    }

    return true;
})

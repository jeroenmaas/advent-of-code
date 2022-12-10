import {readFileSync} from "fs";

const file: string = readFileSync('./day2', 'utf-8');

const options = file.trim().split('\r\n').map(line => line.split(' '))
const lookup: {[key: string]: string} = {'X': 'A', 'Y': 'B', 'Z': 'C'};

let score = 0;
options.forEach(o => {
    const player1 = o[0];
    const player2 = lookup[o[1]];

    if(player1 == player2) {
        score += 3;
    }else if (player1 == 'A' && player2 == 'B') {
        score += 6;
    }else if (player1 == 'C' && player2 == 'A') {
        score += 6;
    }else if (player1 == 'B' && player2 == 'C') {
        score += 6;
    } else {
        // player 1 wins no point.
    }

    let piece_score = 0;
    if(player2 == 'A') {
        piece_score = 1;
    }else if (player2 == 'B') {
        piece_score = 2;
    }else {
        piece_score = 3;
    }
    score += piece_score;
});

console.log('part1: ', score);

score = 0;
options.forEach(o => {
    const player1 = o[0];

    let player2: string;
    if (o[1] == 'Y') {
        player2 = player1;
    }else {
        if(player1 == 'A') { // rock
            if(o[1] == 'X') { // lose
                player2 = 'C'; // wins of sissors
            }else {
                player2 = 'B'; // loses to paper
            }
        }else if (player1 == 'B') { // paper
            if(o[1] == 'X') {
                player2 = 'A'; // wins of rock
            }else {
                player2 = 'C'; // loses to sissors
            }
        }else { // sisors
            if(o[1] == 'X') {
                player2 = 'B'; // wins of paper
            }else {
                player2 = 'A'; // loses to rock
            }
        }
    }

    if(player1 == player2) {
        score += 3;
    }else if (player1 == 'A' && player2 == 'B') {
        score += 6;
    }else if (player1 == 'C' && player2 == 'A') {
        score += 6;
    }else if (player1 == 'B' && player2 == 'C') {
        score += 6;
    } else {
        // player 1 wins no point.
    }

    let piece_score = 0;
    if(player2 == 'A') {
        piece_score = 1;
    }else if (player2 == 'B') {
        piece_score = 2;
    }else {
        piece_score = 3;
    }
    score += piece_score;
});

console.log('part2: ', score);

// 12335 too low

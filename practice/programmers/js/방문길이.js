"use strict";

function solution(dirs) {
  const MAX = 5;
  const dir_obj = {
    U: [0, 1],
    D: [0, -1],
    R: [1, 0],
    L: [-1, 0],
  };
  const route_set = new Set();
  let pos = [0, 0];
  let count = 0;
  for (let dir of dirs) {
    const [x, y] = pos;
    const [dx, dy] = dir_obj[dir];
    const [nx, ny] = [x + dx, y + dy];
    if (nx < -MAX || nx > MAX || ny < -MAX || ny > MAX) {
      continue;
    }
    const route = [x, y, nx, ny].join("");
    const route_reverse = [nx, ny, x, y].join("");
    if (!route_set.has(route) || !route_set.has(route_reverse)) {
      count += 1;
      route_set.add(route);
      route_set.add(route_reverse);
    }

    pos = [nx, ny];
  }
  return count;
}

console.log(solution("ULURRDLLU"));
console.log(solution("LULLLLLLU"));

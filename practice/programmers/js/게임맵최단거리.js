'use strict';

const dirs = [
  [-1, 0],
  [0, -1],
  [0, 1],
  [1, 0],
];

function solution(maps) {
  const [m, n] = [maps.length, maps[0].length];
  const visited = [...Array(m)].map(() => [...Array(n).fill(false)]);

  function bfs() {
    const q = [[0, 0, 1]];
    while (q.length > 0) {
      const [x, y, lv] = q.shift();
      visited[x][y] = true;
      maps[x][y] = lv;
      // console.log(visited);
      // console.log(maps);
      for (let [dx, dy] of dirs) {
        const [nx, ny] = [x + dx, y + dy];
        if (nx < 0 || ny < 0 || nx >= m || ny >= n || maps[nx][ny] === 0) {
          continue;
        }

        if (
          visited[nx][ny] &&
          1 <= maps[nx][ny] &&
          maps[nx][ny] < maps[x][y] + 1
        ) {
          continue;
        }

        q.push([nx, ny, maps[x][y] + 1]);
      }
    }
  }
  bfs();
  console.log(maps);

  return maps[m - 1][n - 1] === 0 || maps[m - 1][n - 1] === 1
    ? -1
    : maps[m - 1][n - 1];
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
  ])
);

// console.log(solution([[1, 1]]));
// console.log(solution([[1], [1]]));

// console.log(
//   solution([
//     [1, 0],
//     [0, 1],
//   ])
// );

// console.log(
//   solution([
//     [1, 1],
//     [0, 1],
//   ])
// );

// console.log(
//   solution([
//     [1, 0],
//     [1, 1],
//   ])
// );

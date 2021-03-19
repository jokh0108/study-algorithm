'use strict';

function range(start, end, step) {
  return [...Array(end).slice(start).keys()].filter((x) => x % step == 0);
}

function sumMatrix(m) {
  return m.reduce(
    (acc, row) => acc + row.reduce((row_acc, val) => row_acc + val, 0),
    0
  );
}

function canCompress(m) {
  const s = sumMatrix(m);
  return s == 0 || s == m.length ** 2;
}

function solution(arr) {
  const n = arr.length;
  let w = 1;
  let one = sumMatrix(arr);
  let zero = n ** 2 - one;
  while (w <= n) {
    for (let i of range(0, n, w)) {
      for (let j of range(0, n, w)) {
        const subMatrix = arr.slice(i, i + w).map((row) => row.slice(j, j + w));
        if (w >= 2 && canCompress(subMatrix) && subMatrix[0][0] == 1) {
          one -= 3;
        }
        if (w >= 2 && canCompress(subMatrix) && subMatrix[0][0] == 0) {
          zero -= 3;
        }
      }
    }

    w *= 2;
  }
  return [zero, one];
}

// def solution(arr):
//     while w <= n:
//         for i in range(0, n, w):
//             for j in range(0, n, w):
//                 subMatrix = [row[j:j+w]for row in arr[i:i+w]]
//                 # print("subMatrix", *subMatrix, sep='\n')
//                 if w >= 2 and can_compress(subMatrix) and subMatrix[0][0] == 1:
//                     one -= 3
//                 if w >= 2 and can_compress(subMatrix) and subMatrix[0][0] == 0:
//                     zero -= 3
//                 # print(zero, one)
//         w *= 2
//     return [zero, one]

console.log(
  solution([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
  ])
);
console.log(
  solution([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
  ])
);

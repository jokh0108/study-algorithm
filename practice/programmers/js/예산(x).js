'use strict'
function solution(requests, budget) {
  console.log(requests.sort())
  return requests
    .sort()
    .reduce(
      ([count, budget], request) =>
        budget >= request ? [count + 1, budget - request] : [count, budget],
      [0, budget]
    )[0]
}

// console.log(solution([10000], 1))
// console.log(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], 1))
// console.log(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], 1))
// console.log(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], 6))
// console.log(solution([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], 100))
console.log(solution([1, 2, 3], 9))
// console.log(solution([1, 3, 2, 5, 4], 9))
// console.log(solution([2, 2, 3, 3], 10))

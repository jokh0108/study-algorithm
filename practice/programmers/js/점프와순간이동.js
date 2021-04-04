'use strict'

function solution(n) {
  let count = 0
  while (n > 0) {
    if (n % 2 === 1) {
      count += 1
      n -= 1
    } else {
      n = Math.floor(n / 2)
    }
  }
  return count
}

console.log(solution(5))
console.log(solution(6))
console.log(solution(5000))

'use strict'

function makeCombination(arr, selectNumber) {
  const results = []
  if (selectNumber === 1) return arr.map((value) => [value]) // 1개씩 택할 때, 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1) // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = makeCombination(rest, selectNumber - 1) // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((combination) => [fixed, ...combination]) //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached) // 배열 spread syntax 로 모두다 push
  })

  return results // 결과 담긴 results return
}

function makePrimes(num) {
  let primes = [...Array(num).keys()].slice(2)
  for (let divisor of [...Array(Math.floor(num ** 0.5 + 1)).keys()].slice(2)) {
    primes = primes.filter((p) => p === divisor || p % divisor !== 0)
  }
  return new Set(primes)
}

function solution(nums) {
  const primeSet = makePrimes(3000)
  const combinations = makeCombination(nums, 3)
  return combinations.filter((c) => {
    const sum = c.reduce((acc, cur) => acc + cur, 0)
    return primeSet.has(sum)
  }).length
}

console.log(solution([1, 2, 3, 4]))
console.log(solution([1, 2, 7, 6, 4]))

'use strict'

function solution(n, words) {
  const used = new Set()
  for (let [index, word] of words.entries()) {
    console.log(index > 0 ? words[index - 1] : '', word, used)
    if (
      (index > 0 && words[index - 1].slice(-1) !== word[0]) ||
      used.has(word) ||
      word.length === 1
    ) {
      return [(index % n) + 1, Math.floor(index / n) + 1]
    }
    used.add(word)
  }
  return [0, 0]
}

console.log(
  solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])
)

'use strict'

function solution(board, moves) {
  let answer = 0
  const N = board.length
  const stack = []
  for (const move of moves) {
    const col = move - 1
    for (const row of Array(N).keys()) {
      const target = board[row][col]
      if (target !== 0 && target === stack.slice(-1).pop()) {
        stack.pop()
        board[row][col] = 0
        answer += 2
        break
      }
      if (target !== 0 && target !== stack.slice(-1).pop()) {
        stack.push(target)
        board[row][col] = 0
        break
      }
    }
  }
  return answer
}

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
)

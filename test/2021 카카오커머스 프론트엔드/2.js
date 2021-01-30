function solution(width, newBlocks) {
  let blocks = [0]
  newBlocks.forEach((newBlock) => {
    console.log(111111)
    const len = blocks.length
    let lowestFloor = len - 1
    for (let i = len - 1; i >= 0; i -= 1) {
      console.log(blocks, blocks[i], newBlock, i, len - 1)
      if (width < blocks[i] + newBlock) {
        if (i === len - 1) {
          blocks.push(newBlock)
          return
        }
        blocks[i + 1] += newBlock
      } else {
        lowestFloor = i
      }
    }
    blocks[lowestFloor] += newBlock
  })
  console.log(blocks)
  return blocks.length
}

// console.log(solution(4, [2, 3, 1]))
console.log(solution(4, [3, 2, 3, 1]))

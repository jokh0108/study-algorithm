'use strict'

function solution(string) {
  return string
    .slice(2)
    .slice(0, -2)
    .split('},{')
    .map((tuple) => tuple.split(','))
    .map((tuple) => tuple.map((e) => +e))
    .sort((a, b) => a.length - b.length)
    .reduce((acc, cur, index, arr) => {
      if (index === 0) {
        return cur
      }
      const newElement = [...cur]
        .filter((e) => !arr[index - 1].includes(e))
        .pop()
      return [...acc, newElement]
    }, [])
}

console.log(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))

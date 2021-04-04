'use strict'

function match(a, b) {
  if (a.length !== b.length) {
    return false
  }
  for (const [index, char] of [...b].entries()) {
    if (char === '*') {
      continue
    }
    if (char !== a[index]) {
      // console.log('Not matched')
      return false
    }
  }
  // console.log('matched')
  return true
}

function solution(userIds, bannedIds) {
  var answer = 0
  const map = {}
  for (const bannedId of bannedIds) {
    if (map.hasOwnProperty(bannedId)) {
      map[bannedId][1] += 1
    } else {
      map[bannedId] = [userIds.filter((id) => match(id, bannedId)), 1]
    }
  }
  console.log(map)
  return answer
}

console.log(
  solution(['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'], ['fr*d*', 'abc1**'])
)
console.log(
  solution(
    ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'],
    ['*rodo', '*rodo', '******']
  )
)

console.log(
  solution(
    ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc'],
    ['fr*d*', '*rodo', '******', '******']
  )
)

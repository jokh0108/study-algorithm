'use strict'

const getCombinations = function (arr, selectNumber) {
  const results = []
  if (selectNumber === 1) return arr.map((value) => [value]) // 1개씩 택할 때, 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1) // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombinations(rest, selectNumber - 1) // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((combination) => [fixed, ...combination]) //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached) // 배열 spread syntax 로 모두다 push
  })

  return results // 결과 담긴 results return
}

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
  const map = {}
  for (const bannedId of bannedIds) {
    map.hasOwnProperty(bannedId)
      ? (map[bannedId][1] += 1)
      : (map[bannedId] = [userIds.filter((id) => match(id, bannedId)), 1])
  }
  // console.log(map)
  let stack = []
  for (const [ids, r] of Object.values(map)) {
    console.log(ids, r)
    const combinations = getCombinations(ids, r)
    console.log('combinations', combinations)
    const newStack = []
    if (stack.length === 0) {
      for (const c of combinations) {
        newStack.push(new Set(c))
      }
      stack = newStack
      continue
    }
    console.log('stack', stack)
    for (const set of stack) {
      for (const c of combinations) {
        console.log('set', set, 'c', c)
        const newSet = new Set([...set, ...c])
        console.log('newSet', newSet)
        newStack.push(newSet)
      }
    }
    stack = newStack
    console.log(stack)
  }
  const cases = stack.filter((set) => set.size === bannedIds.length)
  console.log(cases)
  return cases.length
}

// function insert(root, string) {
//   if (root[string[0]]) {
//     insert(root[string[0]], string.slice(1))
//     return
//   }
//   if (string.length === 1) {
//     root[string[0]] = { isWord: true }
//     return
//   }
//   root[string[0]] = {}
//   insert(root[string[0]], string.slice(1))
// }

// function solution(userIds, bannedIds) {
//   let count = 0
//   const trie = {}

//   for (const userId of userIds) {
//     insert(trie, userId)
//   }
//   console.dir(trie, { depth: null })

//   const answer = []
//   function dfs(root, level, bannedId) {
//     if (root['isWord'] && level === bannedId.length) {
//       count += 1
//       return
//     }
//     for (const child of Object.keys(root)) {
//       if (bannedId[level] === '*' || bannedId[level] === child) {
//         dfs(root[child], level + 1, bannedId)
//       }
//     }
//   }
//   for (const bannedId of bannedIds) {
//     dfs(trie, 0, bannedId)
//   }

//   return count
// }

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

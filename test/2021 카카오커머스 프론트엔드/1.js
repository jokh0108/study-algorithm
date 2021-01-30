function solution(n, record) {
  const CHARACTER_MAX = 5
  const serverMap = [...Array(n + 1).keys()].reduce((acc, cur) => {
    if (cur === 0) return acc
    return Object.assign(acc, { [cur]: [] })
  }, {})
  record.forEach((aRecord) => {
    const [server, newNickName] = aRecord.split(' ')
    if (serverMap[server].includes(newNickName)) {
      return
    }
    if (serverMap[server].length === CHARACTER_MAX) {
      serverMap[server] = [...serverMap[server].slice(1), newNickName]
    } else {
      serverMap[server].push(newNickName)
    }
  })
  // console.log(serverMap)

  const answer = Object.values(serverMap).reduce((acc, cur) => {
    return [...acc, ...cur]
  }, [])
  return answer
}

console.log(
  solution(1, [
    '1 fracta',
    '1 sina',
    '1 hana',
    '1 robel',
    '1 abc',
    '1 sina',
    '1 lynn',
  ])
)

console.log(
  solution(4, [
    '1 a',
    '1 b',
    '1 abc',
    '3 b',
    '3 a',
    '1 abcd',
    '1 abc',
    '1 aaa',
    '1 a',
    '1 z',
    '1 q',
    '3 k',
    '3 q',
    '3 z',
    '3 m',
    '3 b',
  ])
)

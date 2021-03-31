'use strict'

function solution(skill, skill_trees) {
  const skill_sequences = new Set(
    skill.split('').map((_, index) => skill.slice(0, index + 1))
  )
  const skills = new Set(skill.split(''))
  console.log(skill_sequences, skills)
  const answer = skill_trees
    .map((tree) =>
      tree
        .split('')
        .filter((node) => skills.has(node))
        .join('')
    )
    .filter((tree) => skill_sequences.has(tree) || !tree)
  return answer
}

console.log(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']))
console.log(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA', 'AQWER']))

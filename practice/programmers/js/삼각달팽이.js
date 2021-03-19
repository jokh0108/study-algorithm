const dirs = [[1, 0], [0, 1], [-1, -1]]

function solution(n) {
    const matrix = new Array(n).fill(0).map(() => new Array(n).fill(0));
    // console.log(matrix) 
    let [i, j, dir_i] = [0, 0, 0]
    // console.log(i, j, dir_i)
    for (let k of [...Array(n*(n+1)/2).keys()].map(x => x+1)){
        // console.log(k)
        matrix[i][j] = k
        if (i ===  n-1 && j === 0){
            dir_i = (dir_i + 1) % 3
        } else if (i == n-1 && j == n-1){
            dir_i = (dir_i + 1) % 3
        } else {
            const [di, dj] = dirs[dir_i]
            if (matrix[i+di][j+dj] != 0){
                dir_i = (dir_i + 1) % 3
            }
        }
        const [di, dj] = dirs[dir_i]
        i += di
        j += dj
    }
    const answer = matrix.flatMap((row) => row.filter((x) => x != 0))
    console.log(answer)
    return answer
}

console.log(solution(4))
console.log(solution(5))
console.log(solution(6))


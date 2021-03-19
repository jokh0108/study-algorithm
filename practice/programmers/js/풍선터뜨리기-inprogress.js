function solution(arr) {
  let answer = 2; // 양쪽 끝은 항상 가능
  let left_min = arr[0];
  let right_min = Math.min(...arr.slice(1));
  console.log(right_min);
  for (let i = 1; i < arr.length - 1; i++) {}
  return answer;
}

// console.log(solution([9, -1, -5]));
console.log(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]));

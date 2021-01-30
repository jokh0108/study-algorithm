function solution(clothes) {
  const clotheCounter = clothes.reduce((accumulator, [_, category]) => {
    if (accumulator[category]) {
      accumulator[category] += 1;
    } else {
      accumulator[category] = 1;
    }
    return accumulator;
  }, {});
  const product = Object.values(clotheCounter).reduce((accumulator, count) => {
    return accumulator * (count + 1);
  }, 1);
  return product - 1;
}

solution([
  ["yellow_hat", "headgear"],
  ["blue_sunglasses", "eyewear"],
  ["green_turban", "headgear"],
]);

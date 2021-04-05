function minimumLoss(prices) {
  let minLoss = prices[1] - prices[0];
  for (let [index, curPrice] of prices.entries()) {
    console.log(index, curPrice);
    if (index <= 1) {
      continue;
    }
    console.log(minLoss, prices[0] - curPrice, prices[1] - curPrice);
    minLoss = Math.min(minLoss, prices[0] - curPrice);
    minLoss = Math.min(minLoss, prices[1] - curPrice);
  }
  return minLoss;
}

console.log(minimumLoss([5, 10, 3]));
console.log(minimumLoss([20, 15, 8, 2, 12]));

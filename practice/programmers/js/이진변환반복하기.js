'use strict';

function convert(binary, radix) {
  return parseInt(binary, 10).toString(radix);
}

function solution(s) {
  let changed = 0;
  let removed = 0;

  while (s !== '1') {
    const before_len = s.length;
    // console.log('origin', s);
    s = s.replaceAll('0', '');
    // console.log('replace', s);
    // s = s.split('').filter((c) => c === '1');
    const after_len = s.length;

    s = after_len.toString(2);
    // console.log('after', s);

    changed += 1;
    removed += before_len - after_len;
    // console.log(changed, removed);
  }

  return [changed, removed];
}

console.log(solution('110010101001'));
console.log(solution('01110'));
console.log(solution('1111111'));

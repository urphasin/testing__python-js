let nums = [1, 2, 3];

for (let n of nums) {
  n *= 2;
}
for (let n in nums) {
  console.log(n);
}
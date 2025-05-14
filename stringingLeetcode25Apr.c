#include <string.h>
int countCompleteSubarrays(int *nums, int numsSize) {
  short map[2001] = {0};
  int rs = 0, totalDistinct = 0;
  for (int i = 0; i < numsSize; i++)
    if (map[nums[i]] == 0) {
      totalDistinct++;
      map[nums[i]]++;
    }

  memset(map, 0, 2001 * sizeof(short));
  map[nums[0]] = 1;
  int tmpDistinct = 1;
  for (int i = 0, j = 1; i < numsSize; i++) {
    while (j < numsSize && tmpDistinct < totalDistinct) {
      if (map[nums[j]] == 0)
        tmpDistinct++;
      map[nums[j]]++;
      j++;
    }

    if (tmpDistinct == totalDistinct)
      rs += numsSize - j + 1;
    else
      break;

    map[nums[i]]--;
    if (map[nums[i]] == 0)
      tmpDistinct--;
  }
  return rs;
}
/**
 * @param {Array<number>} arr The input integer array to be sorted.
 * @return {Array<number>}
 */
export default function insertionSort(arr) {
  for (let i =1; i < arr.length; i++){
    const currValue = arr[i];
    const j = i - 1;

    while ( j>= 0 && arr[j] > currValue){
      arr[j+1] = arr[j];

      j--;
    }

    arr[j+1] = currValue;
  }

  return arr
}
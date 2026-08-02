export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let calledCount = weakMap.get(endpoint) || 0;
  calledCount += 1;
  weakMap.set(endpoint, calledCount);

  if (calledCount >= 5) {
    throw new Error('Endpoint load is high');
  }
}
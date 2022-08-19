import { readFileSync } from 'fs';

console.time('elapsed')
const words = {};
const fileName = '../rust/first/alice_in_wonderland.txt'

const file = readFileSync(fileName, 'utf-8')
file.split(/(\s+)/).filter((e) => e.trim().length > 0).forEach(word => {
  word = word.toLowerCase()
  words[word] = 1 + (words[word] || 0)
})

const topLength = 1000;
let topWords = Array.from(Object.entries(words)).slice(0, topLength)
Object.entries(words).forEach(([word, n]) => {
  for (const [i, top] of topWords.entries()) {
    if (n > top[1]) {
      const tmp = topWords.slice(i, topWords.length-1)
      topWords[i] = [word, n]
      topWords = topWords.slice(0, i+1).concat(tmp)
      break
    }
  }
})

console.log(topWords)
console.timeEnd('elapsed')

// JavaScript Program to check if the 2 input strings are Anagrams or not.

function main() {
//INPUT
  
var a = readLine().split("");
var b = readLine().split("");
var countA = a.length;
var countB = b.length;
var count = countA + countB;
    var pair = 0;
    for(var i = 0; i < countA;i++){
        for(var j = 0; j < countB; j++){
            if(a[i] == b[j]){
                b.splice(j,1);
                pair++;
                break;
            }
        }
    }
    console.log(count - (pair*2));
}

const fibonacci = (num) => {
    let cycle = num
    let a = 0
    let y = 1
    let z = 1

      i = 2
      while(cycle > i){
        a = y
        y = z
        z = a + y
        i++
        console.log(a,y)
      }
      return z
   
    
}

console.log(fibonacci(11))




  
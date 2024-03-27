/*fibo example with recursio
take into account the following 
fibo starts in 1 and then adds to their previous number which in this case is 0
so 
last = 1
previousLast = last-1
so to find sibo we do the sum = last + lastlast , now we update previousLast = last and last = sum  

then if we wanna find the nth fibo we should find by this pointing to last = n -1; poiting to previousLast = n -2 / last - 1
having this we're gonna implement iterative version and the next we'll split this version to recursive one 

function getNthfibo(n){
    last = 1 
    previousLast = last - 1 
    sum = 0
    for (let c = 1;c<=n;c++){
        sum = last + previousLast;
        previousLast = last 
        last = sum
    }

}

//
*/
//iteractive version 
function getNthfibo(n){
    last = 1 
    previousLast = last - 1 
    sum = 0
    for (let c = 1;c<=n;c++){
        sum = last + previousLast;
        previousLast = last 
        last = sum
    }

}

//recursive version 
function getNthFibo(n){
    if(n<=1)return 1;
    return getNthFibo(n-1) + getNthFibo(n-2)
}

//Tail recursion
function tail(n,previousLast, last){
    if(n ==0) return previousLast;
    if (n==1)return last;
    return tail(n-1, last, last+previousLast)
}

// challenge implement Pascal’s Triangle
//formula pascalTriangle(row - 1, col) + pascalTriangle(row - 1, col - 1). 

// Understanding recursion fibo 


//Understanding recursion tail fibo 
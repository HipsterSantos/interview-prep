function throttle(func: ()=>void,delay: number): Function{
    let timeoutId: Function | number| any,
    upThis: any ,
    upArgs: IArguments | any;
    return function(){
        //first create reference to this and args 
        const innerContext: any = this
        const innerArgs: IArguments = arguments
        // the check if timeoutId have function running 
        if(!timeoutId){
            func.apply(upThis,upArgs)
            console.log('--#immediately-called', timeoutId)
            //checking subsequent call 
            upThis = innerContext
            upArgs = innerArgs
            timeoutId = setTimeout(function(){
                //resettimeoutid 
                timeoutId = null
                if(!timeoutId){
                    func.apply(upThis,upArgs)
                    upArgs = null ;
                    upThis = null;
                }
                console.log('--called-and-timeoutid', timeoutId)

            },delay)
        }

    }
}
function toBeThrottled():void{
    //do someting here
    console.log('do something right here--')
}
const throttleReturned:Function = throttle(toBeThrottled,2000)

// throttleReturned()

// const throttleReturned2:Function = throttle(toBeThrottled,500)
// console.log('\ncall--', throttleReturned())
// console.log('\n\n\n2-call--', throttleReturned())


// console.log('throttle--', throttleReturned2)


function throttleWithWorkers(workers, delay, batchSize) {
    let index = 0;
  
    function executeBatch() {
      const batch = workers.slice(index, index + batchSize);
      index += batchSize;
  
      if (batch.length > 0) {
        Promise.all(batch.map(worker => worker())).then(() => {
          setTimeout(executeBatch, delay);
        });
      }
    }
  
    executeBatch();
  }
  
  // Example array of 50 promised functions (workers)
  const workers = Array.from({ length: 50 }, (_, i) => () => {
    return new Promise(resolve => {
      console.log(`Worker ${i + 1} started.`);
      // Simulating asynchronous work with a delay
      setTimeout(() => {
        console.log(`Worker ${i + 1} finished.`);
        resolve();
      }, Math.random() * 1000); // Random delay between 0 and 1000 milliseconds
    });
  });
  
  // Throttle the execution of workers with a delay of 500 milliseconds and a batch size of 5
  throttleWithWorkers(workers, 500, 5);
  
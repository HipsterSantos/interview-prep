import 'dotenv/config';
import debug from 'debug';

const logger = debug('core');

// Generate random delays for each worker
const delays = [...Array(50)].map(() => Math.floor(Math.random() * 900) + 100);

// Create an array of asynchronous functions simulating a workload
const load: (() => Promise<number>)[] = delays.map(
  (delay) => (): Promise<number> =>
    new Promise((resolve) => {
      setTimeout(() => resolve(Math.floor(delay / 100)), delay);
    })
);

// Define the type for a task (asynchronous function)
type Task = () => Promise<number>;

// Throttle function to control the execution of tasks
const throttle = async (workers: number, tasks: Task[]) => {
  const results: number[] = [];
  const queue: Task[] = [...tasks]; // Create a copy of tasks array to avoid mutation
  const running: Promise<void>[] = [];

  // Function to execute a task by a worker
  const executeTask = async (task: Task) => {
    const result = await task(); // Execute the task
    results.push(result); // Store the result
    // If there are remaining tasks in the queue, execute the next task
    if (queue.length > 0) {
      const nextTask = queue.shift()!;
      await executeTask(nextTask);
    } else {
      // If the queue is empty, remove the worker from the running list
      const index = running.indexOf(promise);
      if (index !== -1) {
        running.splice(index, 1);
      }
    }
  };

  // Start workers
  for (let i = 0; i < workers && i < queue.length; i++) {
    const task = queue.shift()!;
    const promise = executeTask(task);
    running.push(promise); // Track running workers
  }

  // Wait for all workers to finish
  await Promise.all(running);
  
  return results;
};

// Bootstrap function to start the program
const bootstrap = async () => {
  logger('Starting...');
  const start = Date.now();
  const answers = await throttle(5, load);
  logger('Done in %dms', Date.now() - start);
  logger('Answers: %O', answers);
};

// Call bootstrap function and handle errors
bootstrap().catch((err) => {
  logger('General fail: %O', err);
});

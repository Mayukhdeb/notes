# Self-Consistency Improves Chain of Thought Reasoning in Language Models

One issue with large language models has been to find a way to understand and leverage the concept of "chain of thought" (i.e reasoning).

The idea behind this paper is to make the LLM generate multiple completions (i.e chains of thought) and then select the result with the most highest number of occurrences among the samples.

highest number of occurrences -> "self consistency"

## How does it work ?

It's all mostly prompt and completion engineering:

1. We prepare a few-shot prompt which would contain at least one example of the kind of "chain of thought" we're looking for.

```
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.

Q: Janet’s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder for $2 per egg. How much does she make every day?
A:
```

2. Then, we feed this prompt into the model and collect a large set of possible completions via sampling.

3. From this sampled set of completions, we pick out the most consistent answer using a majority vote.

If the possible final verdicts (for the given prompt) are `[18, 14, 18]`, then we pick 18. It's that simple.

## Resources:
 * A nice dataset of binary questions and their reasons: https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/strategyqa/task.json
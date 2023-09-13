Let Q(k) be the number of questions needed to find the magic bean out of a selection of k beans (assuming one is the magic bean)

Initital thought: Start guessing the (entire) plates with the most number of beans first (until the correct plate has been identified)
Rationale: This rules out more beans if guesses are incorrect


### INITIAL CASE STUDY with (1, 2, 3)
Jack chooses plates with 3 beans first.

Min number of questions in each scenario:
    1. If plate 1 has the bean: 2               (guess plates 3, 2 incorrect)
    2. If plate 2 has the bean: 2 + Q(2) = 3    (guess plate 3 incorrect, plate 2 correct, then one more guess on plate 2)
    3. If plate 3 has the bean: 1 + Q(3) = 3    (guess plate 3 correct, then two more guesses on plate 3)
Total = 3 guesses = h(1, 2, 3).


### SECOND CASE STUDY with (2, 3, 3)
Again, Jack chooses plate 3 (WLOG) first to minimise the number of possible candidate magic beans

Min number of questions in each scenario:
    1. If plate 1 has the bean: 2 + Q(2) = 3    (guess plates 3, 2 incorrect, then one more guess on plate 1)
    2. If plate 2 has the bean: 2 + Q(3) = 4    (guess plate 3 incorrect, 2 correct, then two more guesses on plate 2)
    3. If plate 3 has the bean: 1 + Q(4) = 3    (guess plate 3 correct, then two more guess on plate 3)
Total = 4 guesses = h(2, 3, 3).


### HYPOTHESIS
In general, we might hypothesise that if m = min(a, b, c), M = max(a, b, c), and mid is the remaining plate, then

h(a, b, c) = max[1+Q(M), 2+Q(mid), 2+Q(m)],      i.e.        h(a, b, c) = max[1+Q(M), 2+Q(mid)],       since Q(mid) >= Q(m).

However...


### THIRD CASE STUDY with (0, 1, 5)
There is an alternate strategy to do better than 1 + Q(5) = 4 guesses. 

Partition plate 3 into 3 and 2 beans. Then do the following:
    1. Guess the large partition (of 3 beans) in plate 3.       Worst case: No (if yes, then number of guesses is 1 + Q(3) = 3)
    2. Guess the small partition (of 2 beans) in plate 3.       Worst case: Yes (if no, then done - magic bean is on plate 2)
    3. Then Q(2) = 1 guess required.
Total = 3 guesses = h(0, 1, 5). 


This was done in 1 fewer guess than the previous hypothesis claimed. Why is this? 

Due to the partition we created guessing on 3 plates (0, 1, 5) is indentical to guessing on (1, 2, 3).

Our hypothesis states this has a minimum of max(1+Q(3), 2+Q(2)) = 3 number of guesses. 


#### Fine tuning the hypothesis
We now seek to show that our hypothesis is valid once the plates have been "reduced" by partitions.

Idea: Remove plates with 0, and partition the largest plate into two half plates.

(0, 1, 12)
<=> (1, 6, 6)
<=> (1, 3, 3, 3, 3) 



So now we find Q.

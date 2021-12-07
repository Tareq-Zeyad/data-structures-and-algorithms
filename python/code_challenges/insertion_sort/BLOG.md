# Insertion Sort Blog.


- ### Reverse this array using insertion sort:

```
python
[8,4,23,42,16,15]
```

![insertion_sort_1](whiteboard_images/insertion_sort_1.PNG)

### Steps:

### At first, we split the array into 2 partitions, the sorted and unsorted arrays and then we compare the first element with the second, if the second element is less than the first element, we replace the first element with the second element, otherwise we are going to assume that its bigger and so move on.

![insertion_sort_1*](whiteboard_images/insertion_sort_1-1.PNG)

The third array element is bigger as we notice than its previos element so we will ignore that and move on.

![insertion_sort_2](whiteboard_images/insertion_sort_2.PNG)

Same for the next element, its already bigger.

![insertion_sort_3](whiteboard_images/insertion_sort_3.PNG)

Now the next element on the list is less than its previous element, so we are going to replace that element with its previous.

![insertion_sort_4](whiteboard_images/insertion_sort_4.PNG)

We still have the same thing, the previous element is bigger so we will justs replace that aswell

![insertion_sort_5](whiteboard_images/insertion_sort_5.PNG)

Now thats sorted, we will move on to the next element, but it also appears thats it less than its previous element so we will repeat the same steps

![insertion_sort_6](whiteboard_images/insertion_sort_6.PNG)

![insertion_sort_7](whiteboard_images/insertion_sort_7.PNG)

![insertion_sort_8](whiteboard_images/insertion_sort_8.PNG)


Finally, we got a sorted array that matches our expected outcome;

![insertion_sort_9](whiteboard_images/insertion_sort_9.PNG)


### Big O

Time = O(n^2)

Space = O(1)
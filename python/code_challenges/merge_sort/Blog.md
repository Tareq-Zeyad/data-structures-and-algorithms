# Merge Sort

More effcient method to sort an array.

Starting by sort this array using merge sort.
```
python
[8,4,23,42,16,15]
```

## Whiteboard Process.
![whiteboard](whiteboard_images/whiteboard-merge-sort.PNG)
<br>

## Steps
![whiteboard1](whiteboard_images/whiteboard1.PNG)

First start by dividing the array into 2 parts, the left and right until they are simple enough to compare between.

![whiteboard2](whiteboard_images/whiteboard2.PNG)

Then, if the elements are not simple enough to be compared directly, we repeat the same dividing process.

![whiteboard3](whiteboard_images/whiteboard3.PNG)

Then, if the elements are not simple enough to be compared directly, we repeat the same dividing process.

![whiteboard4](whiteboard_images/whiteboard4.PNG)

Now that we have each element of the original array as array of its own, we will start merging them back by comparing which element is higher.

![whiteboard5](whiteboard_images/whiteboard5.PNG)

Finally, we get the sorted array after comparing item by item and appending them in the right order.


# Big O:

- Time: O(log n)
- Space: O(log n)
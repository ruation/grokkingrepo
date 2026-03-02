# 2.1 Suppose you’re building an app to keep track of your inances.
## Every day, you write down everything you spent money on. At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list?

A linked list, because reading and insertion times are O(n) and O(1), respectively. Therefore, inserting something is faster than in an array.

## 2.2 Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders of the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order of the queue and cooks it. Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)

Linked list.

## 2.3 Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list? 

An array, because binary search requires random access. Arrays allow O(1) access to any index, while linked lists require O(n) time to reach a specific position.

## 2.4 People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?

One downside of using an array for storing users is that insertions are expensive. Since binary search requires the array to remain sorted, each new user must be inserted in the correct position. Although finding the position takes O(log n) time, inserting the user requires shifting elements, which takes O(n) time. Therefore, the overall insertion process is O(n), making arrays inefficient for frequent insertions.

## 2.5 In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with a. The second slot points to a linked list containing all the usernames starting with b, and so on.

This structure improves search efficiency by dividing users into 26 categories based on the first letter of their username. Accessing the correct slot in the array takes O(1) time, and searching within the linked list takes O(k), where k is the number of usernames starting with the same letter. In the average case, this is much faster than searching the entire list. However, in the worst case (if many usernames start with the same letter), the time complexity is still O(n).
# Making change

## 0.Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

	* Prototype: makeChange(coins, total)
	* Return: fewest number of coins to meet total
		-> if total is 0 or less, return 0
		-> if total cannot be met by any number of coins you have, return -1 
	* `coins` is a list of the values of the coins in your possession
	* The value of a coin will always be an integer greater than 0
	* You can assume you have an infinte number of each denomination of coin in the list
	* Your solution's runtime will be evaluated in this task.


```
Thought Process
```
Human Logic:
	Give person requesting for 15
	7 2's
	1 1
	
	becasue using the value in the array i had to determine wether the total is higher 
	than any value present or if its equal to any value there then when not any of the 
	above i went thru all the values again and chose the biggest value and multiplied it 
	by an ever increasing multiplier value till i get the total or close to the total before
    adding a remainder from any of the other values.	
	
	But the best approach would be to make this dynamic not always going for the bigger coins 
	and balancing the total with smaller values becasue you will end up with a lot of change 
	and this isnt the best case.
	
	So it would be better for me to iterate through all the values and use each value to reduce 
	the total, storing the amount of coins used for each value to make up the total and comparing 
	the values picking the smallest amount of coins by a value and returning it as the answer.
	
	1.takes coin and total
	2.if total <= 0, return 0
	3.coin_list sorted in descending order so the larger value comes first
	4. if coin in the coin list is less than the total then do steps 567
	5.coin_qty, contains number of coins gotten after a value in the coin_list has divided total with no remainder.
	6.new total value is any remainder from total and coin division.
	7.when total is 0 return the coin_qty



#include "lists.h"
/**
 * check_cycle - checks if a singly linked list is a cycle
 * @list : pointer to list to check
 * Return: 0 if no cycle, 1 if cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
		else
			return (0);
	}
	return (0);
}

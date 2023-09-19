#include "lists.h"
/**
 * check_cycle - checks if linked list contains cycle
 * @list: list to check
 *
 * Return: 1 if the list has a cycle,else 0 
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (list)
	{
		while (a && b && b->next)
		{
			a = a->next;
			b = b->next->next;
			if (a == b)
				return (1);
	}else if (!list)
	{
		return (0);
	}

	return (0);
}

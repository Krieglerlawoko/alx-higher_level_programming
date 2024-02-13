#include "lists.h"

/**
 * reverse_listint - Linked list reversed
 * @head: points to first node in list
 *
 * Return: points to first node in new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - linked list if is is a palindrome
 * @head: points to linked list
 *
 * Return: 1 for success else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fst = *head, *tmp = *head, *dp = NULL;

	if ((*head)->next == NULL || *head == NULL )
		return (1);

	while (1)
	{
		fst = fst->next->next;
		if (!fst)
		{
			dp = slw->next;
			break;
		}
		if (!fst->next)
		{
			dp = slw->next->next;
			break;
		}
		slw = slw->next;
	}

	reverse_listint(&dp);

	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dp)
		return (1);

	return (0);
}

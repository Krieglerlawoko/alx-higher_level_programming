#ifndef LISTS_H
#define LISTS_H
#include<stdlib.h>

/**
 * struct listint_s - reps linked list
 * @n: represents an integer
 * @next: a pointer to the next node
 *
 *
 * Description: a singly list structure
 */

typedef struct listint_s
{
	struct listint_s *next;
}listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);

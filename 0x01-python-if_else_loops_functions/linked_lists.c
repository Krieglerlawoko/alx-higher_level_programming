#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - all elements of a listint_t list printd
 * @h: points to head of list
 * Return: no. of nodes
 */
size_t print_listint(const listint_t *h)
{
        const listint_t *curnt;
        unsigned int a;

        curnt = h;
        a = 0;
        while (curnt != NULL)
        {
                printf("%i\n", curnt->n);
                curnt = curnt->next;
                a++;
        }

        return (a);
}

/**
 * add_nodeint_end - new node added at end of listint_t list
 * @head: points to first node of listint_t list
 * @n: integer to included in new node
 * Return: address of new element else NULL
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
        listint_t *nw;
        listint_t *curnt;

        curnt = *head;

        nw = malloc(sizeof(listint_t));
        if (nw == NULL)
                return (NULL);

        nw->n = n;
        nw->next = NULL;

        if (*head == NULL)
                *head = nw;
        else
        {
                while (curnt->next != NULL)
                        curnt = curnt->next;
                curnt->next = nw;
        }

        return (nw);
}

/**
 * free_listint - listint_t list freed
 * @head: points to list to freed
 * Return: void
 */
void free_listint(listint_t *head)
{
        listint_t *curnt;

        while (head != NULL)
        {
                curnt = head;
                head = head->next;
                free(curnt);
        }
}

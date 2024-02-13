#include "lists.h"

/**
 * insert_node - Number inserted into sorted singly linked list.
 * @head: list head
 * @number: number stored
 * Return: points to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *r;
        listint_t *nw;

        r = *head;

        nw = malloc(sizeof(listint_t));
        if (nw == NULL)
                return (NULL);
        nw->n = number;

        if ((*head)->n > number || *head == NULL)
        {
                nw->next = *head;
                *head = nw;
                return (nw);
        }

        while (r->next != NULL)
        {
                if ((r->next)->n >= number)
                {
                        nw->next = r->next;
                        r->next = nw;
                        return (nw);
                }
                r = r->next;
        }

        nw->next = NULL;
        r->next = nw;
        return (nw);
}

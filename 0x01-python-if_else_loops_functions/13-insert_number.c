#include "lists.h"

/**
 * insert_node - inserts a node in a sorted listint_t list
 * @head: the starting node
 * @number: the node to be added
 * Return: returns an address to the add new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new;

	current = *head;
	prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (current != NULL)
	{
		if (current->n > number)
		{
			new->next = current;
			if (prev == NULL)
			{
				*head = new;
			}
			else
				prev->next = new;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new;
	return (new);
}

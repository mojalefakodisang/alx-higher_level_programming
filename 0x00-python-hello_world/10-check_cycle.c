#include "lists.h"

/**
 * check_cycle - checks if the listint_t list is a cycle
 * @list: list to be checked for cycles
 * Return: returns 0  if there are no cycles else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *check;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	check = current->next;
	while (current != NULL && check->next != NULL && check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}

	return (0);
}

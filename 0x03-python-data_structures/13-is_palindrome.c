#include "lists.h"
#include <stdio.h>
void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *mdl, int len);

/**
 * is_palindrome - Verify if a bound list is a palindrome..
 * @head: Hover over the first node in the listint_t list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len;
	int i;
	listint_t *tmp;
	listint_t *mdl;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	mdl = *head;

	for (len = 0; tmp != NULL; len++)
		tmp = tmp->next;

	len = len / 2;

	for (i = 1; i < len; i++)
		mdl = mdl->next;
	if (len % 2 != 0 && len != 1)
	{
		mdl = mdl->next;
		len = len - 1;
	}
	reverse(&mdl);
	i = compare_lists(*head, mdl, len);

	return (i);
}

/**
 * compare_lists - Compares two lists.
 * @head: Point to the Head node.
 * @mdl: Points to the mdl node.
 * @len: length of the lists.
 * Return: If the lists are the same 1. Otherwise 0.
 */
int compare_lists(listint_t *head, listint_t *mdl, int len)
{
	int i;

	if (head == NULL || mdl == NULL)
		return (1);
	i = 0;
	while (i < len)
	{
		if (head->n != mdl->n)
			return (0);
		head = head->next;
		mdl = mdl->next;
		i++;
	}
	return (1);
}

/**
 * reverse - Reverses a linked list.
 * @head: Pointer to the pointer of the head of a linked list.
 */
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

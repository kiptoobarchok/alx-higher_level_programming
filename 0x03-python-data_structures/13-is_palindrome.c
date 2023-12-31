#include "lists.h"

/**
  *rev_listint - function to reverse a list
  *@head: pointer to first node
  *Return: ptr to first node in new list
  */

void rev_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}

/**
  *is_palindrome - function to check if list is palindrome
  *@head: ptr to the first node
  *Return: 1 if yes else 0
  */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}

		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}

		slow = slow->next;
	}

	rev_listint(&dup);

		while (dup && temp)
		{
			if (temp->n == dup->n)
			{
				dup = dup->next;
				temp = temp->next;
			}
			else
				return (0);
		}

		if (!dup)
			return (1);

		return (0);
}

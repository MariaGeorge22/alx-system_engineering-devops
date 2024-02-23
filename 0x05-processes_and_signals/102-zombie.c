#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - waiting
 *
 * Waits forever
 *
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - program
 *
 * creates 5 zombie processes.
 *
 * Return: 0 (Success)
 */

int main(void)
{
	pid_t child;
	size_t i = 0;
	int status;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child < 0)
		{
			perror("fork");
			exit(1);
		}
		if (child == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child);
	}

	infinite_while();

	wait(&status);
	return (0);
}
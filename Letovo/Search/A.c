#include <stdio.h>
#include <stdlib.h>

int compareints (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int values[] = {};
malloc_size = 100
word[i] = malloc(malloc_size * sizeof(char));
scanf("%s", &word[i]);

int main ()
{
  int * pItem;
  int key = 40;
  pItem = (int*) bsearch (&key, values, 6, sizeof (int), compareints);
  if (pItem!=NULL)
    printf ("YES\n");
  else
    printf ("NO\n");
  return 0;
}

#define _GNU_SOURCE
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <string.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int init = 0;
char * my_strfry (char *string, int pid, int ts)
{
  /* static int init; */
  static struct random_data rdata;

  if (!init)
    {
      /* printf("initializing\n"); */
      static char state[32];
      rdata.state = NULL;
      initstate_r(ts ^ pid, state, sizeof (state), &rdata);
      init = 1;
    }

  size_t len = strlen(string);
  if (len > 0)
    for (size_t i = 0; i < len - 1; ++i)
      {
	int32_t j;
	random_r (&rdata, &j);
	j = j % (len - i) + i;

	char c = string[i];
	string[i] = string[j];
	string[j] = c;
      }

  return string;
}

int main(int argc, char *argv[])
{
    int pid = atoi(argv[1]);
    int ts = atoi(argv[2]);
    char str[100]; 
    while (1) {
        scanf("%[^\n]%*c", str); 
        printf("%s\n", my_strfry(str, pid, ts)); 
    }

    return 0;
}

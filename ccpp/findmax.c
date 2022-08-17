#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
  FILE *fp;
  fp = fopen(argv[1], "rt");

  long n, max = 0;
  while(fscanf(fp, "%ld,", &n) != EOF) {
    if (n>max) max = n;
  }
  fclose(fp);

  printf("%ld", max);

  // FILE *fp;
  // srand(time(NULL));
  // int n = atoi(argv[2]);
  // fp = fopen(argv[1], "w+");
  // int i;
  // for(i=0;i<n;i++) {
  //   fprintf(fp, "%d,", rand());
  // }
  // fclose(fp);

  return 0;
}
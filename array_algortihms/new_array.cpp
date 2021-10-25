
#include<iostream>

using namespace std;

int main()
{
   int c1 = 0, c2 = 0;

   /* FIRST */
   for(int i=0; ++c1&&i<10; i++)
      for(int j=0; ++c1&&j<100;j++);
     //do something

   /* SECOND */
   for(int i=0; ++c2&&i<100; i++)
      for(int j=0; ++c2&&j<10; j++);
      //do something

   cout << " Count fot FIRST  " <<c1 << endl;
   cout << " Count fot SECOND  " <<c2 << endl;
   getchar();
   return 0;
}

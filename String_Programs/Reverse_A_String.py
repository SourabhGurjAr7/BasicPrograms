'''
#Simple logic used in other language like java:

import java.io.*;
import java.util.Scanner;

class GFG {
    public static void main (String[] args) {

        String str= "Geeks", nstr="";
        char ch;

      System.out.print("Original word: ");
      System.out.println("Geeks"); //Example word

      for (int i=0; i<str.length(); i++)
      {
        ch= str.charAt(i);  //extracts each character
        nstr= ch+nstr;  //adds each character in front of the existing string
      }
      System.out.println("Reversed word: "+ nstr);
    }
}


#In Python ,it is much more simpler
#Method1
str="olleh"
for i in range(len(str)-1,-1,-1):
    print(str[i],end=" ")

'''

#Method2
str="olleh"
rev=""
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
print(rev)

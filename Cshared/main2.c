#include <stdio.h>

    char hex_to_ascii(char);
    char byte_to_ascii(char);
int main()
{
    int input;
    int capture;
    int capture1;
    int out_high;
    int out_low;
    char high;
    char low;
   int out_high1;
    int out_low1;
    int high1;
    char low1;
    char high_3;
    char high_2;
    char high_1;
    char high_0;

    
    
    int i;
    int j=0;
	FILE *fpr;
    FILE *fpw;
    int value[3];
    char filename[256];
    char outfile[256];
    
    //printf("enter file to modify   ");
    //gets(filename);
    //printf("enter file to save   ");
    //gets(outfile);
    fpr=fopen("Iwalk_pt_test2.txt", "rb");

// added to get file length
    fseek(fpr, 0L, SEEK_END);
    long int res = ftell(fpr);
    fseek(fpr, 0L, SEEK_SET);
 //
    fpw=fopen("Iwalk2.txt", "wb");
    input = 0;
 //  while(input != EOF)
    while(res >= 0)
    {
       
        
        
     for(i=0;i<2;i++)
      {
        capture = fgetc(fpr);  //get low value
         res--;
        capture1 = fgetc(fpr);  //get high value
        res--;
      //convert from hex to interger value is stored in high1
        value[1] = capture1/16; 
        high1 = value[1]*4096;
 //        high1 = hex_to_ascii(value[1]);
         value[0] = capture1%16;
         high1 += value[0]*256;
 //       low1 = hex_to_ascii(value[0]);

        value[1] = capture/16; 
 //        high = hex_to_ascii(value[1]);
        high1 += value[1]*16;
         value[0] = capture%16;
//        low = hex_to_ascii(value[0]);
        high1 += value[0];
  //now convert high1 to ascii
         value[0] = high1/1000;                  //1000s value
         high_3 = hex_to_ascii(value[0]);
         value[2] = (high1-(value[0]*1000));     
         value[0] = value[2]/100;
         high_2 = hex_to_ascii(value[0]);    //100s value  
         value[1] = (value[2] - (value[0]*100));
         value[2] = value[1]/10;
         high_1 = hex_to_ascii(value[2]);      //10s value
         value[0] = (value[1] - (value[2]*10));
         
         high_0 = hex_to_ascii(value[0]);      //1s value
  
         fputc(high_3,fpw);
         fputc(high_2,fpw);
         fputc(high_1,fpw);
         fputc(high_0,fpw);



        fputc(0x0D,fpw);      
       }
   //   fputc(0x09,fpw);
  //    j++;
  //    if(j > 1000)
 //      {
        
  //      j =0;
      }
     
    
    fclose(fpr); 
    fclose(fpw);
}


char byte_to_ascii(char b)
{
    char low_b;
    char high_b;
    char high_bits;
    char low_bits;
    char byte_out;
    low_bits = (b & 0x0F);
    low_b = hex_to_ascii(low_bits);
    high_bits = (b & 0xF0);
    high_b = hex_to_ascii(high_bits);
    byte_out = (high_b + low_b);
    return(byte_out);
    
}


char hex_to_ascii(char c)
{
    char ascci;
 if(c ==0)
 {
     ascci = 0x30;
 }
 else if(c==1)
 {
     ascci = 0x31;
 }
  else if(c==2)
 {
     ascci = 0x32;
 }
  else if(c==3)
 {
     ascci = 0x33;
 }
  else if(c==4)
 {
     ascci = 0x34;
 }
   else if(c==5)
 {
     ascci = 0x35;
 }
  else if(c==6)
 {
     ascci = 0x36;
 }
  else if(c==7)
 {
     ascci = 0x37;
 }
   else if(c==8)
 {
     ascci = 0x38;
 }
  else if(c==9)
 {
     ascci = 0x39;
 }
  else if(c==10)
 {
     ascci = 0x41;
 }
   else if(c==11)
 {
     ascci = 0x42;
 }
  else if(c==12)
 {
     ascci = 0x43;
 }
  else if(c==13)
 {
     ascci = 0x44;
 }
   else if(c==14)
 {
     ascci = 0x45;
 }
  else if(c==15)
 {
     ascci = 0x46;
 }
   
 return (ascci);
}

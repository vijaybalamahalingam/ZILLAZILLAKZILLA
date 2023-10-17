import java.util.Scanner;
public class SumDigits
{
    public static void main(String[]args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number");
        int num=sc.nextInt();
        int copy=num,digit,sum=0;
        while(copy>0)
        {
            digit=copy%10;
            sum+=digit;
            copy/=10;
        }
        System.out.println("The sum of digits="+sum);
    }
}
        












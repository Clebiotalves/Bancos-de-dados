import java.util.Scanner;

public class Program {
    public static void main (String[] args) {
        Scanner reader = new Scanner(System.in);
        float entry = reader.nextFloat();
        float days = entry /=2;


        for (int i = 0; i < entry ; i++)
            if(entry > 0)
                days ++;

                System.out.println(entry * days);
    }
}



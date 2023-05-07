import java.rmi.*;
import java.rmi.server.*;

public class SampleClient  
{
   public static void main(String[]  args)
   {
      // set the security manager for the client
     // System.setSecurityManager(new RMISecurityManager());
int a=Integer.parseInt(args[0]);
int b=Integer.parseInt(args[1]);

      //get the remote object from the registry
      try
        {
          System.out.println("Security Manager loaded");
          String url = "//localhost/SAMPLE-SERVER";

          SampleServer remoteObject = (SampleServer)Naming.lookup(url);
          System.out.println("Got remote object");

          System.out.println(" GCD IS = " + remoteObject.gcd(a,b) );
		  System.out.println(" LCM IS = " + remoteObject.lcm(a,b) );
		  
        }
        catch (RemoteException exc) {
          System.out.println("Error in lookup: " + exc.toString()); }
        catch (java.net.MalformedURLException exc) {
          System.out.println("Malformed URL: " + exc.toString());   }
        catch (java.rmi.NotBoundException exc)  {
          System.out.println("NotBound: " + exc.toString());
        }

   }
}

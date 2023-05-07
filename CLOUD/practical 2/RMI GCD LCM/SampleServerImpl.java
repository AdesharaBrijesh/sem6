import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;

public class SampleServerImpl extends UnicastRemoteObject
                             implements SampleServer
{
  SampleServerImpl() throws RemoteException
  {
     super();
  }
  public static void main(String args[])
  {
      try
      {
      //  System.setSecurityManager(new RMISecurityManager());  
      //set the security manager

        //create a local instance of the object
        SampleServerImpl Server = new SampleServerImpl();

        //put the local instance in the registry
        Naming.rebind("SAMPLE-SERVER" , Server);

        System.out.println("Server waiting.....");
      }
      catch (java.net.MalformedURLException me)       {
        System.out.println("Malformed URL: " + me.toString());   }
      catch (RemoteException re)  {
         System.out.println("Remote exception: " + re.toString());  }
  }
  public int gcd(int a,int b) throws RemoteException
  {
	  
	  
	  int gcd=1;
        for(int i = 1; i <= a && i <= b; i++)
        {
            if(a%i==0 && b%i==0)
                gcd = i;
        }
        return gcd;
    }
     public int lcm(int a,int b) throws RemoteException
  {
	  
	  
	  int gcd=1;
        for(int i = 1; i <= a && i <= b; i++)
        {
            if(a%i==0 && b%i==0)
                gcd = i;
        }
        int lcm= (a*b)/gcd;
        return lcm;
    }
    
  }


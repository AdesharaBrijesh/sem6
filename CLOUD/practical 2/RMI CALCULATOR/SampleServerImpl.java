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
  public int sum(int a,int b) throws RemoteException
  {
     return a + b;
  }
  public int sub(int a,int b) throws RemoteException
  {
     return a - b;
  }
  public int mul(int a,int b) throws RemoteException
  {
     return a * b;
  }
  public int div(int a,int b) throws RemoteException
  {
     return a / b;
  }
  public int mod(int a,int b) throws RemoteException
  {
     return a % b;
  }
}
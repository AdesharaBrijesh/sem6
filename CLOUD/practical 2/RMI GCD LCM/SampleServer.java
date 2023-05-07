import java.rmi.*;

public interface SampleServer extends Remote
{
  public int gcd(int a,int b) throws RemoteException;
  public int lcm(int a,int b) throws RemoteException;
}

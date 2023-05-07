import java.rmi.*;

public interface SampleServer extends Remote
{
  public int sum(int a,int b) throws RemoteException;
  public int sub(int a,int b) throws RemoteException;
  public int mul(int a,int b) throws RemoteException;
  public int div(int a,int b) throws RemoteException;
  public int mod(int a,int b) throws RemoteException;
}

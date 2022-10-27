using System.Diagnostics;
using System.IO.Pipes;
using System.Text;
using System.Web;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var t = new Producer();
            //Thread.Sleep(2000);
            //Task.Run(() => RunPythonProcess());
            Thread.Sleep(10000);
            Console.WriteLine("Infrastructure established");
            while (true)
            {
                string s = Console.ReadLine();
                t.PostToPipe(s);
                Console.WriteLine(s);
            }
            

        }

        static void RunPythonProcess()
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.CreateNoWindow = false;
            startInfo.UseShellExecute = false;
            startInfo.FileName = @"C:\Users\H261112\source\repos\LatestLAS\PythonCSharpLAS\PyClient\dist\pythonclient.exe";
            startInfo.WindowStyle = ProcessWindowStyle.Hidden;
            //startInfo.Arguments = "sregergergrewgergergergregewr";
            int result;
            try
            {
                // Start the process with the info we specified.
                // Call WaitForExit and then the using statement will close.
                using (Process exeProcess = Process.Start(startInfo))
                {
                    exeProcess.WaitForExit();
                    result = exeProcess.ExitCode;
                }

                Console.WriteLine("*********** " + result);
            }
            catch
            {
                // Log error.
            }
        }
        
    }
}
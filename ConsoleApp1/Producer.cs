using System;
using System.Collections.Generic;
using System.IO.Pipes;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Producer
    {
        private readonly object _lock = new object();
        private readonly Queue<string> _queue = new Queue<string>();
        private readonly AutoResetEvent _signal = new AutoResetEvent(false);
        delegate void StringArgReturningVoidDelegate(string text, Label L);
        private static NamedPipeServerStream server;
        private BinaryReader br;
        private BinaryWriter bw;


         public Producer()
        {
            server = new NamedPipeServerStream("testing");
            br = new BinaryReader(server);
            bw = new BinaryWriter(server);
            new Thread(new ThreadStart(ProducerThread)).Start();
          

        }


        void ProducerThread()
        {
            while (true)
            {
                _signal.WaitOne();
                string item = string.Empty;
                do
                {
                    item = string.Empty;
                    lock (_lock)
                    {
                        if (_queue.Count > 0)
                        {
                            item = _queue.Dequeue();
                            
                        }
                    }

                    if (item != string.Empty)
                    {

                        try
                        {

                            if (server != null && !server.IsConnected)
                                server.WaitForConnection();

                            if (server != null && server.IsConnected)
                            {
                                var str = new string(item.ToString().ToArray());

                                var buf = Encoding.ASCII.GetBytes(str);
                                bw.Write((uint)buf.Length);
                                bw.Write(buf);
                            }
                            if (server != null && server.IsConnected)
                            {
                                var len = (int)br.ReadUInt32();
                                var str = new string(br.ReadChars(len));
                               
                            }
                        }
                        catch (Exception EX)
                        {
                           
                        }
                    }
                }
                while (item != string.Empty);
            }
        }

        public void PostToPipe(string name)
        {

            lock (_lock)
            {

                _queue.Enqueue(name);

            }
            _signal.Set();
        }


    }
}

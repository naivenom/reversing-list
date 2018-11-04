using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ultimate_Minesweeper
{
    class Program
    {
        static void Main(string[] args)
        {
            uint grid = 30u; //VALLOC_NODE_LIMIT
            uint VALLOC_TYPE_HEADER_PAGE = 4294966400u;
            uint VALLOC_TYPE_HEADER_POOL = 4294966657u;
            uint VALLOC_TYPE_HEADER_RESERVED = 4294967026u;
            uint DeriveVallocType(uint r, uint c)
            {
                return ~(r * grid + c);
            }
            uint[] VALLOC_TYPES = new uint[3]
            {
            VALLOC_TYPE_HEADER_PAGE,
            VALLOC_TYPE_HEADER_POOL,
            VALLOC_TYPE_HEADER_RESERVED
            };
            for (uint num = 0u; num < grid; num += 1u)
            {
                for (uint num2 = 0u; num2 < grid; num2 += 1u)
                {
                    bool flag = true;
                    uint row = num + 1u;
                    uint colm = num2 + 1u;
                    if (VALLOC_TYPES.Contains(DeriveVallocType(row, colm)))
                    {
                        flag = false;
                        Console.WriteLine("FLAG--> Row:" + row + " Column:" + colm);
                        Console.ReadLine();
                    }
                }
            }
        }
    }
}

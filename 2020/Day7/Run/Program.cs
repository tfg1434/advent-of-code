using System.Reflection;
using Day7;

Console.WriteLine($"Silver: { Silver.Run(File.ReadAllText(@"in.txt")) }");
Console.WriteLine($"Gold: { Gold.Run(File.ReadAllText(@"in.txt")) }");

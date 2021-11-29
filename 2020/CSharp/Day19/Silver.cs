using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day19;

interface IRule { }

record struct Constant(char Symbol) : IRule;

record struct RuleRef(int Ref) : IRule;

public static class Silver {
    public static int Run(string input) {
        Map<int, IEnumerable<IEnumerable<IRule>>> rules = ParseRules(input);
        



        return 0;
    }
    
    private static Map<int, IEnumerable<IEnumerable<IRule>>> ParseRules(string input) 
        => input.Split(Environment.NewLine).Map(line => {
            string[] split = line.Split(": ");
            int id = int.Parse(split[0]);
            string[] parts = split[1].Split(" | ");

            return (id, parts.Map(side =>
                side.Split(' ').Map<string, IRule>(part =>
                    part.StartsWith('"') ? new Constant(part[1]) : new RuleRef(int.Parse(part)))));


        }).ToMap();
    }
}
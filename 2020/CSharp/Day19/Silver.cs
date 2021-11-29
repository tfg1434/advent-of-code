using System.Data;
using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day19;

interface IRule { }

record struct Constant(char Symbol) : IRule;

record struct RuleRef(int Ref) : IRule;

public static class Silver {
    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        IEnumerable<string> rulesRaw = lines.TakeWhile(line => line != "");
        IEnumerable<string> messages = lines.SkipWhile(line => line != "").Skip(1);
        IEnumerable<IRule> rules = rulesRaw.Map(ParseRule);
        
        
        
        return 0;
    }
    
    private static Map<int, Lst<IRule>> ParseRules(string input) {
        return input.Split(Environment.NewLine).Map(line => {
            string[] split = line.Split(": ");
            int id = int.Parse(split[0]);
            

        });
    }


    }
}
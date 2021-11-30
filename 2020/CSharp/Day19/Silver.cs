using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day19;

interface IRule { }

record struct Constant(char Symbol) : IRule;

record struct RuleRef(int Ref) : IRule;

public static class Silver {
    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        Map<int, Lst<Lst<IRule>>> rules = 
            ParseRules(lines.TakeWhile(line => line != ""));
        IEnumerable<string> messages = lines.SkipWhile(line => line != "").Skip(1);
        
        



        return 0;
    }
    
    private static Lst<int> MatchingRules(Lst<Lst<IRule>> rules, int position, int id) {
        //orRule: inner Lst
        //rule: inner inner IRule

        rules[id].Map(orRule =>  {
            var positions = List(position);

            orRule.ForEach(rule => {
                positions = positions.Map(idx =>
                    rule switch {
                        Constant @const when 
                    })
            });
        });

        return default;
    }
    
    private static Map<int, Lst<Lst<IRule>>> ParseRules(IEnumerable<string> lines) 
        => lines.Map(line => {
            string[] split = line.Split(": ");
            int id = int.Parse(split[0]);
            string[] parts = split[1].Split(" | ");

            return (id, parts.Map(side =>
                side.Split(' ').Map<string, IRule>(part =>
                    part.StartsWith('"') ? new Constant(part[1]) : new RuleRef(int.Parse(part))).ToLst()).ToLst());
            
        }).ToMap();
}
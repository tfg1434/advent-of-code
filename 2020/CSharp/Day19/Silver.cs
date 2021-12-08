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
    
    private static Lst<int> MatchingRules(Map<int, Lst<Lst<IRule>>> rules, int position, int id) {
        //orRule: inner Lst
        //rule: inner inner IRule

        rules[id].Map(orRule =>  {
            var positions = List(position);
        
            orRule.ForEach(rule => { //one rule must match for message to be valid
                positions = positions.Map<int, Lst<int>>(idx =>
                    rule switch {
                        Constant @const when idx == @const.Symbol => List(idx + 1),
                        RuleRef @ref => MatchingRules(rules, @ref.Ref, idx),
                        _ => null,
                    }
                ).Flatten();
            });
        
            return positions;
        });
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
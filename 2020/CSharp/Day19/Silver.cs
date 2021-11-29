using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day19;

abstract record class Rule() {
    public abstract bool IsMatch(string input);
}

record class ConstantRule(string Match) : Rule {
    public override bool IsMatch(string input) 
        => input == Match;
}

record class MultiRule(Lst<Rule> Rules) : Rule {
    public override bool IsMatch(string input) 
        => Rules.All(r => r.IsMatch(input));
}

record class OrRule(Lst<Rule> First, Lst<Rule> Second) : Rule {
    public override bool IsMatch(string input) 
        => First.All(r => r.IsMatch(input)) || Second.All(r => r.IsMatch(input));
}

public static class Silver {
    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        IEnumerable<string> rules = lines.TakeWhile(line => line != "");
        IEnumerable<string> messages = lines.SkipWhile(line => line != "").Skip(1);

        return 0;
    }
}
using System.Text.RegularExpressions;
using FunctionalSharp;
using static FunctionalSharp.F;
using BagName = System.String;

namespace Day7;

readonly record struct Bag(BagName Name, int Count);

public static class Gold {
    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        var map = Map<BagName, Lst<Bag>>();
        
        foreach (string line in lines) {
            BagName bag = Regex.Match(line, @"^([a-z]+ [a-z]+)").Captures[0].Value;
            MatchCollection matchesContains = Regex.Matches(line, @"([0-9]+) ([a-z]+ [a-z]+)");
            var contains = Lst<Bag>.Empty;

            foreach (Match match in matchesContains)
                contains = contains.Append(new Bag(match.Groups[2].Value, int.Parse(match.Groups[1].Value)));

            map = map.Append(bag, contains);
        }

        return HoldingThis(map, "shiny gold");
    }
    
    static int HoldingThis(Map<BagName, Lst<Bag>> map, BagName bag) {
        int count = 0;
        
        foreach (Bag subBag in map[bag]) {
            count += subBag.Count;
            count += HoldingThis(map, subBag.Name) * subBag.Count;
        }

        return count;
    }
}
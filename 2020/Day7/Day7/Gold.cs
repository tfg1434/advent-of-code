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
            GroupCollection capturesContain = Regex.Matches(line, @"([0-9]+) ([a-z]+ [a-z]+)").Groups;
            var contains = Lst<Bag>.Empty;
            
            for (int i = 1; i < capturesContain.Count; i += 2)
                contains = contains.Append(new Bag(capturesContain[i + 1].Value, int.Parse(capturesContain[i].Value)));


            map = map.Append(bag, contains);
        }


        return HoldingThis(map, "shiny gold");


    }
    
    static int HoldingThis(Map<BagName, Lst<Bag>> map, BagName bag) {
        int count = 0;

        //aha parser broken see map["dark olive"]
        foreach (Bag subBag in map[bag]) {
            count += subBag.Count;
            count += HoldingThis(map, subBag.Name) * subBag.Count;
            var a = 4;
        }

        return count;
    }
}
using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day19;

public static class Silver {
    public static int Run(string input) {
        var holds = Map<string, Lst<string>>();
        string[] lines = input.Split(Environment.NewLine);
        
        foreach (string line in lines) {
            string[] split = line.Split(" ");
            string holder = string.Join(" ", split[..2]);

            (Lst<string> List, string Word) seed = (Lst<string>.Empty, "");
            var holding = split[5..]
                .Where((_, i) => i % 4 is 0 or 1)
                .Aggregate(seed, (acc, s) => {

                    if (acc.Word == "")
                        return acc with { Word = s };

                    return (acc.List.Append(string.Join(" ", acc.Word, s)), "");
                })
                .List;

            holds = holds.Append(holder, holding);
        }

        int count = 0;
        
        foreach (string bag in holds.Keys) {
            if (CountGoldBags(holds, bag) != 0)
                count++;
        }

        return count;
    }

    private static int CountGoldBags(Map<string, Lst<string>> map, string bag) {
        if (bag == "other bags.") return 0;
        // Lst<string> bags = map[bag];
        //
        // return bags.Count switch {
        //     0 => 0,
        //     _ => bags.Aggregate(0, (acc, subBag) => {
        //         int count = subBag == "shiny gold" ? 1 : 0;
        //         
        //         return acc + count + CountGoldBags(map, subBag);
        //     }),
        // };

        int count = 0;
        Lst<string> bags = map[bag];
        
        if (bags.Count == 0)
            return 0;
        
        foreach (string subBag in bags) {
            if (subBag == "shiny gold")
                count++;
        
            count += CountGoldBags(map, subBag);
        }
        
        return count;
    }
}
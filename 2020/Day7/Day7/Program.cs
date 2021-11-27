using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day7; 

static class Program {
    public static int Silver(string input) {
        var holds = Map<string, Lst<string>>();

        string[] lines = input.Split(Environment.NewLine);
        foreach (string line in lines) {
            string[] split = line.Split(" ");

            string holder = string.Join(" ", line[..2]);
            var holding = Lst<string>.Empty;

            var holdsRaw = split[5..]
                .Where((_, i) => i % 4 is 0 or 1)
                .Aggregate("", (acc, s) => {

                    if (acc == "")
                        return acc + s;

                    holding = holding.Append(string.Join(" ", acc, s));

                    return "";
                });

            holds = holds.Append(holder, holding);
        }

        return 0;
    }
}
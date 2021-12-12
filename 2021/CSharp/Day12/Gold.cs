﻿using FunctionalSharp;
using static FunctionalSharp.F;

namespace Day12;

public static class Gold {
    public static int Run(string input) {
        Dictionary<string, List<string>> d = new();
        string[] lines = input.Split(Environment.NewLine);
        foreach (string line in lines) {
            string[] split = line.Split('-');

            if (d.TryGetValue(split[0], out List<string> list))
                list.Add(split[1]);
            else
                d[split[0]] = new() { split[1] };
            
            if (d.TryGetValue(split[1], out list))
                list.Add(split[0]);
            else
                d[split[1]] = new() { split[0] };
        }

        (string Curr, Lst<string> Visited, string? Twice) seed = ("start", List("start"), null);
        int ans = 0;
        LinkedList<(string Curr, Lst<string> Visited, string? Twice)> queue = new(new[] { seed });
        while (queue.Any()) {
            (string curr, Lst<string> visited, string? twice) = queue.First();
            queue.RemoveFirst();

            if (curr == "end") {
                ans++;
                
                continue;
            }
            
            foreach (var x in d[curr]) {
                if (!visited.Contains(x)) {
                    queue.AddLast((x, x == x.ToLower() ? visited.Append(x) : visited, twice));
                } else if (twice is null && visited.Contains(x) && x is not "start" or "end")
                    queue.AddLast((x, visited,  x));
            }
        }

        return ans;
    }
}


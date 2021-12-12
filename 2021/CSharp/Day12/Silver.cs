using FunctionalSharp;

namespace Day12;

public static class Silver {
    private record Node(List<Node> Children, string Value);

    private static Node GenTree(Dictionary<string, List<string>> dict, string key = "start") {
        List<string> GetOrEmpty(string key) => dict.TryGetValue(key, out var list) ? list : new();

        var _ = GetOrEmpty(key);
        List<Node> children = _.Map(x => GenTree(/*new() { [x] = GetOrEmpty(x) }*/dict, x)).ToList();
        
        return new Node(children, key);
    }

    public static int Run(string input) {
        Dictionary<string, List<string>> d = new();
        string[] lines = input.Split(Environment.NewLine);
        foreach (string line in lines) {
            string[] split = line.Split('-');
            if (d.TryGetValue(split[0], out List<string> value)) {
                value.Add(split[1]);
            } else {
                d.Add(split[0], new() { split[1] });
            }
        }

        Node tree = GenTree(d);
        
        (string Curr, List<string> Visited) seed = ("start", new() { "start" });
        int ans = 0;
        LinkedList<(string Curr, List<string> Visited)> queue = new(new[] { seed });
        while (queue.Any()) {
            (string curr, List<string> visited) = queue.Last();
            queue.RemoveLast();

            if (curr == "end") {
                ans++;
                
                continue;
            }
            
            foreach (var x in tree[curr]) {
                
            }
        }
        
        //Node root = new(d["start"], null);
        
        return default;
    }
}

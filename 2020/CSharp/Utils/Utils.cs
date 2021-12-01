using System.Diagnostics.Contracts;

namespace Utils;

public static class Utils {
    [Pure]
    public static IList<IList<T>> Permutations<T>(IList<T> items) {
        List<IList<T>> list = new();
    
        return DoPermutations(items, 0, items.Count - 1, list);
    }
    
    private static IList<IList<T>> DoPermutations<T>(IList<T> items, int start, int end, IList<IList<T>> list) {
        if (start == end)
            list.Add(new List<T>(items));
        else {
            for (int i = start; i <= end; i++) {
                (items[start], items[i]) = (items[i], items[start]);
                DoPermutations(items, start + 1, end, list);
                (items[start], items[i]) = (items[i], items[start]);
            }
        }
    
        return list;
    }

    public static IEnumerable<List<T>> Combinations<T>(this IEnumerable<T> items, int r) {
        IEnumerable<T> enumerable = items as T[] ?? items.ToArray();
        int n = enumerable.Count();

        if (r > n) yield break;

        T[] pool = enumerable.ToArray();
        int[] indices = Enumerable.Range(0, r).ToArray();

        yield return indices.Select(x => pool[x]).ToList();

        while (true) {
            int i = indices.Length - 1;
            while (i >= 0 && indices[i] == i + n - r)
                i -= 1;

            if (i < 0) yield break;

            indices[i] += 1;

            for (int j = i + 1; j < r; j += 1)
                indices[j] = indices[j - 1] + 1;

            yield return indices.Select(x => pool[x]).ToList();
        }
    }
    
    // private static IEnumerable<IEnumerable<T>> DoPermutations<T>(IEnumerable<T> items, int length) {
    //     if (length == 1) return items.Select(t => new[] { t });
    //
    //     return DoPermutations(items, length - 1)
    //         .SelectMany(t => items.Where(o => !t.Contains(o)),
    //             (t1, t2) => t1.Concat(new[] { t2 }));
    // }
}
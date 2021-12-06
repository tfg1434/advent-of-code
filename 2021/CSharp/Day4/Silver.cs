using System.Text.RegularExpressions;
using FunctionalSharp;

namespace Day4;

public static class Silver {
    private readonly record struct BoardSquare(int Number, bool Marked);

    private static Func<bool, int, BoardSquare> OfBoardSquare
        => (marked, number) => new(number, marked);

    private static bool CheckForMatch(List<List<BoardSquare>> board)
        => Enumerable.Range(0, 5)
               .Map(y => board[y]
                   .All(square => square.Marked))
               .Any(b => b) || 
           //board[0][0] [1][0] [2][0] ... [0][1]
           Enumerable.Range(0, 5)
               .Map(x => Enumerable.Range(0, 5)
                   .Map(y => board[y][x])
                   .All(square => square.Marked))
               .Any(b => b);

    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        IEnumerable<int> numbers = lines[0].Split(',').Map(int.Parse).ToLst();
        int boardsCount = (lines.Length - 1) / 6;
        List<List<List<BoardSquare>>> boards = new();

        for (int i = 2; i < boardsCount * 6 + 2; i += 6) {
            boards.Add(lines[i..(i + 5)]
                .Map(line => Regex.Matches(line, @"([0-9]+)").Map(match => match.Groups[0].Value)
                    .Map(n => OfBoardSquare(false, int.Parse(n))).ToList()).ToList());
        }

        foreach (int n in numbers) {
            foreach (List<List<BoardSquare>> board in boards) {
                foreach (List<BoardSquare> ys in board) {
                    for (int x = 0; x < ys.Count; x++) {
                        if (ys[x].Number == n) {
                            ys[x] = OfBoardSquare(true, ys[x].Number);
                        }
                    }
                }

                if (CheckForMatch(board))
                    return Enumerable.Range(0, 5)
                        .Map(y => board[y].Sum(square => !square.Marked ? square.Number : 0)).Sum() * n;
            }
        }

        return default;
    }
}

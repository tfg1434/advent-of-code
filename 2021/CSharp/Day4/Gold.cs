using System.Text.RegularExpressions;
using FunctionalSharp;

namespace Day4;

public static class Gold {
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
            for (int i = 0; i < boards.Count; i++) {
                for (int j = 0; j < boards[i].Count; j++) {
                    for (int k = 0; k < boards[i][j].Count; k++) {
                        if (boards[i][j][k].Number == n) {
                            boards[i][j][k] = OfBoardSquare(true, boards[i][j][k].Number);
                        }
                    }
                }

                if (!CheckForMatch(boards[i])) continue;

                if (boards.Count == 1)
                    return Enumerable.Range(0, 5)
                        .Map(y => boards[i][y].Sum(square => !square.Marked ? square.Number : 0)).Sum() * n;
                
                boards.RemoveAt(i);
                i--;
            }
        }

        return default;
    }
}


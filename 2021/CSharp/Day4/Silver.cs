using System.Text.RegularExpressions;
using FunctionalSharp;

namespace Day4;

public static class Silver {
    record struct BoardSquare(int Number, bool Marked);

    static Func<bool, int, BoardSquare> OfBoardSquare
        => (marked, number)  => new(number, marked);

    static bool CheckForMatch(List<List<BoardSquare>> board) {
        return //board[0][0] [1][0] [2][0] ... [0][1]
            Enumerable.Range(0, 4).Map(y => board[y].All(square => square.Marked)).Any() ||
            Enumerable.Range(0, 4).Map(x => Enumerable.Range(0, 4).Map(y => board[y][x]).All(square => square.Marked)).Any();
        
    }
    
    public static int Run(string input) {
        string[] lines = input.Split(Environment.NewLine);
        IEnumerable<int> numbers = lines[0].Split(',').Map(int.Parse).ToLst();
        int boardsCount = (lines.Length - 1) / 6;
        List<List<List<BoardSquare>>> boards = new();//new int[boardsCount][Board];

        for (int i = 2; i < boardsCount * 6 + 2; i += 6) {
            boards.Add(lines[i..(i + 5)]
                .Map(line => Regex.Matches(line, @"([0-9]+)").Map(match => match.Groups[0].Value)
                    .Map(n => OfBoardSquare(false, int.Parse(n))).ToList()).ToList());
        }

        foreach (int n in numbers) {
            foreach (List<List<BoardSquare>> board in boards) {
                foreach (List<BoardSquare> row in board) {
                    foreach (BoardSquare square in row) {
                        //to mutate square
                        BoardSquare boardSquare = square;
                        
                        if (boardSquare.Number == n) {
                            boardSquare.Marked = true;
                        }
                    }
                }

                if (CheckForMatch(board)) {
                    int b = 5;
                }
            }
        }
        
        return default;
    }
}

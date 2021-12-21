int[] ParseLine(string line)
{
    return line.ToCharArray().Select(c => c == '1' ? 1 : 0).ToArray();
}

int[][] ReadBoard(IEnumerator<string> fileStream)
{
    var board = new int[5][];
    for (var i = 0; i < 5; i++)
    {
        board[i] = fileStream.Current.Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();

        fileStream.MoveNext();
    }

    return board;
}

IEnumerable<int[][]> ReadBoards(IEnumerator<string> fileStream)
{
    fileStream.MoveNext();
    fileStream.MoveNext();

    while (fileStream.Current != null)
    {
        yield return ReadBoard(fileStream);
        fileStream.MoveNext();
    }
}

(int[], IEnumerable<int[][]>) ReadData(string filename)
{
    var fileStream = File.ReadLines(filename).GetEnumerator();
    fileStream.MoveNext();

    var numbers = fileStream.Current.Split(",").Select(int.Parse).ToArray();

    var boards = ReadBoards(fileStream);

    return (numbers, boards);
}

int[][] ComputeScoredBoard(int[][] board, Dictionary<int, int> positionDictionary)
{
    return board.Select(boardLine =>
    {
        return boardLine.Select(bl => positionDictionary[bl]).ToArray();
    }).ToArray();
}

Dictionary<int, int> ComputePositionDictionary(int[] numbers)
{
    var result = new Dictionary<int, int>();
    foreach (var number in numbers)
    {
        result.Add(number, Array.FindIndex(numbers, n => n == number));
    }

    return result;
}

IEnumerable<(int, int[])> GetLinesWithScore(int[][] scoredBoard)
{
    foreach (var line in scoredBoard)
    {
        yield return (line.Max(), line);
    }

    for (var i = 0; i < scoredBoard.Length; i++)
    {
        var vertical = scoredBoard.Select(l => l[i]).ToArray();
        yield return (vertical.Max(), vertical);
    }
}

IEnumerable<int> GetUnmarkedNumbers(int[][] board, int[] usedNumbers)
{
    foreach (var line in board)
    {
        foreach (var number in line)
        {
            if (!usedNumbers.Contains(number))
            {
                yield return number;
            }
        }
    }
}

(int, int) Part1(string filename)
{
    var (numbers, boards) = ReadData(filename);
    var positionDictionary = ComputePositionDictionary(numbers);

    var bestScore = int.MaxValue;
    int[][] winningBoard = null;
    foreach (var board in boards)
    {
        var scoredBoard = ComputeScoredBoard(board, positionDictionary);
        var score = GetLinesWithScore(scoredBoard).Min(a => a.Item1);

        if (bestScore > score)
        {
            bestScore = score;
            winningBoard = board;
        }
    }

    var winningNumber = numbers[bestScore];
    var usedNumbers = numbers.Take(bestScore + 1).ToArray();

    var sumOfUnmarked = GetUnmarkedNumbers(winningBoard, usedNumbers).Sum();

    return (sumOfUnmarked, winningNumber);
}

var (sum1, winningNumber1) = Part1("data.input");

Console.WriteLine($"Result part 1: {sum1} * {winningNumber1}");
Console.WriteLine($"Result part 1 output: {sum1 * winningNumber1}");


(int, int) Part2(string filename)
{
    var (numbers, boards) = ReadData(filename);
    var positionDictionary = ComputePositionDictionary(numbers);

    var bestScore = int.MinValue;
    int[][] winningBoard = null;
    foreach (var board in boards)
    {
        var scoredBoard = ComputeScoredBoard(board, positionDictionary);
        var score = GetLinesWithScore(scoredBoard).Min(a => a.Item1);

        if (bestScore < score)
        {
            bestScore = score;
            winningBoard = board;
        }
    }

    var winningNumber = numbers[bestScore];
    var usedNumbers = numbers.Take(bestScore + 1).ToArray();

    var sumOfUnmarked = GetUnmarkedNumbers(winningBoard, usedNumbers).Sum();

    return (sumOfUnmarked, winningNumber);
}

var (sum2, winningNumber2) = Part2("data.input");

Console.WriteLine($"Result part 2: {sum2} * {winningNumber2}");
Console.WriteLine($"Result part 2 output: {sum2 * winningNumber2}");

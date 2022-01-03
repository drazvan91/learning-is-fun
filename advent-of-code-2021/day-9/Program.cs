IEnumerable<int[]> GetLines(string filename)
{
    return File.ReadLines(filename)
        .Select(line =>
        {
            return line.Select(c => int.Parse(c.ToString())).ToArray();
        }
        );
}

IEnumerable<int[]> GetExtendedLines(string filename)
{
    var emptyLine = new int[120].Select(i => int.MaxValue).ToArray();
    yield return emptyLine;
    foreach (var line in GetLines(filename))
    {
        yield return new int[] { int.MaxValue }.Concat(line).Concat(new int[] { int.MaxValue }).ToArray();
    }
    yield return emptyLine;
}

(int, int) Process(string filename)
{
    // this is fun
    var nextLines = GetExtendedLines(filename).Skip(2);
    var currLines = GetExtendedLines(filename).Skip(1);
    var prevLines = GetExtendedLines(filename);

    var zip = nextLines.Zip(currLines, (a, b) => (a, b)).Zip(prevLines, (d, c) => (d.a, d.b, c));

    var count = 0;
    var sum = 0;
    foreach (var (prev, curr, next) in zip)
    {
        for (int i = 1; i < curr.Length - 1; i++)
        {
            var value = curr[i];
            if (value < prev[i] && value < next[i] && value < curr[i - 1] && value < curr[i + 1])
            {
                count += 1;
                sum += value + 1;
            }
        }
    }

    return (count, sum);
}


Console.WriteLine($"Result 1: {Process("data.input")}");

int MeasureBasin(int[][] basin, int startX, int startY)
{
    int value = basin[startX][startY];
    if (value >= 9)
    {
        return 0;
    }

    basin[startX][startY] = 9;
    return 1 +
        MeasureBasin(basin, startX - 1, startY) +
        MeasureBasin(basin, startX, startY - 1) +
        MeasureBasin(basin, startX, startY + 1) +
        MeasureBasin(basin, startX + 1, startY);
}

IEnumerable<int> GetBasinSizes(string filename)
{
    var basin = GetExtendedLines(filename).ToArray();
    for (int line = 1; line < basin.Length - 1; line++)
    {
        for (int column = 1; column < basin[line].Length - 1; column++)
        {
            int value = basin[line][column];
            if (value < 9)
            {
                int basinSize = MeasureBasin(basin, line, column);
                yield return basinSize;
            }
        }
    }
}

int Process2(string filename)
{
    return GetBasinSizes(filename).OrderByDescending(size => size).Take(3).Aggregate(1, (prev, now) => prev * now);
}


Console.WriteLine($"Result 2: {Process2("data.input")}");

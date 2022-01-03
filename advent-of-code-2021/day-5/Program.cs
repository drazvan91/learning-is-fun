Line ParseLine(string line)
{
    var v = line
        .Split(new char[] { ' ', '-', '>', ',' }, System.StringSplitOptions.RemoveEmptyEntries)
        .Select(v => int.Parse(v))
        .ToArray();
    return new Line(v[0], v[2], v[1], v[3]);
}


IEnumerable<Line> ReadLines(string filename)
{
    return File.ReadLines(filename).Select(ParseLine);
}

const int SIZE_X = 10000;


int Part1(string filename, bool considerDiagonal)
{
    Dictionary<int, int> appearances = new Dictionary<int, int>();
    int count = 0;
    foreach (var line in ReadLines(filename))
    {

        if (!considerDiagonal && line.x1 != line.x2 && line.y1 != line.y2)
        {
            continue;
        }

        foreach (var (x, y) in line.GetPoints())
        {
            var key = x * SIZE_X + y;
            if (appearances.TryGetValue(key, out int value))
            {
                if (value == 1)
                {
                    count++;
                }
                appearances[key] = value + 1;
            }
            else
            {
                appearances.Add(key, 1);
            }
        }
    }

    return count;

}

Console.WriteLine(Part1("data.input", false));
Console.WriteLine(Part1("data.input", true));


record Line(int x1, int x2, int y1, int y2)
{
    private int GetDirection(int start, int stop)
    {
        if (start < stop) return 1;
        return start > stop ? -1 : 0;
    }

    private Func<int, bool> GetStopCondition(int start, int stop)
    {
        if (start < stop)
        {
            return (int i) => i > stop;
        }
        else if (start > stop)
        {
            return (int i) => i < stop;
        }
        return (int i) => true;
    }

    public IEnumerable<(int, int)> GetPoints()
    {
        var dirx = GetDirection(x1, x2);
        var diry = GetDirection(y1, y2);

        var stopX = GetStopCondition(x1, x2);
        var stopY = GetStopCondition(y1, y2);

        int x = x1, y = y1;
        while (!stopX(x) || !stopY(y))
        {
            yield return (x, y);
            x += dirx;
            y += diry;
        }
    }
}
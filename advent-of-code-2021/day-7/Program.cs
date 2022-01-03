IEnumerable<int[]> ReadLines(string filename)
{
    return File.ReadLines(filename).Select(line =>
        line
            .Split(',', StringSplitOptions.RemoveEmptyEntries)
            .Select(i => int.Parse(i))
            .ToArray()
    );
}

int[] ReadData(string filename)
{
    return ReadLines(filename).First();
}

IEnumerable<(int, int)> GetCosts1(string filename)
{
    var data = ReadData(filename);
    int min = data.Min();
    int max = data.Max();
    for (int i = min; i < max; i++)
    {
        int sum = data.Select(value => Math.Abs(value - i)).Sum();
        yield return (i, sum);
    }
}

int Process1(string filename)
{
    int prev = int.MaxValue;
    foreach (var (value, cost) in GetCosts1(filename))
    {
        if (prev < cost)
        {
            return prev;
        }

        prev = cost;
    }

    return prev;
}

Console.WriteLine($"Result1: {Process1("data.input")}");



IEnumerable<(int, int)> GetCosts2(string filename)
{
    var data = ReadData(filename);
    int min = data.Min();
    int max = data.Max();
    for (int i = min; i < max; i++)
    {
        int sum = data.Select(value =>
        {
            var diff = Math.Abs(value - i);
            return diff * (diff + 1) / 2;
        }).Sum();
        yield return (i, sum);
    }
}

int Process2(string filename)
{
    int prev = int.MaxValue;
    foreach (var (value, cost) in GetCosts2(filename))
    {
        if (prev < cost)
        {
            return prev;
        }

        prev = cost;
    }

    return prev;
}

Console.WriteLine($"Result2: {Process2("data.input")}");
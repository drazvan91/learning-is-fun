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

long Process(string filename, int nrDays)
{
    long[] values = new long[9];
    foreach (var fishDue in ReadData(filename))
    {
        values[fishDue]++;
    }

    for (int day = 0; day < nrDays; day++)
    {
        long zeroDay = values[0];
        for (int i = 0; i < 8; i++)
        {
            values[i] = values[i + 1];
        }

        values[8] = zeroDay;
        values[6] += zeroDay;
    }

    return values.Sum();
}

Console.WriteLine(Process("data.input", 80));
Console.WriteLine(Process("data.input", 256));
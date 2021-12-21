int[] ParseLine(string line)
{
    return line.ToCharArray().Select(c => c == '1' ? 1 : 0).ToArray();
}

(int, int) Part1(string filename)
{
    var lines = File.ReadLines(filename).Select(ParseLine);

    int[] sumBits = null;
    int linesCount = 0;
    foreach (var bits in lines)
    {
        if (sumBits == null)
        {
            sumBits = bits;
        }
        else
        {
            for (var i = 0; i < bits.Length; i++)
            {
                sumBits[i] += bits[i];
            }
        }

        linesCount++;
    }

    var gamaBits = sumBits.Select(bit => bit > (linesCount / 2) ? "1" : "0");
    var epsilonBits = sumBits.Select(bit => bit > (linesCount / 2) ? "0" : "1");

    int gama = Convert.ToInt32(string.Join("", gamaBits), 2);
    int epsilon = Convert.ToInt32(string.Join("", epsilonBits), 2);

    return (gama, epsilon);
}

var (gama1, epsilon1) = Part1("data.input");

Console.WriteLine($"Result part 1: {gama1} * {epsilon1}");
Console.WriteLine($"Result part 1 output: {gama1 * epsilon1}");


(int, int) Part2(string filename)
{
    var lines = File.ReadLines(filename).Select(ParseLine).ToList();
    var bitsCount = lines[0].Length;

    var filteredOxygen = lines;
    for (var i = 0; i < bitsCount; i++)
    {
        var groups = filteredOxygen.GroupBy(bits => bits[i]).ToList();

        int count0 = groups[0].Count();
        int count1 = groups[1].Count();
        if (count0 > count1)
        {
            filteredOxygen = groups[0].ToList();
        }
        else if (count1 > count0)
        {
            filteredOxygen = groups[1].ToList();
        }
        else
        {
            filteredOxygen = groups[0].Key == 1 ? groups[0].ToList() : groups[1].ToList();
        }

        if (filteredOxygen.Count == 1)
        {
            break;
        }
    }


    var filteredCo2 = lines;
    for (var i = 0; i < bitsCount; i++)
    {
        var groups = filteredCo2.GroupBy(bits => bits[i]).ToList();

        int count0 = groups[0].Count();
        int count1 = groups[1].Count();
        if (count0 < count1)
        {
            filteredCo2 = groups[0].ToList();
        }
        else if (count1 < count0)
        {
            filteredCo2 = groups[1].ToList();
        }
        else
            filteredCo2 = groups[0].Key == 0 ? groups[0].ToList() : groups[1].ToList();

        if (filteredCo2.Count == 1)
        {
            break;
        }
    }

    int oxygen = Convert.ToInt32(string.Join("", filteredOxygen[0]), 2);
    int co2 = Convert.ToInt32(string.Join("", filteredCo2[0]), 2);

    return (oxygen, co2);
}

var (oxygen, co2) = Part2("data.input");

Console.WriteLine($"Result part 2: {oxygen} * {co2}");
Console.WriteLine($"Result part 2 output: {oxygen * co2}");

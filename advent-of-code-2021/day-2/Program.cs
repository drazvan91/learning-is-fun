(string, int) ParseLine(string line)
{
    var split = line.Split(' ');
    return (split[0], int.Parse(split[1]));
}

(int, int) Part1(string filename)
{
    var commands = File.ReadLines(filename).Select(ParseLine);

    int horizontal = 0, depth = 0;
    foreach (var (op, value) in commands)
    {
        switch (op)
        {
            case "forward":
                horizontal += value;
                break;
            case "up":
                depth -= value;
                break;
            case "down":
                depth += value;
                break;
            default:
                throw new Exception($"Unknown operation: {op}");
        }
    }

    return (horizontal, depth);
}

var (h1, d1) = Part1("data.input");

Console.WriteLine($"Result part 1: {h1}:{d1}");
Console.WriteLine($"Result part 1 multiplied: {h1 * d1}");


(int, int, int) Part2(string filename)
{
    var commands = File.ReadLines(filename).Select(ParseLine);

    int horizontal = 0, depth = 0, aim = 0;
    foreach (var (op, value) in commands)
    {
        switch (op)
        {
            case "forward":
                horizontal += value;
                depth += aim * value;
                break;
            case "up":
                // depth -= value;
                aim -= value;
                break;
            case "down":
                // depth += value;
                aim += value;
                break;
            default:
                throw new Exception($"Unknown operation: {op}");
        }
    }

    return (horizontal, depth, aim);
}

var (h2, d2, aim) = Part2("data.input");

Console.WriteLine($"Result part 2: {h2}:{d2}:{aim}");
Console.WriteLine($"Result part 2 multiplied: {h2 * d2}");
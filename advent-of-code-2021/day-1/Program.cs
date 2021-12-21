int Part1()
{
    var linesStream = File.ReadLines("data.input").Select(int.Parse);

    int result = -1;
    int prev = 0;
    foreach (var value in linesStream)
    {
        if (result == -1)
        {
            result = 0;
        }
        else if (value > prev)
        {
            result++;
        }

        prev = value;
    }

    return result;
}

Console.WriteLine($"Increasing values: {Part1()}");

int Part2()
{
    var linesStream = File.ReadLines("data.input").Select(int.Parse);
    var queue = new Queue<int>();
    int sum = 0;
    // int prevSum = 0;
    int result = 0;

    int WINDOW_SIZE = 3;

    foreach (var value in linesStream)
    {
        int prevSum = sum;
        sum += value;
        if (queue.Count >= WINDOW_SIZE)
        {
            Console.WriteLine(queue.Count);
            int old = queue.Dequeue();
            sum -= old;

            if (prevSum < sum)
            {
                result++;
            }
        }

        queue.Enqueue(value);
    }
    return result;
}


Console.WriteLine($"Increasing window: {Part2()}");
IEnumerable<(string[], string[])> GetLines(string filename)
{
    return File.ReadLines(filename)
        .Select(line =>
        {
            var words = line.Split(new char[] { ' ', '|' }, StringSplitOptions.RemoveEmptyEntries);
            return (words.Take(10).ToArray(), words.Skip(10).Take(4).ToArray());
        }
        );
}

int[] SIMPLE_DIGITS = new int[] { 2, 3, 4, 7 };

int Process1(string filename)
{
    int count = 0;

    foreach (var (first, second) in GetLines(filename))
    {
        count += second.Count((v) => SIMPLE_DIGITS.Contains(v.Length));
    }

    return count;
}

Console.WriteLine($"Result 1: {Process1("data.input")}");


char[] Diff(string a, string b)
{
    return a.Where(c => !b.Contains(c)).ToArray();
}

int
    SA = 0b0000001,
    SB = 0b0000010,
    SC = 0b0000100,
    SD = 0b0001000,
    SE = 0b0010000,
    SF = 0b0100000,
    SG = 0b1000000;

Dictionary<int, int> DIGITS = new Dictionary<int, int>();
DIGITS.Add(SA | SB | SC | SE | SF | SG, 0);
DIGITS.Add(SC | SF, 1);
DIGITS.Add(SA | SC | SD | SE | SG, 2);
DIGITS.Add(SA | SC | SD | SF | SG, 3);
DIGITS.Add(SB | SC | SD | SF, 4);
DIGITS.Add(SA | SB | SD | SF | SG, 5);
DIGITS.Add(SA | SB | SD | SE | SF | SG, 6);
DIGITS.Add(SA | SC | SF, 7);
DIGITS.Add(SA | SB | SC | SD | SE | SF | SG, 8);
DIGITS.Add(SA | SB | SC | SD | SF | SG, 9);

Dictionary<char, int> SolveWireing(string[] wireing)
{
    Dictionary<char, int> mappings = new Dictionary<char, int>();

    string w1 = wireing.First(w => w.Length == 2);
    string w7 = wireing.First(w => w.Length == 3);
    string w4 = wireing.First(w => w.Length == 4);
    string w8 = wireing.First(w => w.Length == 7);

    char segment_a = Diff(w7, w1).First();

    string w6 = wireing.Where(w => w.Length == 6).Where(w => Diff(w1, w).Length == 1).First();
    char segment_c = Diff(w1, w6).First();
    char segment_f = Diff(w1, segment_c.ToString()).First();

    string w3 = wireing.Where(w => w.Length == 5).Where(w => Diff(w1, w).Length == 0).First();
    string w9 = wireing.Where(w => w.Length == 6).Where(w => Diff(w, w3).Length == 1 && w != w6).First();
    string w0 = wireing.Where(w => w.Length == 6).Where(w => Diff(w, w3).Length == 2 && w != w6 && w != w9).First();

    char segment_b = Diff(w9, w3).First();
    char segment_e = Diff(w0, w9).First();
    char segment_d = Diff(w9, w0).First();
    char segment_g = Diff(w9, w4).Where(c => c != segment_a).First();

    mappings.Add(segment_a, SA);
    mappings.Add(segment_b, SB);
    mappings.Add(segment_c, SC);
    mappings.Add(segment_d, SD);
    mappings.Add(segment_e, SE);
    mappings.Add(segment_f, SF);
    mappings.Add(segment_g, SG);

    return mappings;
}

int CalculateLine(string[] wireing, string[] clock)
{
    var mappings = SolveWireing(wireing);

    int result = 0;
    foreach (var clockDigit in clock)
    {
        int value = clockDigit.Select(c => mappings[c]).Sum();
        result = result * 10 + DIGITS[value];
    }

    return result;
}

int Process2(string filename)
{
    int sum = 0;
    foreach (var (wiring, clock) in GetLines(filename))
    {
        sum += CalculateLine(wiring, clock);
    }

    return sum;
}

Console.WriteLine($"Result 2: {Process2("data.input")}");